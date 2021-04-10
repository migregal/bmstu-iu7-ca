from sys import argv

from spline import Spline
from utils import *


def main() -> None:
    dots = read_dots(argv[1])

    print("Table loaded from file\n")
    print_dots(dots)

    print("\nEnter X value: ")
    x = read_x()

    res = Spline(dots).solve(x)

    print("\nValue in {:<5.2f} is {:<5.4f}\n".format(res.x, res.y))


if __name__ == "__main__":
    main()
