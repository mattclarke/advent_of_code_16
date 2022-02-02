import copy

with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

MAX = 4294967295

# PUZZLE_INPUT = """
# 5-8
# 0-2
# 4-7
# """
#
# MAX = 9

puzzle = []
for line in PUZZLE_INPUT.split():
    a, b = line.split("-")
    puzzle.append((int(a), int(b)))
# print(puzzle)

puzzle.sort()

low, high = puzzle.pop(0)
lowest = None
total = 0

for i, v in enumerate(puzzle):
    l, h = v
    if l <= high + 1:
        high = max(h, high)
        continue
    if l > high + 1:
        print(high, l, l - high)
        if lowest is None:
            lowest = high + 1
        total += l - (high + 1)
        high = max(h, high + 1)

if MAX > high:
    total += MAX - high

# Part 1 = 31053880
print(f"answer = {lowest}")

# Part 2 = 117
print(f"answer = {total}")
