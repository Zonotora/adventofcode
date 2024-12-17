import re
from itertools import batched

a, b, c, *program = map(int, re.findall(r"[0-9]+", open("../input/17").read()))


def solve(a):
    reg = [a, b, c]

    def combo(operand):
        if 0 <= operand <= 3:
            return operand
        elif operand == 4:
            return reg[0]
        elif operand == 5:
            return reg[1]
        elif operand == 6:
            return reg[2]
        else:
            raise Exception("invalid program")

    instructions = list(batched(program, n=2))
    output = []
    i = 0
    while i < len(instructions):
        opcode, operand = instructions[i]
        combo_operand = combo(operand)
        if opcode == 0:
            reg[0] = reg[0] // (2**combo_operand)
        elif opcode == 1:
            reg[1] = reg[1] ^ operand
        elif opcode == 2:
            reg[1] = combo_operand % 8
        elif opcode == 3:
            if reg[0] != 0:
                i = combo_operand
                continue
        elif opcode == 4:
            reg[1] = reg[1] ^ reg[2]
        elif opcode == 5:
            value = combo_operand % 8
            output.append(value)
        elif opcode == 6:
            reg[1] = reg[0] // (2**combo_operand)
        elif opcode == 7:
            reg[2] = reg[0] // (2**combo_operand)
        i += 1
    return output


def part2():
    valid = [0]
    while True:
        a = valid.pop(0) * 2**3
        for da in range(2**3):
            res = solve(a + da)
            if res == program:
                return a + da
            if res == program[-len(res) :]:
                valid.append(a + da)


part1 = ",".join(map(str, solve(a)))
print(part1)
print(part2())
