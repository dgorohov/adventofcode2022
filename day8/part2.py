import math

from core import load_data_as_arr, take_until


def get_until(current, values):
    return list(take_until(lambda a: int(a) < int(current), values))


def tree_scenic_score(r, c, data):
    v = data[r][c]
    return math.prod([
        len(get_until(v, [data[r][a] for a in reversed(range(0, c))])),  # V -> left
        len(get_until(v, [data[r][a] for a in range(c + 1, len(data[r]))])),  # V -> right
        len(get_until(v, [data[a][c] for a in reversed(range(0, r))])),  # V -> top
        len(get_until(v, [data[a][c] for a in range(r + 1, len(data))]))  # V -> bottom
    ])


def find_max_score(data):
    return max([tree_scenic_score(r, c, data) for r in range(0, len(data)) for c in range(0, len(data[r]))])


def solution():
    datastream = load_data_as_arr("input.txt")
    return find_max_score(datastream)


if __name__ == '__main__':
    print(solution())
