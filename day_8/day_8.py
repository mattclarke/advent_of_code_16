
with open("input.txt") as f:
    PUZZLE_INPUT = f.read()
screen = [[False] * 50 for _ in range(6)]

# PUZZLE_INPUT = """
# rect 3x2
# rotate column x=1 by 1
# rotate row y=0 by 4
# rotate column x=1 by 1
# """
# screen = [[False] * 7 for _ in range(3)]


puzzle_input = [x.strip() for x in PUZZLE_INPUT.strip().split("\n")]
print(puzzle_input)

for line in puzzle_input:
    if line.startswith("rect"):
        line = line.replace("rect ", "")
        nums = line.split("x")
        for y in range(int(nums[1])):
            for x in range(int(nums[0])):
                screen[y][x] = not screen[y][x]
    elif line.startswith("rotate column x="):
        line = line.replace("rotate column x=", "")
        nums = line.split(" by ")
        column = int(nums[0])
        pixels = int(nums[1])
        data = []
        for row in screen:
            data.append(row[column])
        data = data[-pixels:] + data[0:-pixels]
        for i, v in enumerate(data):
            screen[i][column] = v
    elif line.startswith("rotate row y="):
        line = line.replace("rotate row y=", "")
        nums = line.split(" by ")
        row = int(nums[0])
        pixels = int(nums[1])
        screen[row] = screen[row][-pixels:] + screen[row][0:-pixels]


count = 0
for row in screen:
    for x in row:
        if x:
            count += 1

# Part 1 = 115
print(f"answer = {count}")

# Part 2 = EFEYKFRFIJ
for row in screen:
    line = []
    for x in row:
        if x:
            line.append("#")
        else:
            line.append(" ")
    print("".join(line))
