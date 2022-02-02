import copy

PUZZLE_INPUT = "01111010110010011"
LENGTH = 272

# PUZZLE_INPUT = "10000"
# LENGTH = 20


def dragon(data):
    a = data
    b = a[::-1]
    b = b.replace("1", "2").replace("0", "1").replace("2", "0")
    return a + "0" + b


def checksum(data):
    i = 0
    result = []
    while i < len(data):
        d = data[i : i + 2]
        if d == "00" or d == "11":
            result.append("1")
        else:
            result.append("0")
        i += 2
    return "".join(result)


def solve(data, length):
    result = data
    while len(result) < length:
        result = dragon(result)

    result = result[0:length]

    while len(result) % 2 == 0:
        result = checksum(result)
    return result


# Part 1 = 00100111000101111
print(f"answer = {solve(PUZZLE_INPUT, LENGTH)}")


# Part 2 = 11101110011100110
print(f"answer = {solve(PUZZLE_INPUT, 35651584)}")
