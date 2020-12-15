use crate::runner;
use std::collections::HashSet;

fn parse() -> Vec<String> {
    runner::read("../input/06")
        .unwrap()
        .split("\n\n")
        .map(|s| String::from(s))
        .collect()
}

fn part1(input: &Vec<String>) -> Result<usize, &str> {
    let mut ys = 0;
    for x in input {
        let parts: Vec<&str> = x.split("\n").collect();
        let mut qs: HashSet<String> = HashSet::new();
        for person in parts {
            for q in person.chars() {
                qs.insert(q.to_string());
            }
        }
        ys += qs.len();
    }
    Ok(ys)
}

fn part2(input: &Vec<String>) -> Result<usize, &str> {
    let mut ys = 0;
    for x in input {
        let parts: Vec<&str> = x.split("\n").collect();
        let mut qs: Vec<HashSet<String>> = vec![HashSet::new(); parts.len()];
        for (i, person) in parts.iter().enumerate() {
            for q in person.chars() {
                qs[i].insert(q.to_string());
            }
        }
        ys += qs[0]
            .iter()
            .filter(|k| qs.iter().skip(1).all(|s| s.contains(k.to_owned())))
            .collect::<Vec<_>>()
            .len();
    }
    Ok(ys)
}

pub fn run() {
    let input = parse();
    runner::result(part1(&input), part2(&input));
}
