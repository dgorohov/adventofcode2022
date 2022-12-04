def load_data(f):
    with open(f, "r") as f:
        return list(map(lambda x: x.strip(), f.readlines()))


def chunks(data, n=5):
    return [data[i:i + n] for i in range(0, len(data), n)]
