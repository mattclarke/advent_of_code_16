with open("input.txt") as f:
    PUZZLE_INPUT = f.read()


# PUZZLE_INPUT = """
# cpy 2 a
# tgl a
# tgl a
# tgl a
# cpy 1 a
# dec a
# dec a
# """

puzzle_input = [x.strip() for x in PUZZLE_INPUT.strip().split("\n")]

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
        try:
            # x -> y
            if x in ["a", "b", "c", "d"]:
                self.registers[REG_MAP[y]] = self.registers[REG_MAP[x]]
            else:
                self.registers[REG_MAP[y]] = int(x)
        except:
            print(f"skipped cpy {x} {y}")
        self.sp += 1

    def inc(self, x):
        self.registers[REG_MAP[x]] += 1
        self.sp += 1

    def dec(self, x):
        self.registers[REG_MAP[x]] -= 1
        self.sp += 1

    def jnz(self, x, y):
        try:
            value = self.registers[REG_MAP[x]] if x in ["a", "b", "c", "d"] else int(x)
            jump = self.registers[REG_MAP[y]] if y in ["a", "b", "c", "d"] else int(y)
            if value == 0:
                self.sp += 1
            else:
                self.sp += jump
        except:
            print(f"skipped jnz {x} {y}")
            self.sp += 1


toggle = {
    "inc": "dec",
    "dec": "inc",
    "tgl": "inc",
    "jnz": "cpy",
    "cpy": "jnz",
}


def solve(cpu, puzzle_input):
    while cpu.sp < len(puzzle_input):
        cmd = puzzle_input[cpu.sp]
        bits = cmd.split(" ")

        # The lines from 4 to 10 are equivalent to a = b * d
        if cpu.sp == 4:
            cpu.registers[REG_MAP["a"]] = (
                cpu.registers[REG_MAP["b"]] * cpu.registers[REG_MAP["d"]]
            )
            cpu.registers[REG_MAP["c"]] = 0
            cpu.registers[REG_MAP["d"]] = 0
            cpu.sp = 10
            continue

        # The lines from 13 to 16 are equivalent to c += d
        if cpu.sp == 13:
            cpu.registers[REG_MAP["c"]] += abs(cpu.registers[REG_MAP["d"]])
            cpu.registers[REG_MAP["d"]] = 0
            cpu.sp = 16
            continue

        # The lines from 21 to 26 (after toggling) are equivalent to a += c * d
        # Note: the tgl command changes "inc d" to "dec d" BEFORE we reach it
        if cpu.sp == 21:
            cpu.registers[REG_MAP["a"]] += abs(cpu.registers[REG_MAP["c"]]) * abs(
                cpu.registers[REG_MAP["d"]]
            )
            cpu.sp = 26
            continue

        if bits[0] == "cpy":
            cpu.cpy(bits[1], bits[2])
        elif bits[0] == "inc":
            cpu.inc(bits[1])
        elif bits[0] == "dec":
            cpu.dec(bits[1])
        elif bits[0] == "jnz":
            cpu.jnz(bits[1], bits[2])
        elif bits[0] == "tgl":
            value = cpu.registers[REG_MAP[bits[1]]]
            if cpu.sp + value < len(puzzle_input):
                old_bits = puzzle_input[cpu.sp + value].split(" ")
                cmd = toggle[old_bits[0]]
                old_bits[0] = cmd
                puzzle_input[cpu.sp + value] = " ".join(old_bits)
            cpu.sp += 1


cpu = Cpu()
cpu.registers[0] = 7
solve(cpu, puzzle_input)

# Part 1 = 11120
print(f"answer = {cpu.registers[REG_MAP['a']]}")

puzzle_input = [x.strip() for x in PUZZLE_INPUT.strip().split("\n")]
cpu = Cpu()
cpu.registers[0] = 12
solve(cpu, puzzle_input)

# Part 2 = 479007680
print(f"answer = {cpu.registers[REG_MAP['a']]}")
