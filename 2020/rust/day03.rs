use crate::runner;

struct Direction {
    x: usize,
    y: usize,
}

fn parse() -> Vec<String> {
    runner::read_lines("../input/03")
        .unwrap()
        .map(|s| s.unwrap())
        .collect()
}

fn part1(input: &Vec<String>) -> Result<usize, &str> {
    let mut trees = 0;
    for (i, row) in input.iter().enumerate().skip(1) {
        let index = i * 3 % row.chars().count();
        if '#' == row.as_bytes()[index] as char {
            trees += 1;
        }
        println!("{}", row);
    }
    Ok(trees)
}

fn part2(input: &Vec<String>) -> Result<usize, &str> {
    let directions = vec![
        Direction { x: 1, y: 1 },
        Direction { x: 3, y: 1 },
        Direction { x: 5, y: 1 },
        Direction { x: 7, y: 1 },
        Direction { x: 1, y: 2 },
    ];
    let mut result = 1;
    for d in directions {
        let mut trees = 0;
        let mut x = d.x;
        for (i, row) in input.iter().enumerate().skip(1) {
            if i % d.y != 0 {
                continue;
            }
            let length = row.chars().count();
            let index = (i * length + x) % length;
            if '#' == row.as_bytes()[index] as char {
                trees += 1;
            }
            x += d.x;
        }
        println!("{}", trees);
        result *= trees;
    }

    Ok(result)
}

pub fn run() {
    let input = parse();
    runner::result(part1(&input), part2(&input));
}

#[cfg(test)]
mod tests {
    use super::*;

    const INPUT: &str = "..##.........##.........##.........##.........##.........##.......
#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....
.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........#.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...##....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#";

    #[test]
    fn test_part1() {
        let input: Vec<String> = INPUT.split('\n').map(|s| s.into()).collect();
        assert_eq!(7 as usize, part1(&input).unwrap());
    }

    #[test]
    fn test_part2() {
        let input: Vec<String> = INPUT.split('\n').map(|s| s.into()).collect();
        assert_eq!(336 as usize, part2(&input).unwrap());
    }
}
