import copy
import heapq

with open("input.txt") as f:
    PUZZLE_INPUT = f.read()


# PUZZLE_INPUT = """
# /dev/grid/node-x0-y0   10T    8T     2T   80%
# /dev/grid/node-x0-y1   11T    6T     5T   54%
# /dev/grid/node-x0-y2   32T   28T     4T   87%
# /dev/grid/node-x1-y0    9T    7T     2T   77%
# /dev/grid/node-x1-y1    8T    0T     8T    0%
# /dev/grid/node-x1-y2   11T    7T     4T   63%
# /dev/grid/node-x2-y0   10T    6T     4T   60%
# /dev/grid/node-x2-y1    9T    8T     1T   88%
# /dev/grid/node-x2-y2    9T    6T     3T   66%
# """


puzzle = [line for line in PUZZLE_INPUT.strip().split("\n")]
# print(puzzle)

NODES = {}
MAX_X = 0
MAX_Y = 0

for l in puzzle:
    if not l.startswith("/"):
        continue
    l = (
        l.replace("/dev/grid/node-x", "")
        .replace("-y", " ")
        .replace("T", "")
        .replace("%", "")
    )
    l = (
        l.replace("  ", " ")
        .replace("  ", " ")
        .replace("  ", " ")
        .replace("  ", " ")
        .replace("  ", " ")
    )
    bits = [int(b) for b in l.split(" ")]
    NODES[(bits[0], bits[1])] = bits[2:]
    MAX_X = max(MAX_X, bits[0])
    MAX_Y = max(MAX_Y, bits[1])

can_move = set()  # for part 2
zero = None

# Size  Used  Avail  Use%
count = 0
for n, v in NODES.items():
    if v[1] == 0:
        zero = n
        continue
    used = v[1]
    for n1, v1 in NODES.items():
        if n1 == n:
            continue
        avail = v1[2]
        if used <= avail:
            count += 1
            can_move.add(n)

# Part 1 = 1034
print(f"answer = {count}")

all_nodes = set(NODES.keys())
cannot_move = all_nodes.difference(can_move)
cannot_move.remove(zero)

board = []

for y in range(MAX_Y + 1):
    row = []
    for x in range(MAX_X + 1):
        if (x, y) in cannot_move:
            row.append("#")
        elif (x, y) == zero:
            row.append("_")
        elif (x, y) == (MAX_X, 0):
            row.append("G")
        else:
            row.append(".")
    board.append(row)


def pprint(board):
    for row in board:
        print("".join(row))
    print("")

pprint(board)
queue = [(0, 0, zero, copy.deepcopy(board))]
best = 1000000000000000
seen = set()

while queue:
    _, count, (c, r), board = heapq.heappop(queue)
    if count >= best:
        continue
    if board[0][0] == "G":
        best = min(best, count)
        continue
    if "G" not in board[0]:
        # shortest route requires G to stay in top row
        continue

    # Only care where the "space" and "G" are - the rest of the board is ~static
    as_tuple = ((c,r), board[0].index("G"))
    if as_tuple in seen:
        continue
    seen.add(as_tuple)

    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nr = r + dr
        nc = c + dc
        if nr < 0 or nr > MAX_Y or nc < 0 or nc > MAX_X:
            continue
        if board[nr][nc] == "#":
            continue
        new_board = copy.deepcopy(board)
        new_board[r][c] = new_board[nr][nc]
        new_board[nr][nc] = "_"
        weight = board[0].index("G") + nr
        heapq.heappush(queue, (weight, count + 1, (nc, nr), new_board))


# Part 2 = 261
print(f"answer = {best}")
