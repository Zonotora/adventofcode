const fs = require("fs");

fs.readFile("../input/01", "utf-8", (_: any, s: string) => {
  const input = s.split("\n").map((x: string) => +x);
  const part1 = (z: number) =>
    input
      .map((x) => input.find((y) => x + y + z == 2020))
      .filter((x) => x != undefined && x != 0);
  const part2 = input
    .map((x) => [...part1(x), x])
    .filter((x) => x.length > 2)[0];
  [part1(0), part2].forEach((x: any) => {
    console.log(x.reduce((acc: number, x: number) => acc * x));
  });
});
