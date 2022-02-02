from collections import Counter

with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# PUZZLE_INPUT = """aaaaa-bbb-z-y-x-123[abxyz]
# a-b-c-d-e-f-g-h-987[abcde]
# not-a-real-room-404[oarel]
# totally-real-room-200[decoy]
# """


def decode(room):
    parts = room.split("-")
    last = parts.pop(len(parts) - 1)
    r_id, checksum = last.replace("]", "").split("[")
    return ("".join(sorted([c for c in "".join(parts)]))), r_id, checksum


puzzle_input = [x.strip() for x in PUZZLE_INPUT.strip().split()]

total = 0
valid_rooms = []

for p in puzzle_input:
    name, r_id, checksum = decode(p)
    counts = Counter(name)
    foo = [(a, counts[a]) for a in sorted(counts.keys())]
    foo.sort(key=lambda x: x[1], reverse=True)
    foo = foo[0:5]
    if all(a == b[0] for a, b in zip(checksum, foo)):
        total += int(r_id)
        valid_rooms.append(p)

# Part 1 = 409147
print(f"answer = {total}")


# valid_rooms = ["qzmt-zixmtkozy-ivhz-343"]
alphabet = "abcdefghijklmnopqrstuvwxyz"

for room in valid_rooms:
    first, *_ = room.split("[")
    name = first[0 : first.rfind("-")]
    r_id = int(first[first.rfind("-") + 1 :])
    ans = []
    for i in name:
        if i == "-":
            ans.append(" ")
        else:
            index = (alphabet.index(i) + r_id % 26) % 26
            ans.append(alphabet[index])
    decrypted_name = "".join(ans)
    # Look for possible matches
    if "north" in decrypted_name:
        print("".join(ans), r_id)

# Part 2 = 991
