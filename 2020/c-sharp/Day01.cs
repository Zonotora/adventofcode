using System;
using System.Collections.Generic;
using System.Linq;


namespace AOC2020
{
    public class Day01 {
        public static void Run(string input) {
            int[] lines = input.Split("\n").Select(x => int.Parse(x)).ToArray();
            Array.Sort(lines);

            void Part1() {
                foreach (var line in lines) {
                    var index = Array.BinarySearch(lines, 2020 - line);
                    if (index > 0) {
                        var part1 = lines[index] * line;
                        Console.WriteLine(part1);
                        return;
                    }
                }
            };
            void Part2() {
                for(int i = 0; i < lines.Length; i++) {
                    for(int j = i+1; j < lines.Length; j++) {
                        var index = Array.BinarySearch(lines, 2020 - lines[i] - lines[j]);
                        if (index > 0) {
                            var part2 = lines[index] * lines[i] * lines[j];
                            Console.WriteLine(part2);
                            return;
                        }
                    }
                }
            };
            Part1();
            Part2();
        }
    }
}

