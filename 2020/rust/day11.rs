use crate::runner;

fn parse() -> Vec<String> {
    runner::read_lines("input/11")
        .unwrap()
        .map(|s| s.unwrap())
        .collect()
}

fn get_neighbour_count(i: usize, j: usize, input: &Vec<String>) -> (usize, usize, usize) {
    // floor empty occupied
    let mut cnt = (0, 0, 0);
    for y in -1..2 {
        for x in -1..2 {
            if x == 0 && y == 0 {
                continue;
            }
            let y = y + i as i32;
            let x = x + j as i32;
            if y < 0 || y as usize > input.len() - 1 {
                continue;
            }
            let line = &input[y as usize..y as usize + 1].get(0).unwrap();
            if x < 0 || x as usize >= line.chars().count() {
                continue;
            }
            let c = line.chars().nth(x as usize).unwrap();
            let (floor, empty, occupied) = cnt;
            match c {
                '.' => cnt = (floor + 1, empty, occupied),
                'L' => cnt = (floor, empty + 1, occupied),
                '#' => cnt = (floor, empty, occupied + 1),
                _ => (),
            }
        }
    }

    cnt
}

fn check(i1: &Vec<String>, i2: &Vec<String>) -> (bool, usize) {
    let mut cnt = 0;
    for (i, (a, b)) in i1.iter().zip(i2.iter()).enumerate() {
        for j in 0..a.chars().count() {
            let c1 = a.chars().nth(j).unwrap();
            let c2 = b.chars().nth(j).unwrap();
            if c1 != c2 {
                return (false, 0);
            } else if c1 == '#' {
                cnt += 1;
            }
        }
    }

    (true, cnt)
}

fn get_visible_seats(i: isize, j: isize, input: &Vec<String>) -> usize {
    let mut cnt = 0;
    for (x, y) in vec![
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ] {
        let mut ix = x;
        let mut iy = y;
        while i + iy >= 0
            && i + iy < input.len() as isize
            && j + ix >= 0
            && j + ix < input[(i + iy) as usize].len() as isize
        {
            let c = input[(i + iy) as usize]
                .chars()
                .nth((ix + j) as usize)
                .unwrap();
            match c {
                'L' => break,
                '#' => {
                    cnt += 1;
                    break;
                }
                _ => (),
            }

            ix += x;
            iy += y;
        }
    }
    cnt
}

fn part1(input: &Vec<String>) -> Result<usize, &str> {
    let mut input = input.clone();
    let mut new_input: Vec<String> = Vec::new();

    loop {
        for (i, y) in input.iter().enumerate() {
            let mut line = String::new();
            for (j, x) in y.chars().enumerate() {
                let cnt = (x, get_neighbour_count(i, j, &input));
                match cnt {
                    ('L', (_, _, 0)) => line += "#",
                    ('#', (_, _, o)) => {
                        if o >= 4 {
                            line += "L";
                        } else {
                            line += "#";
                        }
                    }
                    (c, _) => line += &c.to_string()[..],
                }
            }
            new_input.push(line);
        }
        let (cond, cnt) = check(&input, &new_input);
        if cond {
            return Ok(cnt);
        }
        input = new_input.clone();
        new_input.clear();
    }
}

fn part2(input: &Vec<String>) -> Result<usize, &str> {
    let mut input = input.clone();
    let mut new_input: Vec<String> = Vec::new();
    loop {
        for (i, y) in input.iter().enumerate() {
            let mut line = String::new();
            for (j, x) in y.chars().enumerate() {
                let c = input[i].chars().nth(j).unwrap();
                if c == '.' {
                    line.push('.');
                    continue;
                }
                let cnt = get_visible_seats(i as isize, j as isize, &input);
                match (c, cnt) {
                    ('L', 0) => line += "#",
                    ('#', o) => {
                        if o >= 5 {
                            line += "L";
                        } else {
                            line += "#";
                        }
                    }
                    (c, _) => line += &c.to_string()[..],
                }
            }
            new_input.push(line);
        }
        let (cond, cnt) = check(&input, &new_input);
        if cond {
            return Ok(cnt);
        }
        input = new_input.clone();
        new_input.clear();
    }
}

pub fn run() {
    let input = parse();
    runner::result(part1(&input), part2(&input));
}
