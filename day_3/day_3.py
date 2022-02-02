with open("input.txt") as f:
    PUZZLE_INPUT = f.read()


puzzle_input = [int(x.strip()) for x in PUZZLE_INPUT.strip().split()]
# print(puzzle_input)

count = 0

while puzzle_input:
    triangle = [puzzle_input.pop(0) for x in range(3)]
    triangle.sort()
    if triangle[0] + triangle[1] > triangle[2]:
        count += 1

# Part 1 = 869
print(f"answer = {count}")

puzzle_input = [int(x.strip()) for x in PUZZLE_INPUT.strip().split()]
# print(puzzle_input)

count = 0
index = 0

triangle_1 = []
triangle_2 = []
triangle_3 = []

while puzzle_input:
    for _ in range(3):
        triangle_1.append(puzzle_input.pop(0))
        triangle_2.append(puzzle_input.pop(0))
        triangle_3.append(puzzle_input.pop(0))
    triangle_1.sort()
    if triangle_1[0] + triangle_1[1] > triangle_1[2]:
        count += 1
    triangle_2.sort()
    if triangle_2[0] + triangle_2[1] > triangle_2[2]:
        count += 1
    triangle_3.sort()
    if triangle_3[0] + triangle_3[1] > triangle_3[2]:
        count += 1
    triangle_1.clear()
    triangle_2.clear()
    triangle_3.clear()

# Part 1 = 869
print(f"answer = {count}")
