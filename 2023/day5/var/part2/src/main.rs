extern crate serde;
extern crate serde_json;
#[macro_use] extern crate serde_derive;

use std::fs::File;
use std::io::Read;

#[derive(Serialize, Deserialize)]
struct Input {
    seed_ranges: Vec<(u64, u64)>,
    maps: Vec<Vec<(u64, u64, u64)>>,
}

fn main() {
    let mut file = File::open("input.json").unwrap();
    let mut input = String::new();
    file.read_to_string(&mut input).unwrap();

    let json: Input =
        serde_json::from_str(&input).unwrap();

    let mut mapped_seeds: Vec<u64> = Vec::new();

    for range in json.seed_ranges {
        for mut seed in range.0..range.1 {
            for map in &json.maps {
                for (dest, src, length) in map {
                    if (src..&((src + length))).contains(&&seed) {
                        seed = dest + seed - src;
                        break;
                    }
                }
            }
            mapped_seeds.push(seed);
        }
    }

    let lowest_distance = mapped_seeds.iter().min();
    match lowest_distance {
        Some(min) => println!( "Lowest distance is {}", min ),
        None      => println!( "Vector is empty" ),
    }
}
