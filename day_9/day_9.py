with open("input.txt") as f:
    PUZZLE_INPUT = f.read()


# PUZZLE_INPUT = """
# ADVENT
# A(1x5)BC
# (3x3)XYZ
# A(2x2)BCD(2x2)EFG
# (6x1)(1x3)A
# X(8x2)(3x3)ABCY
# (27x12)(20x12)(13x14)(7x10)(1x12)A
# (25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN
# """


puzzle_input = [x.strip() for x in PUZZLE_INPUT.strip().split("\n")]
# print(puzzle_input)

for line in puzzle_input:
    result = []
    i = 0
    while i < len(line):
        if line[i] == "(":
            i += 1
            rule = ""
            while line[i] != ")":
                rule += line[i]
                i += 1
            i += 1
            char_count, repeat = [int(x) for x in rule.split("x")]
            to_repeat = ""
            for _ in range(char_count):
                to_repeat += line[i]
                i += 1
            result.append(to_repeat * repeat)
        else:
            result.append(line[i])
            i += 1
    result = "".join(result)
    count = len(result)
    # print(result, count)


# Part 1 = 107035
print(f"answer = {count}")


def solve(line):
    def _solve(chunk, start):
        # print(f"chunk = {chunk}")
        i = start
        count = 0
        debug = ""
        while i < len(chunk):
            if chunk[i] == "(":
                i += 1
                rule = ""
                while chunk[i] != ")":
                    rule += chunk[i]
                    i += 1
                i += 1
                char_count, repeat = [int(x) for x in rule.split("x")]
                to_repeat = ""
                for _ in range(char_count):
                    to_repeat += chunk[i]
                    i += 1
                cnt, patt = _solve(to_repeat, 0)
                count += cnt * repeat
                # UNCOMMENT FOR DEBUGGING
                # debug += patt * repeat
            else:
                # UNCOMMENT FOR DEBUGGING
                # debug += chunk[i]
                count += 1
                i += 1
        # UNCOMMENT FOR DEBUGGING
        # print(f"debug = {debug}")
        return count, debug

    return _solve(line, 0)[0]


result = 0
for line in puzzle_input:
    result = solve(line)

# Part 2 = 11451628995
print(f"answer = {result}")
