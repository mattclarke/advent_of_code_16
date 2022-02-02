import hashlib

PUZZLE_INPUT = 3012210

# PUZZLE_INPUT = 5


class Node:
    def __init__(self, number):
        self.number = number
        self.presents = 1
        self.next = None
        self.prev = None


head = Node(1)
prev = head
curr = None

for i in range(1, PUZZLE_INPUT):
    curr = Node(i + 1)
    prev.next = curr
    prev = curr

curr.next = head

curr = head

while curr != curr.next:
    curr.presents += curr.next.presents
    curr.next = curr.next.next
    curr = curr.next


# Part 1 = 1830117
print(f"answer = {curr.number}")

head = Node(1)
prev = head
curr = None

HALF = PUZZLE_INPUT // 2
half = None

for i in range(1, PUZZLE_INPUT):
    curr = Node(i + 1)
    prev.next = curr
    curr.prev = prev
    prev = curr
    if i == HALF:
        half = curr

curr.next = head
head.prev = curr

curr = head
num_elves = PUZZLE_INPUT

while curr != curr.next:
    curr.presents += half.presents
    half.prev.next = half.next
    half.next.prev = half.prev
    curr = curr.next
    if num_elves % 2 == 0:
        half = half.next
    else:
        half = half.next.next

    num_elves -= 1

# Part 2 = 1417887
print(f"answer = {curr.number}")
