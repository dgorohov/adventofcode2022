import sys

from core import load_data


def build_dirs(parent, ctx, lines):
    line = next(lines, None)
    if line is None:
        return ctx
    print(line)
    if parent not in ctx:
        # ctx[parent] = {}
        ctx[parent] = 0
    match line.split(' '):
        case ['$', 'cd', folder]:
            if folder == '/':
                pass
            elif folder == '..':
                up = parent.split('/')
                up = '/' if len(up) == 2 else '/'.join(up[:len(up) - 1])
                build_dirs(up, ctx, lines)
            else:
                build_dirs(parent + '/' + folder, ctx, lines)
        case ['$', 'ls']:
            pass
        case ['dir', folder]:
            ctx[parent + '/' + folder] = 0
        case [fileSize, fileName]:
            # ctx[parent][fileName] = fileSize
            ctx[parent] += int(fileSize)

    return build_dirs(parent, ctx, lines)


def find_folder_size(ctx):
    keys = ctx.keys()
    sizes = {}
    for key in keys:
        parts = key.split('/')[1:]
        path = '/'
        if len(parts) > 1:
            for part in parts:
                path += '' if part == '' else '/' + part
                if path not in ctx:
                    continue
                if path not in sizes:
                    sizes[path] = 0
                sizes[path] += ctx[key]
        else:
            if path not in sizes:
                sizes[path] = 0
            sizes[path] += ctx[key]

    total_size = 70_000_000
    free_space = sizes['/']

    current_space = total_size - free_space
    required_space = 30_000_000
    smallest_sizes = []

    for key in sizes.keys():
        if current_space + sizes[key] >= required_space:
            smallest_sizes += [sizes[key]]

    return min(smallest_sizes)


def solution():
    datastream = list(load_data("input.txt"))
    ctx = {}
    parent = '/'
    build_dirs(parent, ctx, iter(datastream))
    return find_folder_size(ctx)


if __name__ == '__main__':
    sys.setrecursionlimit(15000)
    print(solution())
