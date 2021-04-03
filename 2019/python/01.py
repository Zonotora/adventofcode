part1 = sum([int(mass) // 3 - 2 for mass in  open("../input/01").readlines()])
print(part1)

def get_fuel(mass):
    mass = int(mass) // 3 - 2
    if mass < 0:
        return 0
    return mass + get_fuel(mass)

part2 = sum([get_fuel(mass) for mass in  open("../input/01").readlines()])
print(part2)
