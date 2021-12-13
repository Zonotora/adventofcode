use crate::runner;

fn parse() -> Vec<String> {
    runner::read_lines("input/25")
        .unwrap()
        .map(|s| s.unwrap())
        .collect()
}

fn part1(input: &Vec<String>) -> Result<usize, &str> {
    let card = input[0].parse::<usize>().unwrap();
    let door = input[1].parse::<usize>().unwrap();
    let mut subject_number = 0;
    let mut loop_size = 0;
    let mut value = 7;
    loop {
        value *= 7;
        value %= 20201227;
        loop_size += 1;
        if value == door {
            subject_number = card;
            break;
        } else if value == card {
            subject_number = door;
            break;
        }
    }
    let mut encryption_key = subject_number;
    for x in 0..loop_size {
        encryption_key *= subject_number;
        encryption_key %= 20201227;
    }
    Ok(encryption_key)
}

fn part2(input: &Vec<String>) -> Result<usize, &str> {
    Ok(0)
}

pub fn run() {
    let input = parse();
    runner::result(part1(&input), part2(&input));
}
