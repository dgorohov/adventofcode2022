from functools import reduce


def take_until(predicate, data):
    it = range(len(data))
    for index in it:
        yield data[index]
        if not predicate(data[index]):
            break


def load_data(f):
    with open(f, "r") as f:
        return list(map(lambda x: x.strip(), f.readlines()))


def load_data_as_arr(f):
    def reducer(out, inp):
        return out + [list(inp.strip())]

    with open(f, "r") as f:
        return reduce(reducer, f.readlines(), [])


def load_data_sep(f, sep=''):
    with open(f, "r") as f:
        return list(map(lambda x: x.split('\n'), f.read().split(sep)))


def chunks(data, n=5):
    return [data[i:i + n] for i in range(0, len(data), n)]


def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
