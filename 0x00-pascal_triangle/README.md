# Project Title: Pascal's Triangle

## Description

This project focuses on creating a Python function that generates Pascal's Triangle. Pascal's Triangle is a mathematical concept where each number is the sum of the two directly above it.

## Learning Objectives

By completing this project, you will gain a better understanding of algorithms and Python programming. Specifically, you will implement a function to generate Pascal's Triangle and handle different edge cases.

## Project Structure

- **0x00-pascal_triangle**
  - **0-pascal_triangle.py**

## Task Details

### Task 0: Pascal's Triangle

Create a function `def pascal_triangle(n):` that returns a list of lists of integers representing Pascal’s triangle of n:

- Returns an empty list if n <= 0
- You can assume n will always be an integer

#### Example Usage

```python
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
```

#### Output

```
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
```

## Usage

Follow the instructions provided in the task file (`0-pascal_triangle.py`) to implement the `pascal_triangle` function. You can test your implementation using the provided example.

Execute the main script (`0-main.py`) to see the output of your function.

## Contributions

Contributions are welcome. Feel free to open issues or submit pull requests.

## License

This project is licensed under the [MIT License](LICENSE).

---
