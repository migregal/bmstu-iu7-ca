from __future__ import annotations
from copy import deepcopy
from math import prod


class Dot(object):
    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x, self.y = x, y

    def __str__(self):
        return "(" + str(self.x) + ";" + str(self.y) + ")"


class Polynomial(object):
    terms: list[callable[float]:float]

    def __init__(self, terms: list[callable[float]:float]):
        self.terms = terms

    def __call__(self, arg: float) -> float:
        return sum([term(arg) for term in self.terms])


class NewtonPolynomial(Polynomial):

    @staticmethod
    def build(points: list[Dot], arg: Dot, n: int) -> NewtonPolynomial:
        table = NewtonPolynomial._make_table(points, arg, n)

        return NewtonPolynomial(
            [lambda x:table[1][0]] +
            [NewtonPolynomial._term(table[i][0],  table[0][:i - 1])
             for i in range(2, len(table))]
        )

    @staticmethod
    def _term(va: float, vl: list[float]) -> callable:
        return lambda x: va * prod(map(lambda a: (x - a), vl))

    @staticmethod
    def _make_table(points: list[Dot], arg: Dot, n: int) -> list[list[Dot]]:
        base = sorted(
            sorted(points, key=lambda p: abs(p.x - arg.x))[:n + 1],
            key=lambda p: p.x
        )

        t = [[None for i in range(len(base))] for j in range(n + 2)]

        for i in range(len(t[0])):
            t[0][i], t[1][i] = base[i].x, base[i].y

        for i in range(2, len(t)):
            for j in range(len(base) - i + 1):
                t[i][j] = (t[i - 1][j] - t[i - 1][j + 1]) / \
                    (t[0][j] - t[0][j + i - 1])

        return t


class BiNewtonPolynomial(Polynomial):

    __second_interp_set: list
    __ny: float

    def __init__(self, temp: list, ny: int):
        self.__second_interp_set = temp
        self.__ny = ny

    @staticmethod
    def build(dots: list[list[Dot]], arg: Dot, nx: int, ny: int) -> BiNewtonPolynomial:
        points = deepcopy(dots)
        xrow, ycol, matrix = BiNewtonPolynomial.__split_data(points)
        baseX, baseY = BiNewtonPolynomial.__get_bases(xrow, ycol, arg, nx, ny)

        t = [[None for i in range(nx + 1)] for j in range(ny + 1)]

        k = 0
        for i in range(xrow.index(baseX[0]), xrow.index(baseX[0]) + nx + 1):
            l = 0
            for j in range(ycol.index(baseY[0]), ycol.index(baseY[0]) + ny + 1):
                t[l][k] = matrix[i][j]
                l += 1
            k += 1

        second_set = []
        for i in range(len(t)):
            for j in range(len(baseX)):
                t[i][j].y = baseX[j].x
                t[i][j].x, t[i][j].y = t[i][j].y, t[i][j].x
            second_set += [
                Dot(
                    baseY[i].x,
                    NewtonPolynomial.build(t[i], Dot(arg.y, arg.x), nx)
                )
            ]

        return BiNewtonPolynomial(
            second_set,
            ny
        )

    @staticmethod
    def __split_data(matrix: list[list[Dot]]) -> tuple[list[Dot], list[Dot], list[list[Dot]]]:
        xrow = matrix[0]
        matrix = matrix[1:]
        ycol = [row[0] for row in matrix]
        matrix = [row[1:] for row in matrix]

        return xrow, ycol, matrix

    @staticmethod
    def __get_bases(x: list[Dot], y: list[Dot], arg: Dot, nx: int, ny: int):
        baseX = sorted(
            sorted(x, key=lambda p: abs(p.x - arg.x))[:nx + 1],
            key=lambda p: p.x
        )
        baseY = sorted(
            sorted(y, key=lambda p: abs(p.x - arg.y))[:ny + 1],
            key=lambda p: p.x
        )
        return baseX, baseY

    def __call__(self, arg: Dot) -> float:
        t = [Dot(i.x, i.y(arg.y)) for i in self.__second_interp_set]
        return NewtonPolynomial.build(t, arg, self.__ny)(arg.x)
