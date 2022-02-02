with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = """
# aba[bab]xyz
# xyx[xyx]xyx
# aaa[kek]eke
# zazbz[bzb]cdb
# """

puzzle_input = [x.strip() for x in PUZZLE_INPUT.strip().split()]
# print(puzzle_input)


valid_count = 0

for line in puzzle_input:
    in_hypernet = False
    valid = False
    for i in range(len(line)):
        next_4 = line[i : i + 4]
        if len(next_4) < 4:
            break
        if "[" in next_4:
            in_hypernet = True
            continue
        if "]" in next_4:
            in_hypernet = False
            continue
        if next_4[0] != next_4[1] and next_4[0] == next_4[3] and next_4[1] == next_4[2]:
            # Is ABBA
            if not in_hypernet:
                valid = True
            else:
                valid = False
                break
    valid_count += 1 if valid else 0


# Part 1 = 115
print(f"answer = {valid_count}")

valid_count = 0

for line in puzzle_input:
    outside = set()
    inside = set()
    in_hypernet = False
    for i in range(len(line)):
        next_3 = line[i : i + 3]
        if len(next_3) < 3:
            break
        if "[" in next_3:
            in_hypernet = True
            continue
        if "]" in next_3:
            in_hypernet = False
            continue
        if next_3[0] != next_3[1] and next_3[0] == next_3[2]:
            if in_hypernet:
                inside.add(next_3[1] + next_3[0] + next_3[1])
            else:
                outside.add(next_3)
    if inside.intersection(outside):
        print(line)
        valid_count += 1

# Part 2 = 231
print(f"answer = {valid_count}")
