# 0x05. N Queens

## Introduction

This project, "0x05. N Queens," is a Python program developed by Alexa Orrico, a Software Engineer at Holberton School. The goal of this project is to solve the N Queens puzzle, which involves placing N non-attacking queens on an N×N chessboard.

## Project Details

- **Author:** Alexa Orrico
- **Position:** Software Engineer at Holberton School
- **Project Weight:** 1
- **Project Start:** January 8, 2024, 6:00 AM
- **Project Deadline:** January 15, 2024, 6:00 AM
- **Review:** Ongoing second chance project
- **Review Status:**
  - Auto QA review: 0.0/15 mandatory
  - Altogether: 0.0%
  - Mandatory: 0.0%
  - Optional: No optional tasks

## Project Requirements

### General

- **Allowed Editors:** vi, vim, emacs
- **Environment:** Ubuntu 20.04 LTS using Python 3 (version 3.4.3)
- **File Requirements:**
  - All files end with a new line
  - The first line of all files is `#!/usr/bin/python3`
- **Documentation:**
  - A `README.md` file at the root of the project folder is mandatory
  - Code should follow PEP 8 style (version 1.7.*)
- **Execution:**
  - All files must be executable

### Tasks

#### 0. N Queens

- **Score:** 0.0% (Checks completed: 0.0%)
- **Task Description:**
  - Implement a program that solves the N Queens problem.
  - Usage: `nqueens N`
  - If the user provides the wrong number of arguments, print `Usage: nqueens N` and exit with status 1.
  - N must be an integer greater or equal to 4; otherwise, print an appropriate error message and exit with status 1.
  - The program should print every possible solution to the problem, with one solution per line.
  - You are only allowed to import the `sys` module.

#### Example

```bash
$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
```

```bash
$ ./0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
```

## Repository Information

- **GitHub Repository:** [alx-interview](#)
- **Directory:** 0x05-nqueens
- **File:** 0-nqueens.py

---
