from sys import argv

from utils import *

def main():

    dots = read_dots(argv[1])

    print("Table loaded from file\n")
    print_dots(dots)

    print("\nEnter polynom degree")
    deg = read_polynom_degree()


if __name__ == "__main__":
    main()
