use crate::runner;

fn parse() -> Vec<String> {
    runner::read_lines("input/13")
        .unwrap()
        .map(|s| s.unwrap())
        .collect()
}

fn part1(input: &Vec<String>) -> Result<i128, &str> {
    let time = &input[0].parse::<usize>().unwrap();
    let departures: Vec<usize> = input[1]
        .split(',')
        .filter(|s| *s != "x")
        .map(|s| s.parse::<usize>().unwrap())
        .collect();
    let mut min = (0, usize::MAX);
    for x in departures {
        let v = time % x;
        let c = x - v;
        if min.1 > c {
            min = (x, c);
        }
    }
    Ok((min.0 * min.1) as i128)
}

fn egcd(a: i128, b: i128) -> (i128, i128) {
    if b == 0 {
        return (1, 0);
    }

    let (x, y) = egcd(b, a % b);
    let k = a / b;
    (y, x - k * y)
}

fn invert_mod(a: i128, n: i128) -> i128 {
    let (mut b, x) = egcd(a, n);
    if b < 0 {
        b = (b % n + n) % n
    }
    b
}

fn part2(input: &Vec<String>) -> Result<i128, &str> {
    let time = &input[0].parse::<usize>().unwrap();
    let departures: Vec<(i128, i128)> = input[1]
        .split(',')
        .enumerate()
        .filter(|(i, s)| *s != "x")
        .map(|(i, s)| {
            let v = s.parse::<i128>().unwrap();
            (v - i as i128, v)
        })
        .collect();
    let N: i128 = departures.iter().map(|(_, a)| *a as i128).product();
    let mut x = 0;
    for (a, n) in &departures {
        let d = (N / n);
        let b = invert_mod(d, *n);
        x += a * d * b;
    }
    Ok(x % N)
}

pub fn run() {
    let input = parse();
    runner::result(part1(&input), part2(&input));
}
