import copy

with open("input.txt") as f:
    PUZZLE_INPUT = f.read()


# PUZZLE_INPUT = """
# value 5 goes to bot 2
# bot 2 gives low to bot 1 and high to bot 0
# value 3 goes to bot 1
# bot 1 gives low to output 1 and high to bot 0
# bot 0 gives low to output 2 and high to output 0
# value 2 goes to bot 2
# """


puzzle_input = [x.strip() for x in PUZZLE_INPUT.strip().split("\n")]
# print(puzzle_input)

rules = {}
bots = {}
bins = {}

for line in puzzle_input:
    if line.startswith("value"):
        line = line.replace("value ", "").replace(" goes to bot ", " b")
        value, bot = line.split(" ")
        holds = bots.get(str(bot), set())
        holds.add(int(value))
        bots[str(bot)] = holds
    elif "output" in line:
        line = line.replace(" gives low to ", " ").replace(" and high to ", " ")
        line = line.replace("bot ", "b").replace("output ", "o")
        bot, low, high = line.split(" ")
        rules[bot] = (low, high)
    elif line.startswith("bot"):
        line = (
            line.replace("bot ", "b")
            .replace(" gives low to ", " ")
            .replace(" and high to ", " ")
        )
        bot, low, high = line.split(" ")
        rules[bot] = (low, high)
    else:
        raise RuntimeError("Oops!")
# print(bots)
# print(rules)

finished = False

next_bot = []

# find start
for bn, bv in bots.items():
    if len(bv) == 2:
        next_bot.append(bn)

while next_bot:
    curr_bot = next_bot.pop(0)
    assert len(bots[curr_bot]) == 2
    low, high = sorted(bots[curr_bot])
    rule = rules[curr_bot]
    dest1, dest2 = rule
    if (low, high) == (17, 61):
        # Part 1 = 157
        print(f"answer = {curr_bot}")

    if dest1.startswith("o"):
        bin = bins.get(dest1, [])
        bin.append(low)
        bins[dest1] = bin
        bots[curr_bot].remove(low)
    else:
        bot = bots.get(dest1, set())
        bot.add(low)
        bots[dest1] = bot
        bots[curr_bot].remove(low)
        if len(bots[dest1]) == 2:
            next_bot.append(dest1)

    if dest2.startswith("o"):
        bin = bins.get(dest2, [])
        bin.append(high)
        bins[dest2] = bin
        bots[curr_bot].remove(high)
    else:
        bot = bots.get(dest2, set())
        bot.add(high)
        bots[dest2] = bot
        bots[curr_bot].remove(high)
        if len(bots[dest2]) == 2:
            next_bot.append(dest2)

answer = bins["o0"][0] * bins["o1"][0] * bins["o2"][0]

# Part 2 = 1085
print(f"answer = {answer}")
