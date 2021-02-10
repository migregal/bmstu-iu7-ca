from sys import argv

import matplotlib.pyplot as plt
import numpy as np

from utils import *
from polynomial import *

import pylab as py


def plot(dots: list[float], polynomials: list[Polynomial]) -> None:
    x, y = [p[0] for p in dots], [p[1] for p in dots]
    a, b = min(x), max(x)
    x_arg = np.linspace(a, b)

    plt.clf()

    for i in range(len(polynomials)):
        plt.subplot(1, len(polynomials), i + 1)
        plt.title(type(polynomials[i]).__name__)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid(which='minor', color='k', linestyle=':')
        plt.grid(which='major', color='k')
        plt.minorticks_on()

        plt.plot(x, y, "xk")

        plt.plot(x_arg, [polynomials[i](arg) for arg in x_arg])

    plt.show()


if __name__ == "__main__":
    dots = read_dots(argv[1])

    print("Loaded table:")

    print_dots(dots)

    print("Enter polynomial degree and X value:")
    deg, x = read_func_data()

    newton = NewtonPolynomial.build(dots, x, deg)

    print("Newton value in {: <5.6g} is {: <5.6g}".format(x, newton(x)))

    hermite = HermitePolynomial.build(dots, x, deg)

    print("Hermite value in {: <5.6g} is {: <5.6g}".format(x, hermite(x)))

    inv_dots = [[p[1], p[0]] for p in dots]
    root = NewtonPolynomial.build(inv_dots, 0.0, deg)(0.0)

    print(
        "Root found by inverted interpolation method is {: <5.6g}".format(root))

    plot(dots, [newton, hermite])
