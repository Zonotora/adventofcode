import os
import time


class AdventOfCode:
    def __init__(self, year, day, name, preprocess):
        self.year = year
        self.day = day
        self.name = name
        self.parts = {}

        input_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), f"../../input/{self.day}")
        )
        with open(input_path) as f:
            self.input = preprocess(f.read())

    def part(self, part):
        assert part >= 0

        def register(f):
            self.parts[part] = f
            return f

        return register

    def solve(self):

        print(f"Year {self.year} Day {self.day} --- {self.name}\n")
        for key in self.parts:
            start = time.time()
            ans = self.parts[key](self.input[:])
            end = time.time()

            total_time, unit = end - start, 0
            while total_time < 1 and unit <= 3:
                total_time, unit = total_time * 1000, unit + 1

            total_time = (
                "{:.6f}".format(total_time) + ["s", "ms", "us", "ns"][unit]
            )

            print(f"Part {key}: {ans} \n\tfinished in {total_time}")
