import copy

with open("input.txt") as f:
    PUZZLE_INPUT = f.read()


# PUZZLE_INPUT = """
# The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
# The second floor contains a hydrogen generator.
# The third floor contains a lithium generator.
# The fourth floor contains nothing relevant.
# """


puzzle_input = [x.strip() for x in PUZZLE_INPUT.strip().split("\n")]
print(puzzle_input)

floors = (() for i in range(len(puzzle_input)))

temp = []
for i, line in enumerate(puzzle_input):
    if "nothing" in line:
        temp.append(tuple())
        continue
    line = (
        line[line.index("contains") + 11 :]
        .replace(" and a ", "|")
        .replace(", a ", "|")
        .replace(".", "")
    )
    parts = line.split("|")
    parts = [p.replace("-compatible", "") for p in parts]
    parts = [
        p[0:2].upper() + "G" if "gener" in p else p[0:2].upper() + "M" for p in parts
    ]
    temp.append(tuple(sorted(parts)))
floors = tuple(temp)

# print(floors)


def is_safe(floors):
    for stuff in floors:
        micros = set()
        gens = set()

        for c in stuff:
            if c[~0] == "M":
                micros.add(c[0:-1])
            else:
                gens.add(c[0:-1])

        if gens:
            for m in micros:
                if m not in gens:
                    return False
    return True


assert is_safe(tuple())
assert is_safe((("HM",),))
assert is_safe((("HM", "LM"),))
assert is_safe((("HM", "HG"),))
assert not is_safe((("LM", "HG"),))
assert not is_safe((("HM", "LM", "HG"),))
assert is_safe((("HM", "LM", "HG", "LG"),))
assert not is_safe(
    (("THG", "THM"), ("STG", "STM"), ("PRG", "RUG", "RUM"), ("PLG", "PLM", "PRM"))
)


def find_possible_carry(flrs, num):
    possibles = []
    tried = set()
    for item1 in flrs[num]:
        possibles.append((item1,))
        tried.add(item1)
        for item2 in flrs[num]:
            if item2 not in tried:
                possibles.append((item1, item2))
    return possibles


def stringify(curr, floors):
    result = []
    for i, fl in enumerate(floors):
        if i == curr:
            result.append(f"F{i+1} E {floors[i]}")
        else:
            result.append(f"F{i+1}   {floors[i]}")
    return "\n".join(reversed(result))


def valid_moves(floors, curr, nxt):
    allowed = []
    for p in find_possible_carry(floors, curr):
        next_flr = [x for x in floors[nxt]]
        next_flr.extend(p)
        curr_flr = tuple(x for x in floors[curr] if x not in p)

        if is_safe((curr_flr, tuple(next_flr))):
            allowed.append(p)
    return allowed


# assert valid_moves(floors, 0, 1) == [('HYM',)]
# assert valid_moves(floors, 1, 0) == []
# assert valid_moves(floors, 1, 2) == [("HYG",)]
# assert valid_moves(floors, 2, 1) == [("LIG",)]
# assert valid_moves(floors, 2, 3) == [("LIG",)]


def create_next(current, floors, move, next_floor):
    curr_flr = sorted([x for x in floors[current] if x not in move])
    next_flr = [x for x in floors[next_floor]]
    next_flr.extend(move)
    next_flr = sorted(next_flr)
    floors_new = []
    for i, flr in enumerate(floors):
        if i == current:
            floors_new.append(tuple(curr_flr))
        elif i == next_floor:
            floors_new.append(tuple(next_flr))
        else:
            floors_new.append(flr)
    floors_new = tuple(floors_new)
    return floors_new


def solve(floors):
    queue = [(0, 0, floors, [])]
    seen = {(1, floors)}

    while queue:
        count, current, floors, hist = queue.pop(0)
        hist = copy.deepcopy(hist)
        hist.append(floors)
        if not floors[0] and not floors[1] and not floors[2]:
            # for i, h in enumerate(hist):
            #     print(i, h)
            return count

        count += 1

        if current < 3:
            nxt_up = current + 1
            moves_up = valid_moves(floors, current, nxt_up)
            for move in moves_up:
                floors_new = create_next(current, floors, move, nxt_up)
                if (nxt_up, floors_new) not in seen:
                    seen.add((nxt_up, floors_new))
                    queue.append((count, nxt_up, floors_new, hist))

        if current > 0:
            nxt_down = current - 1
            # If all floors below are empty then don't move down
            if nxt_down == 0 and not floors[0]:
                continue
            if nxt_down == 1 and not floors[0] and not floors[1]:
                continue
            moves_down = valid_moves(floors, current, nxt_down)
            for move in moves_down:
                # Only ever move one item down = massive speed up!
                if len(move) > 1:
                    continue

                floors_new = create_next(current, floors, move, nxt_down)
                if (nxt_down, floors_new) not in seen:
                    seen.add((nxt_down, floors_new))
                    queue.append((count, nxt_down, floors_new, hist))


# Part 1 = 31
print(f"answer = {solve(floors)}")

# Part 2
first_floor = ["DIG", "DIM", "ELG", "ELM"]
first_floor.extend(floors[0])

floors = (tuple(first_floor), floors[1], floors[2], floors[3])

# Part 2 = 55
print(f"answer = {solve(floors)}")
