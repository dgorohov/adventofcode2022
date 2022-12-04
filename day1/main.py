from functools import reduce

from core import load_data


def solution():
    data = list(map(lambda a: 0 if a == '' else int(a), load_data("input.txt")))

    def reducer(a, b):
        if b == 0:
            a.append(0)
        a[-1:] = [sum(a[-1:] + [b])]
        return a

    data = list(reduce(reducer, data, []))
    data.sort(reverse=True)

    return data[0], sum(data[0:3])


if __name__ == '__main__':
    print(solution())
