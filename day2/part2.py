from functools import reduce

from core import load_data

# 1st column
# A - rock      X
# B - paper     Y
# C - scissors  Z

score = {
    "X": 0, # lose
    "Y": 3, # draw
    "Z": 6  # win
}

eq = {
    "A": ["Z", "X", "Y"],
    "B": ["X", "Y", "Z"],
    "C": ["Y", "Z", "X"]
}

value = {
    "X": 0,
    "Y": 1,
    "Z": 2
}


def solution():
    data = load_data("input.txt")

    def reducer(a, b):
        items = b.split(' ')
        return a + score[items[1]] + value[eq[items[0]][value[items[1]]]] + 1

    data = reduce(reducer, data, 0)

    return data


if __name__ == '__main__':
    print(solution())
