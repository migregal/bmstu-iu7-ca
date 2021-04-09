from sys import argv

import matplotlib.pyplot as plt

from utils import *
from meansquare import *


def plot(dots: list[Dot], approx: list[list[Dot]]) -> None:
    x, y = [p.x for p in dots], [p.y for p in dots]

    plt.clf()

    plt.title("Approximation using meansquare method")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(which='minor', color='k', linestyle=':')
    plt.grid(which='major', color='k')

    plt.plot(x, y, "xk")

    for a in approx:
        plt.plot([p.x for p in a], [p.y for p in a])

    plt.show()


def main():
    dots = read_dots(argv[1])

    print("Table loaded from file\n")
    print_dots(dots)

    print("\nEnter polynom degree")
    deg = read_polynom_degree()

    slae = SLAE().build(dots, deg)

    print("\nSLAE to solve\n")
    print_matrix(slae.mat)

    slae = slae.solve()

    print("\nSolved SLAE\n")
    print_matrix(slae)
    print()

    plot(dots, [Approx().get_coeffs(slae).build(dots)])


def cmp_main():
    dots1 = read_dots(argv[1])

    print("Table loaded from file\n")
    print_dots(dots1)

    print("\nEnter polynom degree")
    deg = read_polynom_degree()

    slae = SLAE().build(dots1, deg)

    print("\nSLAE to solve\n")
    print_matrix(slae.mat)

    slae = slae.solve()

    print("\nSolved SLAE\n")
    print_matrix(slae)
    print()

    approx1 = Approx().get_coeffs(slae).build(dots1)

    dots2 = read_dots(argv[2])

    print("Second table loaded from file\n")
    print_dots(dots2)

    approx2 = Approx().get_coeffs(SLAE().build(dots2, deg).solve()).build(dots2)

    plot(dots1, [approx1, approx2])


if __name__ == "__main__":
    # main()
    cmp_main()
