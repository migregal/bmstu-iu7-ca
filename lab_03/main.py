from sys import argv

from utils import *


def main() -> None:
    dots = read_dots(argv[1])

    print("Table loaded from file\n")
    print_dots(dots)

    print("\nEnter X value: ")
    x = read_x()


if __name__ == "__main__":
    main()
