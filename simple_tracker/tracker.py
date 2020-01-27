
class Tracker():

    def __init__(self, max_distance=5):
        self.points = {}
        # self.objects = []
        self.max_distance = max_distance
        self.count = 0
        # TODO add frame sizing for:
        #   - dynamic processing of min_distance
        #   - process objects moving in/out of frame

    def register(self, x, y):
        self.points[self.count] = (x, y)
        self.count += 1

    def deregister(self, obj):
        self.points.remove(obj)

    @staticmethod
    def create_buffer(items):
        count = 0
        buffer = {}
        for i in items:
            buffer[count] = i
            count += 1
        return buffer

    @staticmethod
    def distance(x1, y1, x2, y2):
        return ((x2-x1)**2+(y2-y1)**2)**(1/2)

    def update(self, points, debug=False):
        """Update objects and determine if they need to be tracked

        Args:
            points (list[tuple]): list of x, y coords
                example: [(x, y), (x, y)...]

        TODO:
            - handle objects with no changes
            - avoid clashes (two objects have the same nearest)
            - future: handle spontanious additions in the middle of the frame
        """
        if len(points) > 0:
            prev_points = self.points
            next_points = self.create_buffer(points)

            additions = []
            movements = {}

            if debug:
                changes = []

            for p2, (x2, y2) in next_points.items():
                counted = False
                distances = {}
                for p1, (x1, y1) in prev_points.items():
                    distance = self.distance(x1, y1, x2, y2)
                    if distance <= self.max_distance:
                        distances[p1] = (x2, y2, distance)
                if len(distances) > 0:
                    nearest = min(distances.items(), key=lambda x: x[1][2])
                    movements[nearest[0]] = nearest[1][0:2]
                    counted = True
                if not counted:
                    additions.append((x2, y2))

        if len(additions) > 0:
            for x, y in additions:
                if debug:
                    changes.append(('', (x, y)))
                self.register(x, y)

        if len(movements) > 0:
            for i, (x2, y2) in movements.items():
                if debug:
                    changes.append((self.points[i], (x2, y2)))
                self.points[i] = (x2, y2)

        if debug:
            if len(changes) > 0:
                for old, new in changes:
                    print('{} -> {}'.format(old, new))

    def __str__(self):
        return str(self.points)

    def __len__(self):
        return len(self.points)


# Some testing down here
if __name__ == "__main__":
    points = [(10, 10), (17, 10), (30, 10)]
    buffer = [(10, 15), (15, 10), (30, 15), (40, 15)]

    t = Tracker()
    for point in points:
        t.register(point[0], point[1])

    print(t)
    t.update(buffer, debug=True)
    print(t)
