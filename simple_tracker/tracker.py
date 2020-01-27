
class Tracker():

    def __init__(self, min_distance=5):
        self.objects = {}
        # self.objects = []
        self.max_distance = 5
        self.count = 0
        # TODO add frame sizing for:
        #   - dynamic processing of min_distance
        #   - process objects moving in/out of frame

    def register(self, x, y):
        self.count += 1
        # self.objects.append(TrackedObject(self.count, x, y))
        self.objects[self.count] = (x, y)

    def deregister(self, obj):
        self.objects.remove(obj)

    @staticmethod
    def distance(x1, y1, x2, y2):
        return ((x2-x1)**2+(y2-y1)**2)**(1/2)

    def update(self, other):
        """Update objects and determine if they need to be tracked

        Args:
            objs (list[tuple]): list of x, y coords
                example: [(x, y), (x, y)...]

        TODO:
            - handle objects with no changes
            - avoid clashes (two objects have the same nearest)
            - future: handle spontanious additions in the middle of the frame
        """
        if len(other) > 0:
            additions = []
            for oth in other:
                tracked = False
                for key, value in self.objects.items():
                    x1, y1 = value
                    x2, y2 = oth
                    if self.distance(x1, y1, x2, y2) <= self.max_distance:
                        print('{} -> {}'.format(value, oth))
                        self.objects[key] = oth
                        tracked = True
                        # TODO put a min() in here somewhere
                if not tracked:
                    additions.append(oth)
                    print('-> {}'.format(oth))

            if len(additions) > 0:
                for addition in additions:
                    self.register(addition[0], addition[1])

    def __str__(self):
        return str(self.objects)


if __name__ == "__main__":
    t = Tracker()
    t.register(10, 10)
    t.register(20, 10)
    t.register(30, 10)

    f = [(10, 14), (20, 15), (30, 15), (40, 15)]

    print("")
    t.update(f)
    print("")
    print(t)
