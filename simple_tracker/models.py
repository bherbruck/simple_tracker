class Tracker:
    def __init__(self, max_distance=5, timeout=40):
        '''
        A simple object tracker

        Args:
            max_distance (int, optional):
                maximum distance an item can move between updates, generally in pixels,
                defaults to 5.
            timeout (int, optional):
                number of update ticks (frames) to wait for an item to be deleted,
                defaults to 40.
        '''
        self.points = {}
        self.max_distance = max_distance
        self.timeout = timeout
        self.count = 0
        self.frame = 0

    def get(self, key):
        """
        Get a dict representation of a tracked point

        Args:
            key (int):
                key of the tem to get

        Returns:
            dict:
                dict representation of the item
        """
        try:
            point = self.points[key]
            return {'id': key, 'x': point[0], 'y': point[1], 'distance': point[2],
                    'last_frame': point[3]}
        except KeyError:
            return None

    @staticmethod
    def distance(x1, y1, x2, y2):
        return abs(((x2-x1)**2+(y2-y1)**2)**(1/2))

    def register(self, x, y):
        self.points[self.count] = (x, y,  0, self.frame)
        self.count += 1

    def deregister(self, k):
        del self.points[k]

    def get_timeouts(self, points, tracking_lost_cb):
        timeouts = []
        for k, v in self.points.items():
            # deregister and count
            if self.frame >= v[3] + self.timeout:
                # tracking lost callback
                if tracking_lost_cb is not None:
                    if tracking_lost_cb(self.get(k)):
                        timeouts.append(self.get(k))
                else:
                    timeouts.append(self.get(k))
        return timeouts

    def update(self, points, tracking_found_cb=None, tracking_lost_cb=None):
        """
        Update object tracking, tracking can be fine-tuned using callbacks

        Args:
            points (list[tuple]):
                list of x, y coords
            tracking_found_cb ([type], optional):
                function to call when a new item is found,
                passes a tuple of the point found '(x, y))',
                return True from the callback function to start tracking the point,
                defaults to None
            tracking_lost_cb ([type], optional):
                function to call when an item loses tracking,
                passes a dictionary of the point lost '{'x': x, 'y': y, 'distance': d, ...}',
                return True from the callback function to stop tracking the point and return,
                defaults to None

        Returns:
            list:
                list of points that lost tracking (for counting)
        """
        deletions = self.get_timeouts(points, tracking_lost_cb)
        movements = {}
        additions = []

        for x2, y2 in points:
            processed = False
            distances = {}

            # get all the distances
            for k, v in self.points.items():
                distance = Tracker.distance(v[0], v[1], x2, y2)
                if distance <= self.max_distance:
                    distances[k] = (x2, y2, distance)

            # filter the distances
            if len(distances) > 0:
                k, v = min(distances.items(), key=lambda x: x[1][2])
                movements[k] = (v[0], v[1], self.points[k][2] + v[2], self.frame)
                processed = True

            if not processed:
                # tracking found callback
                if tracking_found_cb is not None:
                    if tracking_found_cb((x2, y2)):
                        additions.append((x2, y2))
                else:
                    # add new item
                    additions.append((x2, y2))

        # deregister old points
        for point in deletions:
            self.deregister(point['id'])
            
        # add new points
        for point in additions:
            self.register(point[0], point[1])
            
        # update points
        self.points.update(movements)

        self.frame += 1
        return deletions

    def __str__(self):
        return str(self.points)

    def __len__(self):
        return len(self.points)

    def __dict__(self):
        return {k: self.get(k) for k, v in self.points.items()}
