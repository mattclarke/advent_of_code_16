with open("input.txt") as f:
    PUZZLE_INPUT = f.read()


# PUZZLE_INPUT = """
# cpy 41 a
# inc a
# inc a
# dec a
# jnz a 2
# dec a
# """


puzzle_input = [x.strip() for x in PUZZLE_INPUT.strip().split("\n")]
print(puzzle_input)

REG_MAP = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
}


class Cpu:
    def __init__(self):
        self.registers = [0, 0, 0, 0]
        self.sp = 0

    def cpy(self, x, y):
        # x -> y
        if x.isdigit():
            self.registers[REG_MAP[y]] = int(x)
        else:
            self.registers[REG_MAP[y]] = self.registers[REG_MAP[x]]
        self.sp += 1

    def inc(self, x):
        self.registers[REG_MAP[x]] += 1
        self.sp += 1

    def dec(self, x):
        self.registers[REG_MAP[x]] -= 1
        self.sp += 1

    def jnz(self, x, y):
        value = int(x) if x.isdigit() else self.registers[REG_MAP[x]]
        jump = int(y)
        if value == 0:
            self.sp += 1
        else:
            self.sp += jump


def solve(cpu):
    while cpu.sp < len(puzzle_input):
        cmd = puzzle_input[cpu.sp]
        bits = cmd.split(" ")
        if bits[0] == "cpy":
            cpu.cpy(bits[1], bits[2])
        elif bits[0] == "inc":
            cpu.inc(bits[1])
        elif bits[0] == "dec":
            cpu.dec(bits[1])
        elif bits[0] == "jnz":
            cpu.jnz(bits[1], bits[2])


cpu = Cpu()
solve(cpu)

# Part 1 = 318020
print(f"answer = {cpu.registers[0]}")

cpu = Cpu()
cpu.registers[2] = 1
solve(cpu)

# Part 2 = 9227674
print(f"answer = {cpu.registers[0]}")
