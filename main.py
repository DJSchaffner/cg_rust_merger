import pathlib
import sys
import os
import re

def parse_file(path: pathlib.Path, main_file: str, content: list):
  """Parses a given rust file into the content list.

  Args:
      path (pathlib.Path): A path to the file
      content (list): A list of all lines of content
  """
  with open(path, "r") as file:
    # Put file in mod section
    if path.name != main_file:
      content.append(f"mod {path.stem} {{\n")

    while line := file.readline():
      # Remove mod calls in file
      if not re.match("mod\s+.*;", line) is None:
        pass
      else:
        content.append(line)

    # Close file mod section
    if path.name != main_file:
      content.append(f"\n}}\n")

  # Add newline as delimiter
  content.append("\n")

def find_files(dir: pathlib.Path):
  """Finds all files in the given directory recursively.

  Args:
      dir (pathlib.Path): The root directory for finding files

  Yields:
      pathlib.Path: The next file in the given directory
  """
  for dirpath, _dirname, files in os.walk(dir):
    for name in files:
      if name.lower().endswith(".rs"):
        yield pathlib.Path(dirpath) / name

if __name__ == "__main__":
  root_dir = pathlib.Path(sys.argv[1])
  main_file = sys.argv[2]
  out_file = root_dir / "output.rs"
  content = list()

  # Remove output file if it already exists
  if out_file.exists():
    out_file.unlink()

  # Parse all files in current directory recursively
  for file in find_files(root_dir):
    parse_file(file, main_file, content)

  print(f"Writing file {out_file} ...");

  # Write output file
  with open(out_file, "w") as file:
    file.writelines(content)