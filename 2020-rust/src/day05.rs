use crate::runner;
use std::cmp;

fn parse() -> Vec<String> {
    runner::read_lines("input/05")
        .unwrap()
        .map(|s| s.unwrap())
        .collect()
}

fn part1(input: &Vec<String>) -> Result<usize, &str> {
    let mut max = 0;
    for x in input {
        let chars: Vec<char> = x.chars().collect();
        let mut rl: f32 = 127.0;
        let mut ri = 0;
        let mut cl: f32 = 8.0;
        let mut ci = 0;
        for c in chars {
            rl = (rl / 2.0).ceil();
            match c {
                'B' => ri += rl as usize,
                'R' => {
                    cl = (cl / 2.0).ceil();
                    ci += cl as usize
                }
                'L' => cl = (cl / 2.0).ceil(),
                _ => (),
            }
        }
        max = cmp::max(max, ri * 8 + ci);
    }
    Ok(max)
}

fn part2(input: &Vec<String>) -> Result<usize, &str> {
    let mut ids = Vec::new();
    for x in input {
        let chars: Vec<char> = x.chars().collect();
        let mut rl: f32 = 127.0;
        let mut ri = 0;
        let mut cl: f32 = 8.0;
        let mut ci = 0;
        for c in chars {
            rl = (rl / 2.0).ceil();
            match c {
                'B' => ri += rl as usize,
                'R' => {
                    cl = (cl / 2.0).ceil();
                    ci += cl as usize
                }
                'L' => cl = (cl / 2.0).ceil(),
                _ => (),
            }
        }
        ids.push(ri * 8 + ci);
    }
    ids.sort();
    let mut last = 11;
    for x in ids.iter().skip(1) {
        if last != x - 1 {
            return Ok(x - 1);
        }
        last = *x;
    }
    Ok(0)
}

pub fn run() {
    let input = parse();
    runner::result(part1(&input), part2(&input));
}
