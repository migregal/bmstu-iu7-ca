from sys import argv

import matplotlib.pyplot as plt

from utils import *
from meansquare import *


def plot(dots: list[Dot], approx: list[Dot]) -> None:
    x, y = [p.x for p in dots], [p.y for p in dots]
    a, b = min(x), max(x)
    x_arg = np.linspace(a, b)

    plt.clf()

    plt.title("Approximation using meansquare method")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(which='minor', color='k', linestyle=':')
    plt.grid(which='major', color='k')

    plt.plot(x, y, "xk")

    plt.plot([p.x for p in approx], [p.y for p in approx])

    plt.show()

def main():

    dots = read_dots(argv[1])

    print("Table loaded from file\n")
    print_dots(dots)

    print("\nEnter polynom degree")
    deg = read_polynom_degree()

    slae = SLAE().build(dots, deg).solve()

    plot(dots, Approx().get_coeffs(slae).build(dots))


if __name__ == "__main__":
    main()
