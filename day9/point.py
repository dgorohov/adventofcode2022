import math


class Point:
    def __init__(self, pos):
        self.__pos = pos

    def distance(self, to):
        return math.hypot(to[0] - self[0], to[1] - self[1])

    def __dir(self, index):
        _v = self[index]
        if _v != 0:
            _v = math.floor(_v / abs(_v))
        return _v

    def direction(self):
        return Point((self.__dir(0), self.__dir(1)))

    def __sub__(self, other):
        return Point((self[0] - other[0], self[1] - other[1]))

    def __add__(self, other):
        return Point((self[0] + other[0], self[1] + other[1]))

    def __getitem__(self, item):
        return self.__pos[item]

    def __setitem__(self, key, value):
        self.__pos[key] = value

    def __repr__(self):
        return f"Point({self[0]}, {self[1]})"


def move_rope(rope):
    for p in range(len(rope) - 1):
        p1, p2 = Point(rope[p]), Point(rope[p + 1])
        if p1.distance(p2) >= 2:
            rope[p + 1] = p2 + (p1 - p2).direction()
    return rope


def __match_direction(line):
    match line.split(' '):
        case ['R', pos]:
            return pos, Point((1, 0))
        case ['L', pos]:
            return pos, Point((-1, 0))
        case ['D', pos]:
            return pos, Point((0, 1))
        case ['U', pos]:
            return pos, Point((0, -1))


def steps(data):
    for line in data:
        _steps, _dir = __match_direction(line)
        for _ in range(int(_steps)):
            yield _dir
