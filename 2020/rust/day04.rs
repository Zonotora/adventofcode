use crate::runner;
use itertools::Itertools;
use regex::Regex;

fn parse() -> Vec<String> {
    runner::read("input/04")
        .unwrap()
        .split("\n\n")
        .map(|s| String::from(s.split("\n").join(" ")))
        .collect()
}

fn part1(input: &Vec<String>) -> Result<usize, &str> {
    let mut valid = 0;
    for x in input {
        let parts: Vec<Option<(&str, &str)>> = x
            .split(" ")
            .map(|i| i.split(":").collect_tuple::<(&str, &str)>())
            .collect();
        let mut cnt = 0;
        for p in parts {
            match p {
                Some(("cid", _)) => (),
                Some(_) => cnt += 1,
                _ => (),
            }
        }
        if cnt == 7 {
            valid += 1;
        }
    }
    Ok(valid)
}

fn part2<'a>(input: &Vec<String>) -> Result<usize, &str> {
    let mut valid = 0;
    for x in input {
        let parts: Vec<Option<(&str, &str)>> = x
            .split(" ")
            .map(|i| i.split(":").collect_tuple::<(&str, &str)>())
            .collect();
        let mut cnt = 0;
        for p in parts {
            match p {
                Some(("cid", _)) => (),
                Some(("byr", v)) => {
                    let val = v.parse::<usize>().unwrap();
                    if val >= 1920 && val <= 2002 {
                        cnt += 1;
                    }
                }
                Some(("iyr", v)) => {
                    let val = v.parse::<usize>().unwrap();
                    if val >= 2010 && val <= 2020 {
                        cnt += 1;
                    }
                }
                Some(("eyr", v)) => {
                    let val = v.parse::<usize>().unwrap();
                    if val >= 2020 && val <= 2030 {
                        cnt += 1;
                    }
                }
                Some(("hgt", v)) => {
                    if v.ends_with("cm")
                        && (150..=193).contains(&v.trim_end_matches("cm").parse::<usize>().unwrap())
                    {
                        cnt += 1;
                    } else if v.ends_with("in")
                        && (59..=76).contains(&v.trim_end_matches("in").parse::<usize>().unwrap())
                    {
                        cnt += 1;
                    }
                }
                Some(("hcl", v)) => {
                    if Regex::new(r"#[0-9a-f]{6}$").unwrap().is_match(v) {
                        cnt += 1;
                    }
                }
                Some(("ecl", v)) => {
                    if Regex::new(r"(amb|blu|brn|gry|grn|hzl|oth)")
                        .unwrap()
                        .is_match(v)
                    {
                        cnt += 1;
                    }
                }
                Some(("pid", v)) => {
                    if Regex::new(r"^[0-9]{9}$").unwrap().is_match(v) {
                        cnt += 1;
                        println!("{}", v);
                    }
                }
                _ => (),
            }
        }
        if cnt == 7 {
            valid += 1;
        }
    }
    Ok(valid)
}

pub fn run() {
    let input = parse();
    runner::result(part1(&input), part2(&input));
}
