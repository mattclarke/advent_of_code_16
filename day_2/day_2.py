with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = """
# ULL
# RRDDD
# LURDL
# UUUUD
# """

puzzle_input = [x.strip() for x in PUZZLE_INPUT.strip().split()]
print(puzzle_input)

buttons = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

current_position = (1, 1)
code = []

for line in puzzle_input:
    for c in line:
        if c == "L" and current_position[0] > 0:
            current_position = current_position[0] - 1, current_position[1]
        elif c == "R" and current_position[0] < 2:
            current_position = current_position[0] + 1, current_position[1]
        elif c == "U" and current_position[1] > 0:
            current_position = current_position[0], current_position[1] - 1
        elif c == "D" and current_position[1] < 2:
            current_position = current_position[0], current_position[1] + 1
    code.append(buttons[current_position[1]][current_position[0]])

# Part 1 = 56983
print(f"answer = {code}")

buttons = [
    ["", "", "", "", "", "", ""],
    ["", "", "", "1", "", "", ""],
    ["", "", "2", "3", "4", "", ""],
    ["", "5", "6", "7", "8", "9", ""],
    ["", "", "A", "B", "C", "", ""],
    ["", "", "", "D", "", "", ""],
    ["", "", "", "", "", "", ""],
]

# Start from 5
current_position = (1, 3)
code = []

for line in puzzle_input:
    for c in line:
        if c == "L":
            if buttons[current_position[0] - 1][current_position[1]] != "":
                current_position = current_position[0] - 1, current_position[1]
        elif c == "R":
            if buttons[current_position[0] + 1][current_position[1]] != "":
                current_position = current_position[0] + 1, current_position[1]
        elif c == "U":
            if buttons[current_position[0]][current_position[1] - 1] != "":
                current_position = current_position[0], current_position[1] - 1
        elif c == "D":
            if buttons[current_position[0]][current_position[1] + 1] != "":
                current_position = current_position[0], current_position[1] + 1
    code.append(buttons[current_position[1]][current_position[0]])

# Part 2 = 8B8B1
print(f"answer = {''.join(code)}")
