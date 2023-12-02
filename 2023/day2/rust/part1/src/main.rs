use std::fs;

const MAX_RED: i32 = 12;
const MAX_GREEN: i32 = 13;
const MAX_BLU: i32 = 14;

fn main() {
    let input = match fs::read_to_string("../../input.txt") {
        Ok(string) => string,
        Err(error) => panic!("Can't read file! {:#}", error),
    };

    let games = input.split("\n").collect::<Vec<&str>>();

    let mut total: i32 = 0;

    for (index, game) in games.iter().enumerate() {
        let id = index + 1;

        let sets = &game[game.find(":").unwrap() + 2..game.len()];

        let mut valid = true;
        for set in sets.split("; ").collect::<Vec<&str>>() {
            let (mut red, mut green, mut blue) = (0, 0, 0);
            for s in set.split(", ").collect::<Vec<&str>>() {
                let comp = s.split(" ").collect::<Vec<&str>>();
                let num: i32 = comp[0].parse::<i32>().unwrap();
                let color = comp[1];
                match color {
                    "red" => red += num,
                    "blue" => blue += num,
                    "green" => green += num,
                    &_ => panic!("Should be one of those values"),
                }
            }
            if red > MAX_RED || green > MAX_GREEN || blue > MAX_BLU {
                valid = false;
            }
        }

        if valid {
            total += id as i32
        };
    }

    println!("Answer is {total}.");
}