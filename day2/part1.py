from functools import reduce

from core import load_data

# 1st column
# A - rock      X
# B - paper     Y
# C - scissors  Z

eq = {
    "A": "X",
    "B": "Y",
    "C": "Z"
}

guide = {
    "A": "Y",
    "B": "Z",
    "C": "X"
}

score = {
    "X": 1,
    "Y": 2,
    "Z": 3
}


def solution():
    data = load_data("input.txt")

    def reducer(a, b):
        items = b.split(' ')
        if guide[items[0]] == items[1]:
            return a + score[items[1]] + 6
        elif eq[items[0]] == items[1]:
            return a + score[items[1]] + 3
        else:
            return a + score[items[1]] + 0

    data = reduce(reducer, data, 0)

    return data


if __name__ == '__main__':
    print(solution())
