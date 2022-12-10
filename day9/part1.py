from core import load_data

head_moves = [(0, 0)]
tail_moves = [(0, 0)]


def move_tail():
    global tail_moves, head_moves
    head_last_x, head_last_y = head_moves[len(head_moves) - 1]
    tail_last_x, tail_last_y = tail_moves[len(tail_moves) - 1]

    if abs(head_last_x - tail_last_x) > 1 or abs(head_last_y - tail_last_y) > 1:
        if abs(head_last_x - tail_last_x) <= 1:
            # up or down
            if head_last_y > tail_last_y:
                tail_moves += [(head_last_x, y) for y in range(tail_last_y + 1, head_last_y)]  # up
            else:
                tail_moves += [(head_last_x, y) for y in range(tail_last_y - 1, head_last_y, -1)]  # down
        else:
            # left or right
            if head_last_x > tail_last_x:
                tail_moves += [(x, head_last_y) for x in range(tail_last_x + 1, head_last_x)]  # right
            else:
                tail_moves += [(x, head_last_y) for x in range(tail_last_x - 1, head_last_x, -1)]  # left
    return 0


def record_head_move(move):
    global head_moves
    head_last_x, head_last_y = head_moves[len(head_moves) - 1]
    match move.split(' '):
        case['R', right]:
            head_last_x += int(right)
        case['L', left]:
            head_last_x -= int(left)
        case['U', up]:
            head_last_y += int(up)
        case['D', down]:
            head_last_y -= int(down)

    head_moves += [(head_last_x, head_last_y)]


def solution():
    datastream = load_data("input.txt")
    for line in datastream:
        record_head_move(line)
        move_tail()
    return len(set(tail_moves))


if __name__ == '__main__':
    print(solution())
