# CG Rust Merger

This is a very basic parser that will parse a Rust project into a single file for websites like CodinGame.  

No guarantess this is bug free and respects all possible file structures in Rust but as of now this works for my purposes.  
Feel free to open a ticket with feature requests or bug reports if you have / find any.

# Usage

Call cg_rust_merger.exe \<PathToProject> \<RelativeMainFilePath>  
ex: ./ cg_rust_merger.exe C:/myrustproject/ src/main.rs
  
Example `tasks.json` file for VSCode:
```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "merge",
      "type": "process",
      "command": "C:/cg_rust_merger/cg_rust_merger.exe",
      "args": ["${workspaceFolder}", "src/main.rs"],
      "presentation": {
        "echo": true,
        "reveal": "always",
        "focus": false,
        "panel": "shared",
        "showReuseMessage": true,
        "clear": false
      }
    }
  ]
}
```
