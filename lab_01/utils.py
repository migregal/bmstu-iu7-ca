from structs import Point


def read_dots(fname: str) -> list[Point]:
    dots = []

    with open(fname) as fin:
        for line in fin.readlines():
            coords = list(map(float, line.split()))

            dots.append(
                Point(
                    coords[0],
                    coords[1],
                    coords[2:]
                )
            )

    return sorted(dots, key=lambda p: p.y)


def print_dots(dots: list[Point]) -> None:
    for d in dots:
        print(d)


def read_func_data() -> tuple[int, float]:
    deg, x = map(float, input().split())

    return int(deg), x
