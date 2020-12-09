use crate::runner;

fn parse() -> Vec<usize> {
    let mut input: Vec<usize> = runner::read_lines("input/01")
        .unwrap()
        .enumerate()
        .map(|(_, s)| s.unwrap().parse::<usize>().unwrap())
        .collect();
    input.sort();
    input
}

fn part1(input: &Vec<usize>) -> Result<usize, &str> {
    for x in input {
        let s = 2020 - x;
        match input.binary_search(&s) {
            Ok(_) => return Ok(s * x),
            _ => (),
        }
    }
    Err("Error: no value found!")
}

fn part2(input: &Vec<usize>) -> Result<usize, &str> {
    for (i, x) in input.iter().enumerate() {
        for y in input.iter().skip(i) {
            if x + y > 2020 {
                break;
            }
            let s = 2020 - (x + y);
            match input.binary_search(&s) {
                Ok(_) => return Ok(s * x * y),
                _ => (),
            }
        }
    }
    Err("Error: no value found!")
}

pub fn run() {
    let input = parse();
    runner::result(part1(&input), part2(&input));
}
