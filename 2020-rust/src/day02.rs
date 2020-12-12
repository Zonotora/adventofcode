use crate::runner;

fn parse() -> Vec<String> {
    runner::read_lines("input/02")
        .unwrap()
        .map(|s| s.unwrap())
        .collect()
}

fn part1(input: &Vec<String>) -> Result<usize, &str> {
    let mut valid = 0;
    for x in input {
        let index = x.find('-').unwrap();
        let min = x[0..index].parse::<usize>().unwrap();
        let max = x[index + 1..index + 3].trim().parse::<usize>().unwrap();
        let index = x.find(':').unwrap();
        let c_valid = x.as_bytes()[index - 1] as char;
        let mut cnt = 0;
        for c in x.chars().skip(index) {
            match c {
                ch => {
                    if ch == c_valid {
                        cnt += 1
                    }
                }
                _ => (),
            }
        }
        if cnt >= min && cnt <= max {
            valid += 1;
        }
    }
    Ok(valid)
}

fn part2(input: &Vec<String>) -> Result<usize, &str> {
    let mut valid = 0;
    for x in input {
        let index = x.find('-').unwrap();
        let min = x[0..index].parse::<usize>().unwrap();
        let max = x[index + 1..index + 3].trim().parse::<usize>().unwrap();
        let index = x.find(':').unwrap() + 1;
        let bytes = x.as_bytes();
        let min_valid = index + min < x.len() && bytes[index + min] == bytes[index - 2];
        let max_valid = index + max < x.len() && bytes[index + max] == bytes[index - 2];
        if min_valid && !max_valid || !min_valid && max_valid {
            valid += 1;
        }
    }
    Ok(valid)
}

pub fn run() {
    let input = parse();
    runner::result(part1(&input), part2(&input));
}
