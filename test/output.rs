mod elo {
pub fn lebo() -> String {
  String::from("ELO")
}
}
mod subdir {
pub  mod subdirfile {
pub fn my_life() -> String {
  String::from("MY LIFE")
}
}

}

use std::io;
use crate::subdir::subdirfile;

fn main() {
  println!("{}", elo::lebo());
  println!("{}", subdirfile::my_life());
}
