from meansquare import Dot


def read_dots(fname: str) -> list[Dot]:
    dots = []

    with open(fname) as fin:

        for line in fin.readlines():
            dots += [Dot(*line.split()[:3])]

    return dots

def print_dots(dots: list[Dot]) -> None:
    print("{:8} {:8} {:8}".format("X", "Y", "Weight"))
    for i in dots:
        print("{:8} {:8} {:8}".format(i.x, i.y, i.weight))
