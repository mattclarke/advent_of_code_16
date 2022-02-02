import hashlib

PUZZLE_INPUT = "qljzarfv"

# PUZZLE_INPUT = "ihgpwlah"
# PUZZLE_INPUT = "kglvqrro"
# PUZZLE_INPUT = "ulqzkmiv"

TARGET = (3, 3)


def gen_hash(seed):
    return hashlib.md5(f"{seed}".encode()).hexdigest()[0:4]


def is_open(data):
    return data in ["b", "c", "d", "e", "f"]


position = (0, 0)

queue = [((0, 0), PUZZLE_INPUT)]

best = 100000000
best_ans = ""

worst = 0

while queue:
    position, seed = queue.pop(0)
    if position == TARGET:
        if len(seed) < best:
            best = len(seed)
            best_ans = seed
        if len(seed) > worst:
            worst = len(seed)
        continue
    hash = gen_hash(seed)
    for d, c in zip(["U", "D", "L", "R"], hash):
        if is_open(c):
            if d == "U" and position[1] > 0:
                queue.append(((position[0], position[1] - 1), seed + "U"))
            elif d == "D" and position[1] < 3:
                queue.append(((position[0], position[1] + 1), seed + "D"))
            elif d == "L" and position[0] > 0:
                queue.append(((position[0] - 1, position[1]), seed + "L"))
            elif d == "R" and position[0] < 3:
                queue.append(((position[0] + 1, position[1]), seed + "R"))


# Part 1 = DRLRDDURDR
print(f"answer = {best_ans.replace(PUZZLE_INPUT, '')}")

# # Part 2 = 11101110011100110
print(f"answer = {worst - len(PUZZLE_INPUT)}")
