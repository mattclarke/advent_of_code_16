import hashlib

PUZZLE_INPUT = "ojvtpuvg"

# PUZZLE_INPUT = "abc"

index = 0
count = 0

code = []

while count < 8:
    hash = hashlib.md5(f"{PUZZLE_INPUT}{index}".encode()).hexdigest()
    if hash.startswith("00000"):
        # print(hash, hash[5], index)
        code.append(hash[5])
        count += 1
    index += 1

# Part 1 = 4543c154
print(f"answer = {''.join(code)}")

code = [None] * 8

while None in code:
    hash = hashlib.md5(f"{PUZZLE_INPUT}{index}".encode()).hexdigest()
    if hash.startswith("00000"):
        if hash[5].isdigit():
            pi = int(hash[5])
            if pi < 8 and code[pi] is None:
                code[pi] = hash[6]
                print(code)

    index += 1

# Part 2 = 1050cbbd
print(f"answer = {''.join(code)}")
