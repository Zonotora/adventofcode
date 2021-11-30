# flake8: noqa

from python import *

aoc = AdventOfCode("2019", "01", "The Tyranny of the Rocket Equation", newint)


def get_fuel(mass):
    mass = int(mass) // 3 - 2
    if mass < 0:
        return 0
    return mass + get_fuel(mass)


@aoc.part(1)
def part1(items):
    return sum([mass // 3 - 2 for mass in items])


@aoc.part(2)
def part2(items):
    return sum([get_fuel(mass) for mass in items])


if __name__ == "__main__":
    aoc.solve()
