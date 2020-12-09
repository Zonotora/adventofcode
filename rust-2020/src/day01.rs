use crate::runner;

fn parse_input() -> Vec<i32> {
    let mut input = Vec::new();
    if let Ok(lines) = runner::read_lines("input/01") {
        for line in lines {
            if let Ok(ip) = line {
                let parsed = ip.parse::<i32>().unwrap();
                input.push(parsed);
            }
        }
    }
    input.sort();
    input
}

fn part1() -> i32 {
    let input = parse_input();
    for x in &input {
        let s = 2020 - x;
        if let Ok(_) = &input.binary_search(&s) {
            return s * x;
        }
    }
    0
}

fn part2() -> i32 {
    let input = parse_input();
    for x in &input {
        for y in &input {
            if x + y > 2020 {
                break;
            }
            let s = 2020 - (x + y);
            if let Ok(_) = &input.binary_search(&s) {
                return s * x * y;
            }
        }
    }
    0
}

pub fn run() {
    let res1 = part1();
    println!("{}", res1);
    let res2 = part2();
    println!("{}", res2);
}
