from sys import argv

from utils import read_dots, print_dots

def main():

    dots = read_dots(argv[1])

    print_dots(dots)


if __name__ == "__main__":
    main()
