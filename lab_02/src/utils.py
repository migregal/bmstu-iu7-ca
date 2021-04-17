from polynomial import Dot


def read_dots(fname: str) -> list[list[Dot]]:
    dots = []

    with open(fname) as fin:
        dots += [[Dot(x, None)
                  for x in list(map(float, fin.readline().split()))]]

        for line in fin.readlines():
            dots += [[Dot(x, None) for x in list(map(float, line.split()))]]

    return sorted(dots, key=lambda p: p[0].x)


def print_dots(dots: list[list[Dot]]) -> None:
    print(" Y \ X ", end="")
    for i in dots[0]:
        print("{: >6.2f}".format(i.x), end=" ")
    print()

    for row in dots[1:]:
        for col in row:
            print("{: >6.2f}".format(col.x), end=" ")
        print()


def read_func_data() -> tuple[int, int, float, float]:
    degx, degy, x, y = map(float, input().split())

    return int(degx), int(degy), x, y
