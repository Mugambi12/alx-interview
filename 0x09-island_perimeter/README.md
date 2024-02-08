# Island Perimeter

## Description

This project implements a function `island_perimeter(grid)` that calculates the perimeter of an island described in a grid.

- `grid` is a list of lists of integers where:
  - 0 represents water
  - 1 represents land
- Each cell is square, with a side length of 1.
- Cells are connected horizontally/vertically (not diagonally).
- The grid is rectangular, with its width and height not exceeding 100.
- The grid is completely surrounded by water.
- There is only one island (or nothing).
- The island doesn’t have "lakes" (water inside that isn’t connected to the water surrounding the island).

## Requirements

### General

- Allowed editors: vi, vim, emacs
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.4.3)
- All files should end with a new line.
- The first line of all files should be exactly `#!/usr/bin/python3`.
- A `README.md` file, at the root of the folder of the project, is mandatory.
- Code should use the PEP 8 style (version 1.7).
- No importing of any modules allowed.
- All modules and functions must be documented.
- All files must be executable.

## Usage

To use the `island_perimeter` function, import it into your Python script and provide a grid as an argument. The function will return the perimeter of the island described in the grid.

Example usage:

```python
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
print(island_perimeter(grid))  # Output: 12
```
