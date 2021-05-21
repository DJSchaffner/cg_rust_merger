mod elo;
mod subdir;

use std::io;
use crate::subdir::subdirfile;

fn main() {
  println!("{}", elo::lebo());
  println!("{}", subdirfile::my_life());
}