class Tracker():
    # TODO add frame sizing for:
    #   - dynamic processing of min_distance
    #   - process objects moving in/out of frame

    def __init__(self, max_distance=5, timeout=40):
        self.points = {}
        self.max_distance = max_distance
        self.timeout = timeout
        self.count = 0
        self.frame = 0

    def get(self, key):
        """[summary]

        Args:
            key (int): key of the tem to get

        Returns:
            dict: dict representation of the item
        """
        try:
            point = self.points[key]
            return {'x': point[0], 'y': point[1], 'distance': point[2],
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

    def update(self, points, tracking_found_cb=None, tracking_lost_cb=None):
        """Update objects and determine if they need to be tracked

        Args:
            points (list[tuple]): list of x, y coords
            tracking_found_cb ([type], optional): function to call when a new item is found
            tracking_lost_cb ([type], optional): function to call when an item loses tracking

        Returns:
            list: list of points that lost tracking (to be counted)
        """
        counts = []
        if len(points) > 0:
            movements = {}

            for x2, y2 in points:
                counted = False
                distances = {}

                # get all the distances
                for k, v in self.points.items():
                    # deregister and count
                    if self.frame >= v[3] + self.timeout:
                        # tracking lost callback
                        if tracking_lost_cb is not None:
                            if tracking_lost_cb(self.get(k)):
                                counts.append(v)
                        self.deregister(k)
                        continue

                    distance = Tracker.distance(v[0], v[1], x2, y2)
                    if distance <= self.max_distance:
                        distances[k] = (x2, y2, distance)

                # filter the distances
                if len(distances) > 0:
                    k, v = min(distances.items(), key=lambda x: x[1][2])
                    movements[k] = (v[0], v[1], self.points[k][2] + v[2],
                                    self.frame)
                    counted = True

                if not counted:
                    # tracking found callback
                    if tracking_found_cb is not None:
                        if tracking_found_cb({'x': x2, 'y': y2}):
                            self.register(x2, y2)
                    else:
                        # add new item
                        self.register(x2, y2)

            # update points
            self.points.update(movements)

        self.frame += 1
        return counts

    def __str__(self):
        return str(self.points)

    def __len__(self):
        return len(self.points)

    def __dict__(self):
        return {k: self.get(k) for k, v in self.points.items()}
