import copy

with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = ".^^.^.^^^^"


puzzle = [PUZZLE_INPUT.strip()]
print(puzzle[0])

def get_next(data):
    result = []
    for i, x in enumerate(data):
        above = [
            data[i-1] == "^" if i > 0 else False,
            x == "^",
            data[i+1] == "^" if i < len(data) - 1 else False,
        ]
        if above[0] and above[1] and not above[2]:
            result.append("^")
        elif not above[0] and above[1] and above[2]:
            result.append("^")
        elif above[0] and not above[1] and not above[2]:
            result.append("^")
        elif not above[0] and not above[1] and above[2]:
            result.append("^")
        else:
            result.append(".")
    return "".join(result)

answer = puzzle[~0].count(".")

for i in range(39):
    ans = get_next(puzzle[~0])
    print(ans)
    puzzle.append(ans)
    answer += puzzle[~0].count(".")


# Part 1 = 1956
print(f"answer = {answer}")

puzzle = PUZZLE_INPUT.strip()

answer = puzzle.count(".")

for i in range(400000 - 1):
    puzzle = get_next(puzzle)
    # print(ans)
    answer += puzzle.count(".")

# Part 2 = 19995121
print(f"answer = {answer}")
