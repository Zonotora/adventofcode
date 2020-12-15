use crate::runner;

fn parse() -> Vec<String> {
    runner::read_lines("../input/09")
        .unwrap()
        .map(|s| s.unwrap())
        .collect()
}

fn part1(input: &Vec<String>) -> Result<usize, &str> {
    let threshold = 25;
    let mut numbers: Vec<usize> = Vec::new();
    for x in input {
        let t = x.parse::<usize>().unwrap();
        if numbers.len() > threshold {
            let mut found = false;
            for num in &numbers {
                if let Some(_) = numbers.iter().position(|r| *r + num == t) {
                    found = true;
                    break;
                }
            }
            if !found {
                return Ok(t);
            }
            numbers.remove(0);
        }
        numbers.push(t);
    }
    Ok(0)
}

fn part2(input: &Vec<String>) -> Result<usize, &str> {
    let target = part1(input).unwrap();
    let mut numbers: Vec<usize> = Vec::new();
    for (i, _) in input.iter().enumerate() {
        numbers.clear();
        for y in input.iter().skip(i) {
            let sum = numbers.iter().sum::<usize>();
            if sum == target {
                return Ok(numbers.iter().max().unwrap() + numbers.iter().min().unwrap());
            } else if sum > target {
                numbers.remove(0);
            }
            numbers.push(y.parse().unwrap());
        }
    }
    Ok(0)
}

pub fn run() {
    let input = parse();
    runner::result(part1(&input), part2(&input));
}
