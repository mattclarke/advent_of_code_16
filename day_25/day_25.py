with open("input.txt") as f:
    PUZZLE_INPUT = f.read()


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
        self.last_out = None

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

    def out(self, x):
        new_out = self.registers[REG_MAP[x]]
        if self.last_out is None:
            if new_out != 0:
                raise Exception(f"Nope - incorrect start! {new_out}")
            self.last_out = 0
        elif new_out not in [0, 1]:
            raise Exception(f"Nope - not 0 or 1! {new_out}")
        elif new_out == self.last_out:
            raise Exception(f"Nope - not different to previous {new_out}")
        self.last_out = new_out

        self.sp += 1


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
        elif bits[0] == "out":
            cpu.out(bits[1])


ans = 0

while True:
    print(f"trying {ans}")
    cpu = Cpu()
    cpu.registers[0] = ans
    try:
        solve(cpu)
    except Exception as error:
        print(f"Failed: {error}\n")
    ans += 1


# Part 1 = 196
