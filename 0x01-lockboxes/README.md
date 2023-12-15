# 0x01. Lockboxes

## Algorithm - Python

### Overview

This project, "Lockboxes," is part of the Holberton School curriculum and was completed by Carrie Ybay, a Software Engineer. The project took place from Dec 4, 2023, 6:00 AM, to Dec 8, 2023, 6:00 AM, with an auto review scheduled at the deadline.

## Requirements

### General

- Allowed editors: vi, vim, emacs
- All files interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the project folder is mandatory
- Code documentation is required
- Code should follow the PEP 8 style (version 1.7.x)
- All files must be executable

## Tasks

### 0. Lockboxes (mandatory)

- **Score: 0.0% (Checks completed: 0.0%)**
- Prototype: `def canUnlockAll(boxes)`
- `boxes` is a list of lists
- A key with the same number as a box opens that box
- All keys will be positive integers
- There can be keys that do not have boxes
- The first box `boxes[0]` is unlocked
- Return True if all boxes can be opened, else return False

### Example

```python
#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # Output: False
```
