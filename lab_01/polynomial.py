from __future__ import annotations
from structs import Point
from math import prod


class Polynomial(object):
    terms: list[callable[float]:float]

    def __init__(self, terms: list[callable[float]:float]):
        self.terms = terms

    def __call__(self, arg: float) -> float:
        return sum([term(arg) for term in self.terms])


class NewtonPolynomial(Polynomial):

    @staticmethod
    def build(points: list[Point], arg: float, degree: int) -> NewtonPolynomial:
        table = NewtonPolynomial._make_table(points, arg, degree)

        return NewtonPolynomial(
            [lambda x:table[1][0]] +
            [NewtonPolynomial._term(table[i][0],  table[0][:i - 1])
             for i in range(2, len(table))]
        )

    @staticmethod
    def _term(va: float, vl: list[float]) -> callable:
        return lambda x: va * prod(map(lambda a: (x - a), vl))

    @staticmethod
    def _make_table(points: list[Point], arg: float, degree: int) -> list[list[float]]:
        base = sorted(sorted(points, key=lambda p: abs(p.x - arg))[:degree+1])

        t = [[None for i in range(len(base))] for j in range(degree + 2)]

        for i in range(len(t[0])):
            t[0][i] = base[i].x
            t[1][i] = base[i].y

        for i in range(2, len(t)):
            for j in range(len(base) - i + 1):
                t[i][j] = (t[i - 1][j] - t[i - 1][j + 1]) / \
                    (t[0][j] - t[0][j + i - 1])

        return t


class HermitePolynomial(NewtonPolynomial):

    @staticmethod
    def build(points: list[Point], arg: float, degree: int) -> HermitePolynomial:
        table = HermitePolynomial._make_table(points, arg, degree)

        return HermitePolynomial(
            [lambda x:table[1][0]] +
            [HermitePolynomial._term(table[i][0],  table[0][:i - 1])
             for i in range(2, len(table))]
        )

    @staticmethod
    def _make_table(points: list[Point], arg: float, degree: int) -> list[list[float]]:
        base = []

        for p in sorted(points, key=lambda p: abs(p.x - arg)):
            base += [Point(p.x, p.y, p.dy[:j]) for j in range(len(p.dy) + 1)]

        base = sorted(base[:degree + 1], key=lambda p: (p.x, -len(p.dy)))

        t = [[None for i in range(len(base))] for j in range(degree + 2)]

        for i in range(len(base)):
            p = base[i]
            t[0][i], t[1][i] = p.x, p.y

            for j in range(2, len(p.dy)+2):
                t[j][i] = p.dy[j - 2]

        for i in range(2, len(t)):
            for j in range(len(base) - i + 1):
                if t[i][j]:
                    continue

                dx = t[0][j] - t[0][j + i - 2]
                if dx == 0:
                    dx = t[0][j] - t[0][j + i - 1]

                t[i][j] = (t[i - 1][j] - t[i - 1][j + 1]) / dx

        return t
