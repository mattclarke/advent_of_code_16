import copy
import itertools

with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

START = "abcdefgh"

# PUZZLE_INPUT = """
# swap position 4 with position 0
# swap letter d with letter b
# reverse positions 0 through 4
# rotate left 1 step
# move position 1 to position 4
# move position 3 to position 0
# rotate based on position of letter b
# rotate based on position of letter d
# """
#
# START = "abcde"

puzzle = [line for line in PUZZLE_INPUT.strip().split("\n")]
print(puzzle)


def swap_pos(data, line):
    # swap position 4 with position 0
    x, y = line.replace("swap position ", "").replace(" with position", "").split(" ")
    data[int(x)], data[int(y)] = data[int(y)], data[int(x)]
    return data


def swap_let(data, line):
    # swap letter d with letter b
    x, y = line.replace("swap letter ", "").replace(" with letter", "").split(" ")
    i = data.index(x)
    j = data.index(y)
    data[i], data[j] = data[j], data[i]
    return data


def rotate_based(data, line):
    # rotate based on position of letter b
    x = line.replace("rotate based on position of letter ", "")
    i = data.index(x)
    i = i if i < 4 else i + 1
    i += 1
    i %= len(data)
    for _ in range(i):
        data = [data[~0]] + data[0:-1]
    return data


def rotate_dir(data, line):
    # rotate left 1 step
    d, x = line.replace("rotate ", "").replace(" step", "").replace("s", "").split(" ")
    i = int(x)
    right = d.startswith("r")

    if right:
        for _ in range(i):
            data = [data[~0]] + data[0:-1]
    else:
        for _ in range(i):
            data = data[1:] + [data[0]]
    return data


def reverse_(data, line):
    # reverse positions 0 through 4
    x, y = line.replace("reverse positions ", "").replace(" through", "").split(" ")
    i = int(x)
    j = int(y)
    temp = data[i : j + 1]
    temp.reverse()
    data = data[0:i] + temp + data[j + 1 :]
    return data


def move(data, line):
    # move position 3 to position 0
    x, y = line.replace("move position ", "").replace(" to position", "").split(" ")
    i = int(x)
    j = int(y)
    temp = data.pop(i)
    data.insert(j, temp)
    return data


def parse(data, line):
    if line.startswith("swap pos"):
        return swap_pos(data, line)
    elif line.startswith("swap let"):
        return swap_let(data, line)
    elif line.startswith("rotate based"):
        return rotate_based(data, line)
    elif line.startswith("rotate"):
        return rotate_dir(data, line)
    elif line.startswith("reverse"):
        return reverse_(data, line)
    elif line.startswith("move"):
        return move(data, line)
    else:
        raise Exception("Oops!")


data = list(START)
for line in puzzle:
    data = parse(data, line)


# Part 1 = bgfacdeh
print(f"answer = {''.join(data)}")

target = list("fbgdceah")

for perm in itertools.permutations(list("abcdefgh")):
    data = list(perm)
    for line in puzzle:
        data = parse(data, line)
    if data == target:
        data = perm
        break


# Part 2 = bdgheacf
print(f"answer = {''.join(data)}")
