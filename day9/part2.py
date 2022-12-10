from core import load_data
from day9.point import Point, move_rope, steps


def solution(data, rope_length):
    rope = [Point((0, 0))] * rope_length
    tail_moves = set()

    for _dir in steps(data):
        rope[0] += _dir
        rope = move_rope(rope)
        tail_moves.add(tuple(rope[-1]))
    return len(tail_moves)


if __name__ == '__main__':
    datastream = load_data("input.txt")
    print(solution(datastream, 10))
