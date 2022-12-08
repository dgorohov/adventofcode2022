from core import load_data_as_arr


def is_visible(r, c, data):
    v = data[r][c]
    return any([
        all([(v > data[r][i]) for i in range(0, c)]),
        all([(v > data[r][i]) for i in range(c + 1, len(data[0]))]),
        all([(v > data[j][c]) for j in range(0, r)]),
        all([(v > data[j][c]) for j in range(r + 1, len(data))])
    ])


def count_interior_trees(data):
    count = 0
    for r in range(1, len(data) - 1):
        for c in range(1, len(data[r]) - 1):
            count += 1 if is_visible(r, c, data) else 0
    return count


def count_trees(data):
    edge_trees = (len(data[0]) - 2) * 2 + (len(data) - 2) * 2 + 4
    return edge_trees + count_interior_trees(data)


def solution():
    datastream = load_data_as_arr("input.txt")
    return count_trees(datastream)


if __name__ == '__main__':
    print(solution())
