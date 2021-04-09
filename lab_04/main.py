from sys import argv

from utils import *
from meansquare import *

def main():

    dots = read_dots(argv[1])

    print("Table loaded from file\n")
    print_dots(dots)

    print("\nEnter polynom degree")
    deg = read_polynom_degree()

    slae = SLAE().build(dots, deg).solve()

    for i in slae:
        print(i)

    res = Approx().get_coeffs(slae).build(dots)


if __name__ == "__main__":
    main()
