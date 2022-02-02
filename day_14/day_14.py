import hashlib


PUZZLE_INPUT = "ngcjuoqr"
# PUZZLE_INPUT = 'abc'


def solve(additional_hashes):
    index = 0
    count = 0
    cache = {}

    while True:
        if index in cache:
            hash = cache[index]
        else:
            hash = hashlib.md5(f"{PUZZLE_INPUT}{index}".encode()).hexdigest()
            for i in range(additional_hashes):
                hash = hashlib.md5(hash.encode()).hexdigest()

        acc = 0
        ch = None
        found = False
        for c in hash:
            if c == ch:
                acc += 1
            else:
                ch = c
                acc = 1
            if acc == 3:
                found = True
                break

        if found:
            target = ch * 5
            for i in range(1000):
                i_ = index + i + 1
                if i_ in cache:
                    hash2 = cache[i_]
                else:
                    hash2 = hashlib.md5(f"{PUZZLE_INPUT}{i_}".encode()).hexdigest()
                    for i in range(additional_hashes):
                        hash2 = hashlib.md5(hash2.encode()).hexdigest()
                    cache[i_] = hash2
                if target in hash2:
                    count += 1
                    print("found", target, index, i_, count)
                    break
        if count == 64:
            return index
        index += 1


# Part 1 = 18626
print(f"answer = {solve(0)}")

# Part 2 = 20092
print(f"answer = {solve(2016)}")
