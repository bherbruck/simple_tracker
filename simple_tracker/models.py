class Tracker:
    def __init__(self, max_distance=5, timeout=40):
        '''
        A simple centroid object tracker

        Args:
            max_distance (int, optional):
                maximum distance an item can move between updates, generally in pixels,
                defaults to 5.
            timeout (int, optional):
                number of update ticks (frames) to wait for an item to be deleted,
                defaults to 40.

        TODO:
            Refactor output of Tracker.points to include amount of frames
        '''
        self.points = {}
        self.max_distance = max_distance
        self.timeout = timeout
        self.count = 0
        self.frame = 0

    @staticmethod
    def distance(x1, y1, x2, y2):
        return abs(((x2-x1)**2+(y2-y1)**2)**(1/2))

    def start_tracking(self, x, y):
        self.points[self.count] = (x, y,  0, self.frame)
        self.count += 1

    def stop_tracking(self, k):
        del self.points[k]

    def get_timeouts(self, tracking_lost_cb=None):
        """Get all the points that have not been seen for longer than the timeout threshold

        Args:
            tracking_lost_cb (function) function to call when a point is lost

        Returns:
            list: list of dicts representation of the points
        
        TODO:
            return dict instead of list of dicts
        """
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

    def get_closest(self, x, y, tracking_update_cb=None):
        """Get the closest active point

        Args:
            x (int): x
            y (int): y
            tracking_found_cb (function, optional): not implemented

        Returns:
            dict: {<id>: (<x>, <y>, <distance>, <frame>)}
        """
        distances = {}
        # get all the distances
        for k, v in self.points.items():
            distance = Tracker.distance(v[0], v[1], x, y)
            if distance <= self.max_distance:
                distances[k] = (x, y, distance)

        # filter the distances
        if len(distances) > 0:
            k, v = min(distances.items(), key=lambda x: x[1][2])
            return {k: (v[0], v[1], self.points[k][2] + v[2], self.frame)}
        else:
            return None

    def update(self, points, tracking_found_cb=None, tracking_lost_cb=None):
        """
        Update object tracking, tracking can be fine-tuned using callbacks

        Args:
            points (list[tuple]):
                list of x, y coords
            tracking_found_cb (function, optional):
                function to call when a new item is found,
                passes a tuple of the point found '(x, y))',
                return True from the callback function to start tracking the point,
                defaults to None
            tracking_lost_cb (function, optional):
                function to call when an item loses tracking,
                passes a dictionary of the point lost '{'x': x, 'y': y, 'distance': d, ...}',
                return True from the callback function to stop tracking the point and return,
                defaults to None

        Returns:
            list:
                list of points that lost tracking (for counting)
        """
        movements = {}
        additions = []

        for x, y in points:
            # find the closest active point
            closest = self.get_closest(x, y)
            if closest is not None:
                movements.update(closest)
            # add point if it isn't close to any active points
            else:
                # tracking found callback
                if tracking_found_cb is not None:
                    if tracking_found_cb((x, y)):
                        additions.append((x, y))
                else:
                    # add new item
                    additions.append((x, y))

        # start tracking new points
        for point in additions:
            self.start_tracking(point[0], point[1])
        # update active points
        self.points.update(movements)
        # stop tracking old points
        deletions = self.get_timeouts(tracking_lost_cb)
        for point in deletions:
            self.stop_tracking(point['id'])

        self.frame += 1
        return deletions

    def __str__(self):
        return str(self.points)

    def __len__(self):
        return len(self.points)

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

    def __dict__(self):
        return {k: self.get(k) for k, v in self.points.items()}
