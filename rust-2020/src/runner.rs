use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

pub fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

pub fn result<T: std::fmt::Display>(part1: Result<T, &str>, part2: Result<T, &str>) {
    println!("part1: {}\tpart2: {}", part1.unwrap(), part2.unwrap());
}
