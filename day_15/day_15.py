import copy

with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

puzzle_input = [x.strip() for x in PUZZLE_INPUT.strip().split("\n")]
print(puzzle_input)

DISCS = []

for l in puzzle_input:
    l = (
        l.replace("Disc #", "")
        .replace("has ", "")
        .replace("positions; at time=0, it is at position ", "")
        .replace(".", "")
    )
    num, pos, curr = l.split(" ")
    DISCS.append([int(pos), int(curr)])


def solve(discs):
    discs = copy.deepcopy(discs)
    # Advance "current" position based on how far down the stack they are.
    # E.g. disc four will have moved by four positions by the time the capsule reaches it
    for i, d in enumerate(discs):
        discs[i][1] = (discs[i][1] + i) % discs[i][0]

    step = 1
    ticks = 0
    pointer = 1

    while True:
        for i, d in enumerate(discs):
            d[1] = (d[1] + step) % d[0]
        # Only need to check that the current disc is open as the previous ones
        # will be
        if discs[pointer - 1][1] == 0:
            if pointer >= len(discs):
                return ticks
            step *= discs[pointer - 1][0]
            pointer += 1
        ticks += step


# Part 1 = 317371
print(f"answer = {solve(DISCS)}")

# Part 2 = 2080951
DISCS.append([11, 0])
print(f"answer = {solve(DISCS)}")
