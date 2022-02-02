# advent_of_code_16
https://adventofcode.com/2016

## Day 1
- Looping through the commands and tracking current position and direction

## Day 2
- Part 1: looping and tracking
- Part 2: put empty border around keypad to keep boundary checks simple

## Day 3
- Part 1: split into triangles, sort each one then check
- Part 2: same but different way to split them

## Day 4
- Part 1: manipulating the string to get the data required in the correct order
- Part 2: use mod to performs Caesar's cipher

## Day 5
- Part 1: basically the bitcoin algorithm
- Part 2: same but with some extra constraints

## Day 6
- Part 1: count occurrences per column and sort
- Part 2: same but take the lowest count

## Day 7
- Part 1: sliding window and check it string matches puzzle conditions
- Part 2: same but collect parts that match and check for intersection

## Day 8
- Part 1: instruction parsing, column rotate is a bit of a pain but not too tricky (numpy would make it easier?)
- Part 2: print the screen from part 1

## Day 9
- Part 1: looping through the chars adding them until (AxB) then append next A chars B times and continue after A.
- Part 2: count until (AxB) then recurse until "plain" string, only necessary to return the number of chars at each
level, i.e. don't need to build the string.

## Day 10
- Part 1: parse the rules and starting conditions then find the bots with two chips and apply the rules.
- Part 2: trivial as we saved which chips go in which bins (unnecessarily) during part 1

## Day 11
- Part 1: breadth first search, discard any repeats of current floor and floor contents. A bit slow at ~15 seconds with
pypy.
- Part 2: using BFS explodes, so must be some algorithm? Found a speed-up by limiting moves down to one item which gives
a result in ~120 seconds (pypy)
TODO: revisit to see if can be sped up further.

## Day 12:
- Part 1: simple cpu.
- Part 2: same, but different starting conditions.

## Day 13:
- Part 1: walk around the maze until either go out of bounds or cannot improve on shortest route to target.
Nothing clever, just made the maze much bigger than required so can be reasonable certain we get the shortest route.
- Part 2: take the maze from part 1 and count how many locations have a shortest distance of 50 or below.

## Day 14:
- Part 1: bitcoin algorithm, had trouble with regexes so resorted to brute force.
- Part 2: same as part 1 but added caching so it doesn't take forever, still quite slow though (~55 seconds).

## Day 15:
- Part 1: step through until first disc is open, then multiply the step size by the disc size, repeat for the second cog
and so on until all discs are open.
- Part 2: same as part 1 but with extra disc.

## Day 16:
- Part 1: follow the steps of the algorithm, seems unusually simple...
- Part 2: same as part 1 but takes 10 seconds because of the increased length.

## Day 17:
- Part 1: follow the steps of the algorithm and use a queue for valid moves, seems unusually simple...
- Part 2: same as part 1 but track worst path too

## Day 18:
- Part 1: follow the steps of the algorithm and loop, seems unusually simple...
- Part 2: same as part 1 but slower due to the size (~25 seconds).

## Day 19:
- Part 1: use a linked list, so it is quick to remove elves (~5 seconds).
- Part 2: on creation of linked list, assign a pointer to halfway round - this is the item to remove. If the total
number of items is even then advance the pointer by one otherwise by two, and that is the item to delete next turn.

## Day 20:
- Part 1: sort pairs and note the first time there isn't an overlap.
- Part 2: same but keep a running total of the sizes of the non-overlaps.

## Day 21:
- Part 1: parse the input and run the commands on the data.
- Part 2: I didn't think that the "rotate based on position of letter x" could be reversed, so I just ran all the
permutations until we get a match. Turns out I was wrong!

Two internet solutions for part 2 ("rotate based on position of letter x"):
- rotate the input in steps and apply the algorithm until the result matches the initial input.
- each position maps to a unique rotation position so one can do a "reverse look-up", i.e:
```
[0] -> [1]  # shift of 1
[1] -> [3]  # shift of 2
[2] -> [5]  # shift of 3
[3] -> [7]  # shift of 4
[4] -> [2]  # shift of 6
[5] -> [4]  # shift of 7
[6] -> [6]  # shift of 8
[7] -> [0]  # shift of 9
```
E.g. if we want to reverse on 'b' and it is at [5] then we know we need to rotate left 3 times until it is at [2].

## Day 22:
- Part 1: loop and count.
- Part 2: basically a kid's slider puzzle where we want to get a certain piece to a certain position. However, it does
also have pieces that cannot move. E.g.
```
 .  .  G
 .  _  .
 #  .  .
```
Where we want to move `G` to the top-left corner. `_` is the empty square and `#` cannot be moved.

Dijkstra/A* -ish but ignore moves that take G out of the first row as the best answer must be a straight line.

Can also be done by hand pretty quickly if we print the starting board (quicker than coding it up!). Basically it is the
number of steps to get the empty space directly left of the G plus five steps for each movement of G.
```
. . . _ G      . . . G _      . . . G .      . . . G .      . . . G .      . . _ G .
. . . . .  =>  . . . . .  =>  . . . . _  =>  . . . _ .  =>  . . _ . .  =>  . . . . .
. . . . .      . . . . .      . . . . .      . . . . .      . . . . .      . . . . .
```

## Day 23:
- Part 1: add toggle to instruction set and run.
- Part 2: the increased starting value means much much more slow looping, but we can identify chunks of ASM which can be
optimised, for example:
```
cpy b c
inc a
dec c
jnz c -2
dec d
jnz d -5
```
is equivalent to:
```
a = b * d
c = 0
d = 0
```
The `tgl` command initially doesn't do anything because the value of 'c' means it points past the end of the instruction
set. When it does start having an affect it only changes the final optimisation (before we use it, so we can take that
into account beforehand) and the other changes necessary to allow the program to exit.

## Day 24:
- Part 1: building the graph takes some work, but solving the quickest way round the nodes is easy enough using itertools. The
real puzzle is easier than the example because each node can reach every other node and the shortest distance from one
node to another never involves visiting a third node.
- Part 2:  add returning to 0 for all the permutations using in part 1.

## Day 25:
- Part 1:  Add extra instruction to cpu, increment starting "a" register until it hits an infinite loop.
