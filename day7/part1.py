import sys

from core import load_data


def build_dirs(parent, ctx, lines):
    line = next(lines, None)
    if line is None:
        return ctx
    if parent not in ctx:
        # ctx[parent] = {}
        ctx[parent] = 0
    match line.split(' '):
        case ['$', 'cd', folder]:
            if folder == '/':
                pass
            elif folder == '..':
                up = list(parent)
                up = ''.join(up[:len(up) - 2])
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


def find_total_size_at_most(ctx, max_size=100000):
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
    print(sizes)
    return sum(map(lambda k: sizes[k], filter(lambda k: sizes[k] <= max_size, sizes.keys())))


def solution():
    datastream = list(load_data("sample2.txt"))
    ctx = {}
    parent = '/'
    build_dirs(parent, ctx, iter(datastream))

    return find_total_size_at_most(ctx)


if __name__ == '__main__':
    sys.setrecursionlimit(15000)
    print(solution())
