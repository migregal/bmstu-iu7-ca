from sys import argv

from polynomial import NewtonPolynomial
from spline import Spline
from utils import *


def main() -> None:
    dots = read_dots(argv[1])

    print("Table loaded from file\n")
    print_dots(dots)

    print("\nEnter X value: ")
    x = read_x()

    res = Spline(dots).solve(x)
    poly = Dot(x, NewtonPolynomial.build([[d.x, d.y] for d in dots], x, 3)(x))

    print_res(res, poly)


if __name__ == "__main__":
    main()
