from copy import deepcopy

PUZZLE_INPUT = 1364
TARGET = (31, 39)


# PUZZLE_INPUT = 10
# TARGET = (7, 4)


def is_wall(x, y, favourite):
    base = x * x + 3 * x + 2 * x * y + y + y * y
    base += favourite
    as_bin = "{0:b}".format(base)
    ones = as_bin.count("1")
    return ones % 2 == 1


AREA = []
for y in range(TARGET[1] * 3):
    line = []
    for x in range(TARGET[0] * 3):
        if is_wall(x, y, PUZZLE_INPUT):
            line.append("#")
        else:
            line.append(".")
    AREA.append(line)


dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

position = (1, 1)
area = deepcopy(AREA)
to_try = [(1, (position[0] + x, position[1] + y)) for x, y in dirs]
area[position[0]][position[1]] = 0

while to_try:
    count, position = to_try.pop(0)
    if area[position[1]][position[0]] == "#":
        continue
    if area[position[1]][position[0]] == "." or count < area[position[1]][position[0]]:
        area[position[1]][position[0]] = count
    for cnt, pos in [(count + 1, (position[0] + x, position[1] + y)) for x, y in dirs]:
        # Out of range
        if pos[0] < 0 or pos[0] >= len(area[0]) or pos[1] < 0 or pos[1] >= len(area):
            continue
        # Is a wall
        if area[pos[1]][pos[0]] == "#":
            continue
        if area[pos[1]][pos[0]] == "." or cnt < area[pos[1]][pos[0]]:
            to_try.append((cnt, pos))

    # print("=========")
    # for l in area:
    #     print(l)
    # print("=========")


# Part 1 = 86
print(f"answer = {area[TARGET[1]][TARGET[0]]}")


count = 0

for l in area:
    for x in l:
        if isinstance(x, int):
            if x <= 50:
                count += 1

print(f"answer = {count}")
