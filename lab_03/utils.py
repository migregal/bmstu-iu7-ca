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

def print_res(spline: Dot, polyn: Dot) -> None:
    print("        {:^8} {:^8}".format("X", "Y"))
    print("Spline  {:^8.4f} {:^8.4f}".format(spline.x, spline.y))
    print("Newton  {:^8.4f} {:^8.4f}".format(polyn.x, polyn.y))

def read_x() -> float:
    return float(input())
