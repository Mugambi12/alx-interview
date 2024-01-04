# 0x03. Log Parsing

## Overview

This project involves the development of a Python script for log parsing. The script reads input from standard input (stdin) line by line and computes various metrics based on the provided format. Additionally, it prints statistics after every 10 lines or upon a keyboard interruption (CTRL + C).

## Project Details

- **Author:** Alexa Orrico, Software Engineer at Holberton School
- **Project Weight:** 1
- **Project Duration:** Dec 18, 2023, 6:00 AM, to Dec 22, 2023, 6:00 AM
- **Auto QA Review:** 0.0/11 mandatory
- **Mandatory Tasks:** Log parsing script development
- **Optional Tasks:** None specified

## Requirements

### General

- **Allowed Editors:** vi, vim, emacs
- **Platform:** Ubuntu 20.04 LTS
- **Python Version:** 3.4.3
- **File Endings:** All files should end with a new line
- **Shebang Line:** The first line of all files should be exactly `#!/usr/bin/python3`
- **README.md:** A README.md file at the root of the project folder is mandatory
- **Coding Style:** Code should adhere to PEP 8 style (version 1.7.x)
- **Executable Files:** All files must be executable
- **File Length:** File length will be tested using `wc`

## Tasks

### Task 0: Log Parsing

- **Mandatory:** Yes
- **Score:** 0.0% (Checks completed: 0.0%)
- **Description:** Write a script that reads stdin line by line and computes metrics based on the specified input format. Print statistics after every 10 lines and/or upon a keyboard interruption (CTRL + C).

### Input Format:

```
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
```

### Statistics to Print:

1. Total file size: `File size: <total size>`
2. Number of lines by status code:
   - Possible status codes: 200, 301, 400, 401, 403, 404, 405, 500
   - Format: `<status code>: <number>`
   - Status codes should be printed in ascending order

### Example:

```bash
./0-generator.py | ./0-stats.py
```

```
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
File size: 11320
...
```

## Usage

Clone the GitHub repository and navigate to the project directory:

```bash
git clone https://github.com/mugambi12/alx-interview
cd alx-interview/0x03-log_parsing
```

Run the log generator and parser:

```bash
./0-generator.py | ./0-stats.py
```

## Repository Information

- **GitHub Repository:** [alx-interview](https://github.com/mugambi12/alx-interview)
- **Directory:** 0x03-log_parsing
- **File:** 0-stats.py

---
