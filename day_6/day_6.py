with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = """
# eedadn
# drvtee
# eandsr
# raavrd
# atevrs
# tsrnev
# sdttsa
# rasrtv
# nssdts
# ntnada
# svetve
# tesnvt
# vntsnd
# vrdear
# dvrsen
# enarar
# """

puzzle_input = [x.strip() for x in PUZZLE_INPUT.strip().split()]
# print(puzzle_input)

answer_1 = ""
answer_2 = ""

for i in range(len(puzzle_input[0])):
    counter = {}
    for line in puzzle_input:
        counter[line[i]] = counter.get(line[i], 0) + 1
    as_tuples = [(k, v) for k, v in counter.items()]
    as_tuples.sort(key=lambda x: x[1], reverse=True)
    answer_1 += as_tuples[0][0]
    answer_2 += as_tuples[~0][0]

# Part 1 = qoclwvah
print(f"answer = {answer_1}")

# Part 2 = ryrgviuv
print(f"answer = {answer_2}")
