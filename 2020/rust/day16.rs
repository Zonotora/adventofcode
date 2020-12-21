use crate::runner;
use itertools::Itertools;
use std::collections::HashSet;

fn parse() -> Vec<String> {
    runner::read("input/16")
        .unwrap()
        .split("\n\n")
        .map(|s| String::from(s))
        .collect()
}

type Ticket = Vec<usize>;

#[derive(Debug)]
struct Interval {
    name: String,
    min1: usize,
    max1: usize,
    min2: usize,
    max2: usize,
}

impl Interval {
    fn new(input: &str) -> Interval {
        let (name, interval) = input.split(':').collect_tuple::<(&str, &str)>().unwrap();
        let interval = interval
            .split(' ')
            .filter(|s| *s != "or" && *s != "")
            .map(|s| s.split('-').collect_tuple::<(&str, &str)>().unwrap())
            .map(|(s, e)| (s.parse::<usize>().unwrap(), e.parse::<usize>().unwrap()))
            .collect::<Vec<(usize, usize)>>();

        Interval {
            name: String::from(name),
            min1: interval[0].0,
            max1: interval[0].1,
            min2: interval[1].0,
            max2: interval[1].1,
        }
    }
    fn name(&self) -> &str {
        &self.name[..]
    }
    fn valid(&self, value: usize) -> bool {
        (value >= self.min1 && value <= self.max1 || value >= self.min2 && value <= self.max2)
    }
}

fn ticket_from_str(ticket: &str) -> Ticket {
    ticket
        .split(',')
        .map(|s| s.parse::<usize>().unwrap())
        .collect()
}

fn generate(input: &Vec<String>) -> (Vec<Interval>, Ticket, Vec<Ticket>) {
    let mut input = input.iter();
    let intervals = input
        .next()
        .unwrap()
        .split('\n')
        .map(|s| Interval::new(s))
        .collect_vec();
    let ticket = ticket_from_str(input.next().unwrap().split(':').collect_vec()[1].trim());
    let tickets = input
        .next()
        .unwrap()
        .split('\n')
        .filter(|s| *s != "" && !s.starts_with("nearby"))
        .map(|s| ticket_from_str(s))
        .collect_vec();
    (intervals, ticket, tickets)
}

fn part1(
    (intervals, ticket, tickets): &(Vec<Interval>, Ticket, Vec<Ticket>),
) -> Result<usize, &str> {
    Ok(tickets
        .iter()
        .map(|x| {
            let mut res = 0;
            for value in x {
                if !intervals.iter().any(|interval| interval.valid(*value)) {
                    res += value;
                }
            }
            res
        })
        .sum())
}

fn part2(
    (intervals, ticket, tickets): &(Vec<Interval>, Ticket, Vec<Ticket>),
) -> Result<usize, &str> {
    let valids: Vec<&Ticket> = tickets
        .iter()
        .filter(|t| {
            t.iter()
                .all(|value| intervals.iter().any(|interval| interval.valid(*value)))
        })
        .collect();
    let valids = (0..valids[0].len())
        .map(|i| {
            valids
                .iter()
                .map(|inner| inner[i].clone())
                .collect::<Vec<usize>>()
        })
        .collect_vec();

    let mut valid_for_intervals: Vec<(usize, Vec<usize>)> =
        (0..).zip(vec![Vec::new(); ticket.len()]).collect();
    for (i, interval) in intervals.iter().enumerate() {
        for (j, valid) in valids.iter().enumerate() {
            if valid.iter().all(|t| interval.valid(*t)) {
                valid_for_intervals[i].1.push(j);
            }
        }
    }
    valid_for_intervals.sort_by(|(_, a), (_, b)| a.len().cmp(&b.len()));

    let mut used = valid_for_intervals[0].1.clone();
    let departures: usize = valid_for_intervals
        .iter()
        .skip(1)
        .map(|(i, v)| {
            let nv: Vec<usize> = v
                .iter()
                .filter(|x| !used.contains(x))
                .map(|x| x.to_owned())
                .collect();
            used.append(&mut nv.clone());
            (intervals[*i].name(), nv[0])
        })
        .filter(|(name, _)| name.starts_with("departure"))
        .map(|(_, i)| ticket[i])
        .product();
    Ok(departures)
}

pub fn run() {
    let input = generate(&parse());
    runner::result(part1(&input), part2(&input));
}
