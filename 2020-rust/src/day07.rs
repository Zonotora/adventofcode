use crate::runner;
use std::collections::{HashMap, HashSet};

fn parse() -> HashMap<String, Vec<(usize, String)>> {
    let mut bags: HashMap<String, Vec<(usize, String)>> = HashMap::new();
    let input: Vec<(String, Vec<(usize, String)>)> = runner::read_lines("input/07")
        .unwrap()
        .map(|s| {
            let ss = s.unwrap();
            let parts: Vec<&str> = ss.split(", ").collect();
            let head: Vec<&str> = parts.first().unwrap().split(" ").collect();
            let key = head[0..2].to_vec().join("");
            let mut bs: Vec<(usize, String)> = Vec::new();
            if let Ok(val) = head[4].parse::<usize>() {
                bs.push((val, head[5..7].to_vec().join("")));
            }

            for p in parts.iter().skip(1) {
                let ps: Vec<&str> = p.split(" ").collect();
                bs.push((
                    ps.first().unwrap().parse::<usize>().unwrap(),
                    ps[1..3].to_vec().join(""),
                ))
            }
            (key, bs)
        })
        .collect();
    for (val, elem) in input {
        bags.insert(val, elem);
    }
    bags
}

fn contains_gold(
    key: &String,
    bags: &Vec<(usize, String)>,
    total: &HashMap<String, Vec<(usize, String)>>,
    valid: &mut HashSet<String>,
) {
    for (_, bag) in bags {
        if valid.contains(bag) || bag == "shinygold" {
            valid.insert(key.to_owned());
            break;
        } else {
            let bs = total.get(bag).unwrap();
            contains_gold(bag, bs, total, valid)
        }
    }
}

fn get_count(bags: &Vec<(usize, String)>, total: &HashMap<String, Vec<(usize, String)>>) -> usize {
    if bags.len() == 0 {
        return 1;
    }
    let mut bag_cnt: usize = 0;
    for (cnt, bag) in bags {
        let bs = total.get(bag).unwrap();
        let mut tmp = cnt * get_count(bs, total);
        if bs.len() != 0 {
            tmp += cnt;
        }
        bag_cnt += tmp;
    }

    bag_cnt
}

fn part1(input: &HashMap<String, Vec<(usize, String)>>) -> Result<usize, &str> {
    let mut valid_bags: HashSet<String> = HashSet::new();
    for _ in 0..3 {
        for (key, bags) in input {
            contains_gold(&key, bags, &input, &mut valid_bags);
        }
    }
    Ok(valid_bags.len())
}

fn part2(input: &HashMap<String, Vec<(usize, String)>>) -> Result<usize, &str> {
    Ok(get_count(input.get("shinygold").unwrap(), input))
}

pub fn run() {
    let input = parse();
    runner::result(part1(&input), part2(&input));
}
