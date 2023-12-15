# 0x02. Minimum Operations

## Overview

This project is centered around solving the "Minimum Operations" problem using Python. The primary goal is to calculate the fewest number of operations needed to achieve a specific number of characters (H) in a text file, where only two operations (Copy All and Paste) are allowed.

## Requirements

### General

- **Allowed Editors:** vi, vim, emacs
- **Interpretation/Compilation:** Ubuntu 20.04 LTS using python3 (version 3.4.3)
- **File Ending:** All files should end with a new line
- **Shebang Line:** The first line of all files should be exactly `#!/usr/bin/python3`
- **README.md:** A mandatory file at the root of the project folder
- **Documentation:** Code should be well-documented
- **Coding Style:** PEP 8 style (version 1.7.x)
- **Execution:** All files must be executable

## Tasks

### 0. Minimum Operations

- **Description:** Given a number `n`, write a method `minOperations(n)` that calculates the fewest number of operations needed to result in exactly `n` H characters in the file.

- **Prototype:** `def minOperations(n) -> int`
- **Returns:** An integer
- **If n is impossible to achieve:** Return 0

#### Example:

```python
n = 9

# Operations:
# H => Copy All => Paste => HH => Paste => HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH
# Number of operations: 6

minOperations(n)  # Output: 6
```

## Testing

```python
# Example usage in 0-main.py
minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
```

## Repository Details

- **GitHub Repository:** [alx-interview](https://github.com/username/alx-interview)
- **Directory:** 0x02-minimum_operations
- **File:** 0-minoperations.py

---
