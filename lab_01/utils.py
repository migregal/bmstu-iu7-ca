def read_dots(fname: str) -> list[list[float]]:
    dots = []

    with open(fname) as fin:
        for line in fin.readlines():
            dots += [list(map(float, line.split()))]

    return sorted(dots, key=lambda p: p[1])


def print_dots(dots: list[float]) -> None:
    for d in dots:
        print(d)


def read_func_data() -> tuple[int, float]:
    deg, x = map(float, input().split())

    return int(deg), x
