from typing import Sequence


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'({self.x}, {self.y})'


class Line:
    def __init__(self, a: Point, b: Point):
        self.a = a
        self.b = b

    def slope(self):
        return (self.b.y - self.a.y) / (self.b.x - self.a.x)

    def __repr__(self):
        return f'Line: ({self.a}, {self.b})'


def find_parallel(lines: Sequence[Line]):
    lines = list(lines)
    grouped_lines = []
    while lines:
        line = lines.pop(0)
        result = [line]
        for next_line in lines:
            if line.slope() == next_line.slope():
                result.append(next_line)
                lines.remove(next_line)
        grouped_lines.append(result)

    print(*sorted(grouped_lines, key=len, reverse=True), sep='\n')

    return grouped_lines


l1 = Line(Point(-7, -3), Point(-2, 2))
l2 = Line(Point(1, 1), Point(5, 5))
l3 = Line(Point(-8, 2), Point(-2, 5))
l4 = Line(Point(6, 7), Point(12, 7))
l5 = Line(Point(-8, 9), Point(-4, 5))
l6 = Line(Point(0, -3), Point(5, -8))
l7 = Line(Point(7, 5), Point(9, 1))
l8 = Line(Point(3, 6), Point(7, 10))

find_parallel([l1, l2, l3, l4, l5, l6, l7, l8])
