extern crate serde;
extern crate serde_json;
#[macro_use] extern crate serde_derive;

use std::fs::File;
use std::io::Read;

#[derive(Serialize, Deserialize)]
struct Input {
    seed_ranges: Vec<(u32, u32)>,
    maps: Vec<Vec<(u32, u32, u32)>>,
}

fn main() {
    let mut file = File::open("input.json").unwrap();
    let mut input = String::new();
    file.read_to_string(&mut input).unwrap();

    let json: Input =
        serde_json::from_str(&input).unwrap();

    println!("{:?}", json.maps);
}
