use crate::runner;
use std::collections::HashMap;

fn parse() -> Vec<String> {
    runner::read_lines("input/15")
        .unwrap()
        .map(|s| s.unwrap())
        .collect()
}

fn compute(input: &Vec<String>, n: usize) -> usize {
    let mut start_numbers: Vec<usize> = input[0]
        .split(',')
        .map(|s| s.parse::<_>().unwrap())
        .collect();
    let mut collection: HashMap<usize, usize> = HashMap::new();
    let mut spoked = 0;
    for (i, x) in start_numbers.iter().enumerate() {
        collection.insert(*x, i + 1);
        spoked = *x;
    }
    for x in start_numbers.len() + 1..=n {
        if let Some(turn) = collection.get(&spoked) {
            let turn = turn.to_owned();
            collection.insert(spoked, x - 1);
            spoked = x - 1 - turn;
        } else {
            collection.insert(spoked, x - 1);
            spoked = 0;
        }
    }
    spoked
}

fn part1(input: &Vec<String>) -> Result<usize, &str> {
    Ok(compute(input, 2020))
}

fn part2(input: &Vec<String>) -> Result<usize, &str> {
    Ok(compute(input, 30000000))
}

pub fn run() {
    let input = parse();
    runner::result(part1(&input), part2(&input));
}
