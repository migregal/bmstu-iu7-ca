from __future__ import annotations


class Dot(object):
    x: float
    y: float

    def __init__(self, _x: float, _y: float) -> None:
        super().__init__()

        self.x, self.y = _x, _y

    def __lt__(self, other: Dot):
        return self.x < other.x
