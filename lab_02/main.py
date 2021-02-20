from sys import argv

import matplotlib.pyplot as plt
import numpy as np

from copy import deepcopy

from utils import *
from polynomial import *


def plot(dots: list[list[Dot]], polynomial: BiNewtonPolynomial) -> None:
    plt.clf()

    matrix = deepcopy(dots)
    xrow = matrix[0]
    matrix = matrix[1:]
    ycol = [row[0] for row in matrix]
    matrix = [row[1:] for row in matrix]

    x_s, z_s, y_s = [], [], []
    for i in range(len(xrow)):
        for j in range(len(ycol)):
            x_s.append(xrow[i].x)
            y_s.append(ycol[j].x)
            z_s.append(matrix[i][j].x)

    axis = plt.figure(1).add_subplot(111, projection='3d')
    axis.set_xlabel('X')
    axis.set_ylabel('Y')
    axis.set_zlabel('Z')
    axis.scatter(x_s, y_s, z_s, color='red')

    x_arg = np.linspace(min([x.x for x in dots[0]]),
                        max([x.x for x in dots[0]]), 20)
    y_arg = np.linspace(min([y.x for y in [row[0] for row in dots]]),
                        max([y.x for y in [row[0] for row in dots]]), 20)
    z_arg = np.empty([len(x_arg), len(y_arg)])

    for i in range(len(x_arg)):
        for j in range(len(y_arg)):
            z_arg[i][j] = polynomial(Dot(x_arg[i], y_arg[j]))

    X, Y = np.meshgrid(x_arg, y_arg)
    axis.plot_wireframe(X, Y, z_arg)

    plt.show()


if __name__ == "__main__":
    dots = read_dots(argv[1])

    print("Loaded table:")

    print_dots(dots)

    print("Enter polynomial X, Y degree and X value:")
    degx, degy, x, y = read_func_data()

    polynomial = BiNewtonPolynomial.build(dots, Dot(x, y), degx, degy)

    print(
        "Value in ({: >5.6g}; {: >5.6g}) is {: <5.6g}".format(
            x,
            y,
            polynomial(Dot(x, y))
        )
    )

    plot(dots, polynomial)
