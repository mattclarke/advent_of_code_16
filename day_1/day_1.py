with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = """
# R2, L3
# """

puzzle_input = [x.strip() for x in PUZZLE_INPUT.strip().split(",")]
print(puzzle_input)

position = (0, 0)
heading = 0

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for command in puzzle_input:
    direction = command[0]
    step = int(command[1:])
    if direction == "R":
        heading = (heading + 1) % 4
    else:
        heading = (heading - 1) % 4
    position = (
        position[0] + (directions[heading][0] * step),
        position[1] + (directions[heading][1] * step),
    )

# Part 1 = 287
print(f"answer = {abs(position[0]) + abs(position[1])}")

position = (0, 0)
heading = 0

visited = set()

for command in puzzle_input:
    direction = command[0]
    step = int(command[1:])
    if direction == "R":
        heading = (heading + 1) % 4
    else:
        heading = (heading - 1) % 4

    for _ in range(step):
        position = (
            position[0] + directions[heading][0],
            position[1] + directions[heading][1],
        )
        if position in visited:
            break
        visited.add(position)
    else:
        continue
    break

# Part 2 = 133
print(f"answer = {abs(position[0]) + abs(position[1])}")
