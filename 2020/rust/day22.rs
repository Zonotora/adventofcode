use crate::runner;
use std::collections::HashSet;

fn parse() -> Vec<String> {
    runner::read("input/22")
        .unwrap()
        .split("Player")
        .map(|s| String::from(s))
        .collect()
}

fn generate(input: &Vec<String>) -> Vec<Vec<usize>> {
    input
        .iter()
        .map(|s| {
            s.split("\n")
                .skip(1)
                .filter(|x| *x != "")
                .map(|x| x.parse::<_>().unwrap())
                .collect::<_>()
        })
        .skip(1)
        .collect()
}

fn recursive_combat(
    player1: &mut Vec<usize>,
    player2: &mut Vec<usize>,
    card1: usize,
    card2: usize,
) -> usize {
    let mut winner = 1;
    let prime = (14695981039346656037, 1099511628211);
    let mut game: HashSet<(usize, usize)> = HashSet::new();
    loop {
        let hash1 = player1
            .iter()
            .enumerate()
            .fold(prime.0, |acc, (i, x)| acc ^ ((i + 1) * x * prime.1));
        let hash2 = player2
            .iter()
            .enumerate()
            .fold(prime.0, |acc, (i, x)| acc ^ ((i + 1) * x * prime.1));
        if player1.len() == 0 || player2.len() == 0 {
            return winner;
        } else if let Some(_) = game.get(&(1, hash1)) {
            return 1;
        } else if let Some(_) = game.get(&(2, hash2)) {
            return 1;
        }
        game.insert((1, hash1));
        game.insert((2, hash2));

        let card1 = player1.remove(0);
        let card2 = player2.remove(0);

        if card1 <= player1.len() && card2 <= player2.len() {
            let mut copy1: Vec<usize> = player1[0..card1].iter().cloned().collect();
            let mut copy2: Vec<usize> = player2[0..card2].iter().cloned().collect();
            winner = recursive_combat(&mut copy1, &mut copy2, card1, card2);
        } else if card1 > card2 {
            winner = 1;
        } else {
            winner = 2;
        }

        if winner == 1 {
            player1.append(&mut vec![card1, card2]);
        } else {
            player2.append(&mut vec![card2, card1]);
        }
    }
}

fn part1(input: &Vec<Vec<usize>>) -> Result<usize, &str> {
    let mut player1 = input[0].clone();
    let mut player2 = input[1].clone();
    loop {
        if player1.len() == 0 {
            return Ok(player2
                .iter()
                .rev()
                .enumerate()
                .fold(0, |acc, (i, x)| acc + (i + 1) * x));
        }
        if player2.len() == 0 {
            return Ok(player1
                .iter()
                .rev()
                .enumerate()
                .fold(0, |acc, (i, x)| acc + (i + 1) * x));
        }
        let card1 = player1.remove(0);
        let card2 = player2.remove(0);
        if card1 > card2 {
            player1.append(&mut vec![card1, card2]);
        } else {
            player2.append(&mut vec![card2, card1]);
        }
    }
    Err("Error: no value found!")
}

fn part2(input: &Vec<Vec<usize>>) -> Result<usize, &str> {
    let mut player1 = input[0].clone();
    let mut player2 = input[1].clone();
    let length = (player1.len(), player2.len());
    let winner = recursive_combat(&mut player1, &mut player2, length.0, length.1);
    if winner == 1 {
        return Ok(player1
            .iter()
            .rev()
            .enumerate()
            .fold(0, |acc, (i, x)| acc + (i + 1) * x));
    } else {
        return Ok(player2
            .iter()
            .rev()
            .enumerate()
            .fold(0, |acc, (i, x)| acc + (i + 1) * x));
    }
}

pub fn run() {
    let input = generate(&parse());
    runner::result(part1(&input), part2(&input));
}
