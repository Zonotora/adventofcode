use crate::runner;
use itertools::Itertools;
use std::collections::HashSet;

fn parse() -> Vec<String> {
    runner::read_lines("input/08")
        .unwrap()
        .map(|s| s.unwrap())
        .collect()
}

fn compute(pc: usize, acc: usize, input: &Vec<String>, flip: bool) -> Result<usize, &str> {
    let mut pc = pc;
    let mut acc = acc;
    let mut has_flipped = false;
    let mut instr_already_executed: HashSet<usize> = HashSet::new();
    loop {
        if instr_already_executed.contains(&pc) {
            if !flip {
                break;
            } else {
                return Err("Loop");
            }
        }
        if pc >= input.len() {
            return Ok(acc);
        }
        instr_already_executed.insert(pc);
        let (instr, value) = input[pc]
            .split(" ")
            .collect_tuple::<(&str, &str)>()
            .unwrap();
        let op = &value[0..1];
        let instr = if flip && !has_flipped {
            let n = if instr == "nop" {
                "jmp"
            } else if instr == "jmp" {
                "nop"
            } else {
                instr
            };
            has_flipped = true;
            n
        } else {
            instr
        };
        let instr = (instr, op);
        let value = value[1..].parse::<usize>().unwrap();
        match instr {
            ("acc", "+") => acc += value,
            ("acc", "-") => acc -= value,
            ("jmp", "+") => pc += value - 1,
            ("jmp", "-") => pc -= value + 1,
            _ => (),
        }
        pc += 1;
    }
    Ok(acc)
}

fn part1(input: &Vec<String>) -> Result<usize, &str> {
    compute(0, 0, input, false)
}
fn part2(input: &Vec<String>) -> Result<usize, &str> {
    let mut pc = 0;
    let mut acc = 0;
    let mut instr_already_executed: HashSet<usize> = HashSet::new();
    loop {
        if instr_already_executed.contains(&pc) {
            break;
        }
        instr_already_executed.insert(pc);
        let (instr, value) = input[pc]
            .split(" ")
            .collect_tuple::<(&str, &str)>()
            .unwrap();
        let op = &value[0..1];
        let instr = (instr, op);
        let value = value[1..].parse::<usize>().unwrap();
        println!("instr: {:?} pc: {}", instr, pc);
        match instr {
            ("acc", "+") => acc += value,
            ("acc", "-") => acc -= value,
            (t, op) => {
                if let Ok(v) = compute(pc, acc, input, true) {
                    return Ok(v);
                }
                match (t, op) {
                    ("jmp", "+") => pc += value - 1,
                    ("jmp", "-") => pc -= value + 1,
                    _ => (),
                }
            }
            _ => (),
        }
        pc += 1;
    }
    Ok(acc)
}

pub fn run() {
    let input = parse();
    runner::result(part1(&input), part2(&input));
}
