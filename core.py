def load_data(f):
    with open(f, "r") as f:
        return list(map(lambda x: x.strip(), f.readlines()))


def load_data_sep(f, sep=''):
    with open(f, "r") as f:
        return list(map(lambda x: x.split('\n'), f.read().split(sep)))


def chunks(data, n=5):
    return [data[i:i + n] for i in range(0, len(data), n)]


def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
