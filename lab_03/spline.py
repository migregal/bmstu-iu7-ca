from __future__ import annotations


class Dot(object):
    x: float
    y: float

    def __init__(self, _x: float, _y: float) -> None:
        super().__init__()

        self.x, self.y = _x, _y

    def __lt__(self, other: Dot):
        return self.x < other.x


class Spline(object):
    dots: list[Dot]

    def __init__(self, _dots: list[Dot]) -> None:
        super().__init__()
        self.dots = _dots

    def get_pos(self, d: Dot) -> int:
        i = 1

        while i < len(self.dots) and self.dots[i].x < d.x:
            i += 1

        return i - 1

    def solve(self, x: float) -> Dot:
        arg_x = [d.x for d in self.dots]
        arg_y = [d.y for d in self.dots]

        a = arg_y[:-1]

        c = [0] * (len(self.dots) - 1)

        # Начальные известные значения коэффициентов
        ksi_coef, eta_coef = [0, 0], [0, 0]

        # Прямой проход
        for i in range(2, len(self.dots)):
            xhi, xhi_1 = arg_x[i] - arg_x[i - 1], arg_x[i - 1] - arg_x[i - 2]
            yhi, yhi_1 = arg_y[i] - arg_y[i - 1], arg_y[i - 1] - arg_y[i - 2]

            fi = 3 * (yhi / xhi - yhi_1 / xhi_1)

            # Вычисление прогоночных коэффициентов
            ksi_coef.append(-xhi /
                            (xhi_1 * ksi_coef[i - 1] + 2 * (xhi_1 + xhi)))
            eta_coef.append(
                (fi - xhi_1 * eta_coef[i - 1]) / (
                        xhi_1 * ksi_coef[i - 1] + 2 * (xhi_1 + xhi)))

        c[len(self.dots) - 2] = eta_coef[-1]

        # Обратный проход
        for i in range(len(self.dots) - 2, 0, -1):
            c[i - 1] = ksi_coef[i] * c[i] + eta_coef[i]

        b, d = [], []
        for i in range(1, len(self.dots) - 1):
            xhi = arg_x[i] - arg_x[i - 1]
            yhi = arg_y[i] - arg_y[i - 1]
            b.append(yhi / xhi - (xhi * (c[i] + 2 * c[i - 1])) / 3)
            d.append((c[i] - c[i - 1]) / (3 * xhi))

        b.append((arg_y[-1] - arg_y[-2]) / (arg_x[-1] - arg_x[-2]) -
                 ((arg_x[-1] - arg_x[-2]) * 2 * c[-1]) / 3)
        d.append(-c[len(self.dots) - 2] / (3 * (arg_x[-1] - arg_x[-2])))

        pos = self.get_pos(Dot(x, 0))

        res = a[pos] + \
              b[pos] * (x - self.dots[pos].x) + \
              c[pos] * (x - self.dots[pos].x) ** 2 + \
              d[pos] * (x - self.dots[pos].x) ** 3

        return Dot(x, res)
