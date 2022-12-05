import re
from functools import reduce

from core import load_data_sep, chunks, transpose


def normalize(line):
    line = list(map(lambda a: re.sub(r'\[([A-Z])]', r'\1', a.strip()), line))
    return line


def build_stack(crates):
    crates = list(map(lambda a: normalize(chunks(a, n=4)), crates))
    crates = transpose(crates)
    return reduce(lambda a, b: a + [list(filter(None, b))], crates, [])


def move_items(crates, move_from, move_to, n=1):
    t = crates[move_from - 1][:n]
    del crates[move_from - 1][:n]
    crates[move_to - 1] = t + crates[move_to - 1]
    return crates


def apply_instruction(instr, crates):
    n, _, x, _, y = instr.split(' ')[1:]
    return move_items(crates, int(x), int(y), n=int(n))


def solution():
    crates, inst = load_data_sep("input.txt", sep='\n\n')
    crates = crates[:len(crates) - 1]
    crates = build_stack(crates)
    for instr in inst:
        print(f"Applying {instr}")
        crates = apply_instruction(instr, crates)
    crates = list(filter(None, crates))
    return ''.join(list(map(lambda a: a[0], crates)))


if __name__ == '__main__':
    print(solution())
