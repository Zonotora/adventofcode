use crate::runner;

fn parse() -> Vec<usize> {
    let mut res: Vec<usize> = runner::read_lines("../input/10")
        .unwrap()
        .map(|s| s.unwrap().parse().unwrap())
        .collect();
    res.sort();
    res
}

fn compute(length: usize) -> usize {
    match length {
        3 => 2,
        4 => 4,
        5 => 7,
        _ => 1,
    }
}

fn part1(input: &Vec<usize>) -> Result<usize, &str> {
    let mut cnt = (0, 0);
    let mut last = 0;
    for x in input {
        match x - last {
            1 => cnt = (cnt.0 + 1, cnt.1),
            3 => cnt = (cnt.0, cnt.1 + 1),
            _ => (),
        }
        last = x.to_owned();
    }
    Ok(cnt.0 * (cnt.1 + 1))
}

fn part2(input: &Vec<usize>) -> Result<usize, &str> {
    let mut buf: Vec<usize> = vec![0];
    let mut last = 0;
    let mut arr = 1;
    for x in input {
        match x - last {
            3 => {
                arr *= compute(buf.len());
                buf.clear();
            }
            _ => (),
        }
        last = x.to_owned();
        buf.push(last);
    }
    arr *= compute(buf.len());
    Ok(arr)
}

pub fn run() {
    let input = parse();
    runner::result(part1(&input), part2(&input));
}
