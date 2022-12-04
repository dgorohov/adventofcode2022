from functools import reduce
from string import ascii_lowercase, ascii_uppercase

from core import load_data

codes = ascii_lowercase + ascii_uppercase


def intersection(lines):
    c = set(reduce(lambda a, b: a & set(b), lines[1:], set(lines[0])))
    return codes.index(''.join(c)) + 1


def solution():
    data = load_data("input.txt")

    def reducer(a, b):
        return a + intersection([b[:len(b) // 2], b[len(b) // 2:]])

    data = reduce(reducer, data, 0)

    return data


if __name__ == '__main__':
    print(solution())
