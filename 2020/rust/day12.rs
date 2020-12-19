use crate::runner;

fn parse() -> Vec<String> {
    runner::read_lines("input/12")
        .unwrap()
        .map(|s| s.unwrap())
        .collect()
}

fn part1(input: &Vec<String>) -> Result<f64, &str> {
    let mut direction = (1.0, 0.0);
    let mut position = (0.0, 0.0);
    for x in input {
        let action = x.chars().next().unwrap();
        let value = &x[1..].parse::<f64>().unwrap();
        let (x, y) = position;
        let (dx, dy) = direction;
        match action {
            'N' => position = (x, y + value),
            'S' => position = (x, y - value),
            'E' => position = (x + value, y),
            'W' => position = (x - value, y),
            'L' => {
                let value = value.to_radians();
                direction = (
                    dx * value.cos() - dy * value.sin(),
                    dx * value.sin() + dy * value.cos(),
                )
            }
            'R' => {
                let value = value.to_radians();
                direction = (
                    dx * value.cos() + dy * value.sin(),
                    -dx * value.sin() + dy * value.cos(),
                )
            }
            'F' => position = (x + dx * value, y + dy * value),
            _ => (),
        }
    }

    Ok((position.0.abs() + position.1.abs()).round())
}

fn part2(input: &Vec<String>) -> Result<f64, &str> {
    let mut direction = (1.0, 0.0);
    let mut position = (0.0, 0.0);
    let mut waypoint = (10.0, 1.0);
    for x in input {
        let action = x.chars().next().unwrap();
        let value = &x[1..].parse::<f64>().unwrap();
        let (x, y) = position;
        let (wx, wy) = waypoint;
        match action {
            'N' => waypoint = (wx, wy + value),
            'S' => waypoint = (wx, wy - value),
            'E' => waypoint = (wx + value, wy),
            'W' => waypoint = (wx - value, wy),
            'L' => {
                let value = value.to_radians();
                waypoint = (
                    wx * value.cos() - wy * value.sin(),
                    wx * value.sin() + wy * value.cos(),
                )
            }
            'R' => {
                let value = value.to_radians();
                waypoint = (
                    wx * value.cos() + wy * value.sin(),
                    -wx * value.sin() + wy * value.cos(),
                )
            }
            'F' => position = (x + wx * value, y + wy * value),
            _ => (),
        }
    }

    Ok((position.0.abs() + position.1.abs()).round())
}

pub fn run() {
    let input = parse();
    runner::result(part1(&input), part2(&input));
}
