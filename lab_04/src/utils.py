from meansquare import Dot


def read_dots(fname: str) -> list[Dot]:
    dots = []

    with open(fname) as fin:
        for line in fin.readlines():
            dots += [Dot(*list(map(float, line.split()[:3])))]

    return dots


def print_dots(dots: list[Dot]) -> None:
    print("{:^8} {:^8} {:^8}".format("X", "Y", "Weight"))
    for i in dots:
        print("{:<8.2f} {:<8.2f} {:<8.2f}".format(i.x, i.y, i.weight))


def read_polynom_degree() -> int:
    return int(input())


def print_matrix(mat: list[list[float]]) -> None:
    for line in mat:
        print(('[' + ', '.join(["{:8.2f}"] * len(line)) + ']').format(*line))
