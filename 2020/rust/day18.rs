use crate::runner;

fn parse() -> Vec<String> {
    runner::read_lines("input/18")
        .unwrap()
        .map(|s| s.unwrap())
        .collect()
}

fn eval1(op: char, acc: usize, value: usize) -> usize {
    if op == '+' {
        acc + value
    } else {
        acc * value
    }
}

fn compute1<I: Iterator<Item = char>>(input: &mut I) -> usize {
    let mut acc = 0;
    let mut op = '+';
    while let Some(c) = input.next() {
        match c {
            '+' | '*' => op = c,
            '(' => acc = eval1(op, acc, compute1(input)),
            ')' => break,
            ' ' => (),
            num => acc = eval1(op, acc, num.to_string().parse::<usize>().unwrap()),
        }
    }
    acc
}

fn eval2(vals: &mut Vec<usize>, ops: &mut Vec<char>) -> usize {
    while let Some(op) = ops.pop() {
        let operand1 = vals.pop().unwrap();
        let operand2 = vals.pop().unwrap();
        if let Some(next_op) = ops.pop() {
            if (op == next_op) {
                vals.push(eval1(op, operand1, operand2));
            } else {
                if op == '*' {
                    vals.insert(0, operand1);
                    vals.push(operand2);
                    ops.insert(0, op);
                } else {
                    vals.push(eval1(op, operand1, operand2));
                }
            }
            ops.push(next_op);
        } else {
            vals.push(eval1(op, operand1, operand2));
        }
    }
    vals[0]
}

fn compute2<I: Iterator<Item = char>>(input: &mut I) -> usize {
    let mut vals: Vec<usize> = Vec::new();
    let mut ops: Vec<char> = Vec::new();
    while let Some(c) = input.next() {
        match c {
            '+' | '*' => ops.push(c),
            '(' => vals.push(compute2(input)),
            ')' => break,
            ' ' => (),
            num => vals.push(num.to_string().parse::<usize>().unwrap()),
        }
    }
    eval2(&mut vals, &mut ops)
}

fn part1(input: &Vec<String>) -> Result<usize, &str> {
    let mut acc = 0;
    for x in input {
        acc += compute1(&mut x.chars());
    }
    Ok(acc)
}

fn part2(input: &Vec<String>) -> Result<usize, &str> {
    let mut acc = 0;
    for x in input {
        acc += compute2(&mut x.chars());
    }
    Ok(acc)
}

pub fn run() {
    let input = parse();
    runner::result(part1(&input), part2(&input));
}
