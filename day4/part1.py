from functools import reduce

from core import load_data


def expand(value):
    value = value.split('-')
    return set(range(int(value[0]), int(value[1]) + 1))


def is_overlap(a, b):
    return len(a - b) == 0 or len(b - a) == 0


def solution():
    data = load_data("input.txt")

    # data = [
    #     "2-4,6-8",
    #     "2-3,4-5",
    #     "5-7,7-9",
    #     "2-8,3-7",
    #     "6-6,4-6",
    #     "2-6,4-8"
    # ]

    def reducer(a, b):
        left, right = list(map(lambda x: expand(x), b.split(',')))
        return a + (1 if is_overlap(left, right) else 0)

    data = reduce(reducer, data, 0)

    return data


if __name__ == '__main__':
    print(solution())
