import itertools

with open("input.txt") as f:
    PUZZLE_INPUT = f.read()


# PUZZLE_INPUT = """
# ###########
# #0.1.....2#
# #.#######.#
# #4.......3#
# ###########
# """

puzzle_input = [x.strip() for x in PUZZLE_INPUT.strip().split("\n")]
# print(puzzle_input)

WIDTH = len(puzzle_input[0])
HEIGHT = len(puzzle_input)

MAZE = {}
NUMS = {}


class Node:
    def __init__(self, value, neighbours):
        self.value = value
        self.neighbours = neighbours


for y in range(HEIGHT):
    for x in range(WIDTH):
        if puzzle_input[y][x] != "#":
            neighbours = set()
            for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if puzzle_input[y + dy][x + dx] != "#":
                    neighbours.add((x + dx, y + dy))
            MAZE[(x, y)] = Node(puzzle_input[y][x], neighbours)
            if puzzle_input[y][x].isdigit():
                NUMS[puzzle_input[y][x]] = (x, y)

# print(MAZE)
# print(NUMS)

EDGES = {}

for start in NUMS:
    x, y = NUMS[start]
    temp = {(x, y): 0}
    neighbours = [(n, 1) for n in MAZE[(x, y)].neighbours]

    while neighbours:
        ngh, count = neighbours.pop(0)
        best = temp.get(ngh, 10000000000000)
        temp[ngh] = min(best, count)
        if count >= best:
            continue
        if MAZE[ngh].value.isdigit():
            edge = [start, MAZE[ngh].value]
            edge.sort()
            EDGES[tuple(edge)] = count
            continue
        for n in MAZE[ngh].neighbours:
            neighbours.append((n, count + 1))


# print(sorted(list(EDGES.keys())))

best = 100000000000000000000

for perm in itertools.permutations([str(x + 1) for x in range(len(NUMS) - 1)]):
    current = "0"
    count = 0
    for point in perm:
        temp = tuple(sorted([point, current]))
        count += EDGES[temp]
        current = point
    best = min(count, best)

# Part 1 = 456
print(f"answer = {best}")

best = 100000000000000000000

for perm in itertools.permutations([str(x + 1) for x in range(len(NUMS) - 1)]):
    current = "0"
    perm = list(perm)
    perm.append("0")
    count = 0
    for point in perm:
        temp = tuple(sorted([point, current]))
        count += EDGES[temp]
        current = point
    best = min(count, best)

# Part 2 = 704
print(f"answer = {best}")
