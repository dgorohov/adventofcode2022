from core import load_data


def find_next_marker_pos(data, marker_len=4):
    for packet in range(0, len(data), 1):
        if len(set(data[packet:packet + marker_len])) == marker_len:
            yield packet + marker_len


def solution():
    datastream = list(load_data("input.txt")[0])
    # datastream = list("mjqjpqmgbljsphdztnvjfqwrcgsmlb")
    packets = list(find_next_marker_pos(datastream))
    return packets[0]


if __name__ == '__main__':
    print(solution())
