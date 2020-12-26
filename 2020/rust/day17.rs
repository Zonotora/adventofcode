use crate::runner;

fn parse() -> Vec<String> {
    runner::read_lines("input/17")
        .unwrap()
        .map(|s| s.unwrap())
        .collect()
}

type Layer = Vec<String>;

fn extend(input: &Vec<String>) -> Vec<String> {
    let mut input: Vec<String> = input
        .iter()
        .map(|s| {
            let mut s = s.clone();
            s.insert(0, '.');
            s.push('.');
            s
        })
        .collect();
    input.insert(0, (0..input[0].len()).map(|_| '.').collect::<String>());
    input.push((0..input[0].len()).map(|_| '.').collect::<String>());
    input
}

fn empty_line(length: usize) -> String {
    (0..length).map(|_| '.').collect()
}

fn empty(length: usize) -> Vec<String> {
    (0..length).map(|_| empty_line(length)).collect()
}
fn empty_block(length: usize, count: usize) -> Vec<Vec<String>> {
    (0..count).map(|_| empty(length)).collect()
}

fn get_neighbour_size(
    x: isize,
    y: isize,
    z: isize,
    w: isize,
    w_range: isize,
    input: &Vec<Vec<Layer>>,
) -> usize {
    let mut cnt = 0;
    for w_i in -1 + w_range..=1 - w_range {
        if w + w_i < 0 || w + w_i >= input.len() as isize {
            continue;
        }
        let layers = &input[(w + w_i) as usize];
        for z_i in -1..=1 {
            if z + z_i < 0 || z + z_i >= layers.len() as isize {
                continue;
            }
            let layer = &layers[(z + z_i) as usize];
            for y_i in -1..=1 {
                if y + y_i < 0 || y + y_i >= layer.len() as isize {
                    continue;
                }
                let row = &layer[(y + y_i) as usize];
                let length = row.len();
                for x_i in -1..=1 {
                    let mut row = row.chars();
                    if x + x_i < 0
                        || x + x_i >= length as isize
                        || (x_i == 0 && y_i == 0 && z_i == 0 && w_i == 0)
                    {
                        continue;
                    }
                    let c = row.nth((x + x_i) as usize).unwrap();
                    if c == '#' {
                        cnt += 1;
                    }
                }
            }
        }
    }
    cnt
}

fn compute_3d(
    layer_4d: &Vec<Vec<Layer>>,
    length: usize,
    w: usize,
    w_range: isize,
) -> (Vec<Layer>, usize) {
    let mut active = 0;
    let mut layers = layer_4d[w as usize].clone();
    let mut tmp_layers: Vec<Layer> = Vec::with_capacity(layers.len());

    for (z, layer) in layers.iter().enumerate() {
        let mut lines: Vec<String> = Vec::with_capacity(layer.len());
        lines.push(empty_line(length));
        for (y, states) in layer.iter().enumerate() {
            let mut line = String::with_capacity(states.len() + 2);
            line.push('.');
            for (x, c) in states.chars().enumerate() {
                let cnt = get_neighbour_size(
                    x as isize, y as isize, z as isize, w as isize, w_range, &layer_4d,
                );
                match (c, cnt) {
                    ('#', 2) | ('#', 3) | ('.', 3) => {
                        line.push('#');
                        active += 1;
                    }
                    _ => line.push('.'),
                }
            }
            line.push('.');
            lines.push(line);
        }
        lines.push(empty_line(length));
        tmp_layers.push(lines);
    }
    layers = tmp_layers.clone();
    layers.insert(0, empty(length));
    layers.push(empty(length));
    (layers, active)
}

fn part1(input: &Vec<String>) -> Result<usize, &str> {
    let mut input = extend(input);
    let mut layers: Vec<Layer> = vec![empty(input.len()), input.clone(), empty(input.len())];
    let mut length = input.len() + 2;
    let mut active = 0;
    for _ in 0..6 {
        let (l, a) = compute_3d(&vec![layers.clone()], length, 0, 1);
        layers = l;
        active = a;
        length += 2;
    }

    Ok(active)
}

fn part2(input: &Vec<String>) -> Result<usize, &str> {
    let mut input = extend(input);
    let mut layer_4d = vec![
        empty_block(input.len(), 3),
        vec![empty(input.len()), input.clone(), empty(input.len())],
        empty_block(input.len(), 3),
    ];
    let mut length = input.len() + 2;
    let mut total_active = 0;
    for _ in 0..6 {
        total_active = 0;
        let mut tmp_layer_4d: Vec<Vec<Layer>> = Vec::with_capacity(layer_4d.len());
        for (w, layer) in layer_4d.iter().enumerate() {
            let (layers, active) = compute_3d(&layer_4d, length, w, 0);
            tmp_layer_4d.push(layers);
            total_active += active;
        }
        layer_4d = tmp_layer_4d.clone();
        layer_4d.insert(0, empty_block(length, length - 2));
        layer_4d.push(empty_block(length, length - 2));
        length += 2;
    }
    Ok(total_active)
}

pub fn run() {
    let input = parse();
    runner::result(part1(&input), part2(&input));
}
