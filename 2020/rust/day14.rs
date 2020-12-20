use crate::runner;
use itertools::Itertools;
use std::collections::HashMap;

fn parse() -> Vec<String> {
    runner::read_lines("input/14")
        .unwrap()
        .map(|s| s.unwrap())
        .collect()
}

fn part1(input: &Vec<String>) -> Result<isize, &str> {
    let mut mask = "";
    let mut mem: HashMap<usize, isize> = HashMap::new();
    for x in input {
        if x.starts_with("mask") {
            mask = &x[7..];
        } else {
            let adr = x[4..]
                .chars()
                .take_while(|c| *c != ']')
                .map(|c| c.to_string())
                .collect::<Vec<String>>()
                .join("")
                .parse::<usize>()
                .unwrap();
            let value = format!(
                "{:036b}",
                x[x.find('=').unwrap() + 2..].parse::<i32>().unwrap()
            );
            let mut mask_it = mask.chars();
            let mut value_it = value.chars();
            let mut res = String::new();
            while let Some(bit) = mask_it.next() {
                let value_bit = value_it.next().unwrap();
                match bit {
                    '0' => res.push('0'),
                    '1' => res.push('1'),
                    'X' => res.push(value_bit),
                    _ => (),
                }
            }
            let res = isize::from_str_radix(&res[..], 2).unwrap();
            mem.insert(adr, res);
        }
    }
    let mut acc = 0;
    for (_, v) in mem {
        acc += v;
    }
    Ok(acc)
}

fn part2(input: &Vec<String>) -> Result<isize, &str> {
    let mut mask = "";
    let mut mem: HashMap<usize, isize> = HashMap::new();
    for x in input {
        if x.starts_with("mask") {
            mask = &x[7..];
        } else {
            let adr = format!(
                "{:036b}",
                x[4..]
                    .chars()
                    .take_while(|c| *c != ']')
                    .map(|c| c.to_string())
                    .collect::<Vec<String>>()
                    .join("")
                    .parse::<usize>()
                    .unwrap()
            );
            let value = x[x.find('=').unwrap() + 2..].parse::<isize>().unwrap();
            let mut mask_it = mask.chars();
            let mut adr_it = adr.chars();
            let mut res = String::new();
            let mut floating: Vec<usize> = Vec::new();
            let mut i = 0;
            while let Some(bit) = mask_it.next() {
                let adr_bit = adr_it.next().unwrap();
                match bit {
                    '0' => res.push(adr_bit),
                    '1' => res.push('1'),
                    'X' => {
                        res.push('X');
                        floating.push(i);
                    }
                    _ => (),
                }
                i += 1;
            }
            let mut combinations: Vec<Vec<&usize>> = Vec::new();
            for i in 0..=floating.len() {
                let mut t = floating
                    .iter()
                    .combinations(i)
                    .collect::<Vec<Vec<&usize>>>();
                combinations.append(&mut t);
            }

            for c in &combinations {
                let mut adr_it = res.chars();
                let mut i = 0;
                let mut new_adr = String::new();
                while let Some(bit) = adr_it.next() {
                    if bit == 'X' {
                        if let Some(_) = c.iter().position(|e| **e == i) {
                            new_adr.push('1');
                        } else {
                            new_adr.push('0');
                        }
                    } else {
                        new_adr.push(bit);
                    }

                    i += 1;
                }
                let new_adr = usize::from_str_radix(&new_adr[..], 2).unwrap();
                mem.insert(new_adr, value);
            }
        }
    }
    let mut acc = 0;
    for (_, v) in mem {
        acc += v;
    }
    Ok(acc)
}

pub fn run() {
    let input = parse();
    runner::result(part1(&input), part2(&input));
}
