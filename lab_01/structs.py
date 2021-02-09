class Point(object):
    x: float
    y: float
    dy: list[float]

    def __init__(self, x: float, y: float, dy: float = list()):
        self.x = x
        self.y = y
        self.dy = dy

    def __lt__(self, other):
        return (self.x, self.y) < (other.x, other.y)

    def __str__(self):
        return "{: <5.6f} {: <5.6f} ".format(self.x, self.y) + str(self.dy)
