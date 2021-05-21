import pathlib
import sys
import os
import re

def parse_file(path: pathlib.Path, content: list):
  """Parses a given rust file into the content list.

  Args:
      path (pathlib.Path): A path to the file
      content (list): A list of all lines of content
  """
  with open(path, "r") as file:
    while line := file.readline():
      # Parse mod calls
      if not (match := re.match("(pub )?\s*mod\s+(\S+)\s*;", line)) is None:
        name = visibility = None

        if len(match.groups()) == 2:
          visibility = match.groups()[0]
          name = match.groups()[1]
        else:
          name = match.groups()[0]

        # ./<name>.rs exists
        if (path.parent / f"{name}.rs").exists():
          content.append(f"{visibility + ' ' if visibility else ''}mod {name} {{\n")
          parse_file(path.parent / f"{name}.rs", content)
          content.append(f"}}\n")
        # ./<name>/mod.rs exists
        elif (path.parent / f"{name}/mod.rs").exists():
          content.append(f"{visibility + ' ' if visibility else ''}mod {name} {{\n")
          parse_file(path.parent / f"{name}/mod.rs", content)
          content.append(f"}}\n")
      else:
        content.append(line)

  # Add newline as delimiter
  content.append("\n")

if __name__ == "__main__":
  root_dir = pathlib.Path(sys.argv[1])
  main_file = sys.argv[2]
  out_file = root_dir / "output.rs"
  content = list()

  # Remove output file if it already exists
  if out_file.exists():
    out_file.unlink()

  # Recursively parse files starting from main file
  parse_file(root_dir / main_file, content)

  print(f"Writing file {out_file} ...");

  # Write output file
  with open(out_file, "w") as file:
    file.writelines(content)