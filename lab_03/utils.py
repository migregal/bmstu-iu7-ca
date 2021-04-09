from spline import Dot


def read_dots(fname: str) -> list[Dot]:
    dots = []

    with open(fname) as fin:
        for line in fin.readlines():
            dots += [Dot(*list(map(float, line.split()[:2])))]

    return dots


def print_dots(dots: list[Dot]) -> None:
    print("{:^8} {:^8}".format("X", "Y"))
    for i in dots:
        print("{:<8.2f} {:<8.2f}".format(i.x, i.y))


def read_x() -> int:
    return int(input())
