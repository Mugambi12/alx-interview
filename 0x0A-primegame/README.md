### Prime Game

**Project Description:**
In this project, you will apply your knowledge of prime numbers, game theory, and algorithm optimization to solve a competitive game scenario. The goal is to determine the winner of a game where players strategically remove prime numbers and their multiples from a set of consecutive integers.

---

**Concepts Covered:**

- **Prime Numbers:**
  - Understanding the concept of prime numbers and identifying them within a range efficiently.
- **Sieve of Eratosthenes:**
  - Implementing an efficient algorithm for finding all prime numbers up to a given limit.
- **Game Theory:**
  - Applying basic principles of competitive games and understanding optimal play strategies.
- **Dynamic Programming/Memoization:**
  - Using previous results to expedite future calculations, particularly beneficial for optimizing solutions for multiple rounds.
- **Python Programming:**
  - Employing loops, conditional statements, arrays, and lists for implementing game logic and algorithms.

---

**Resources:**

- **Prime Numbers and Sieve of Eratosthenes:**
  - [Khan Academy](https://intranet.alxswe.com/rltoken/IUKEfGVroNza8u37x0lEzw): Prime Numbers
  - [Sieve of Eratosthenes in Python](https://intranet.alxswe.com/rltoken/sVjdrNQEaErO_qRYsVMTEg): Step-by-step Guide
- **Game Theory Basics:**
  - [Introduction to Game Theory](https://intranet.alxswe.com/rltoken/lH4z--LnsuXYKh23Ji9Elw): Understanding Strategic Decision-making
- **Dynamic Programming:**
  - [What Is Dynamic Programming With Python Examples](https://intranet.alxswe.com/rltoken/W6T0RxWaFG3GisPxLLNYkQ): An introduction to dynamic programming with Python examples.
- **Python Official Documentation:**
  - [Python Lists](https://intranet.alxswe.com/rltoken/JTEGXnSDYDp8yblD9y86eg): Managing lists in Python, essential for tracking game state.

By mastering these concepts and utilizing the recommended resources, you'll be well-equipped to tackle the project's mathematical and programming challenges effectively. Success in this project hinges on the application of efficient algorithms to manage the game's state and make optimal decisions based on the game's rules.

---

**Project Requirements:**

- **Allowed Editors:** vi, vim, emacs
- **Platform:** Ubuntu 20.04 LTS
- **Python Version:** 3.4.3
- **PEP 8 Style:** Ensure adherence to PEP 8 style guidelines.
- **Executable Files:** All files must be executable.
- **README.md:** A mandatory README.md file, located at the root of the project folder.

---

**Project Task:**
**0. Prime Game**

- **Description:** Maria and Ben engage in a game where they remove prime numbers and their multiples from a set of consecutive integers. The player unable to make a move loses the game.
- **Function Prototype:** `def isWinner(x, nums)`
- **Parameters:** `x` (number of rounds), `nums` (array of upper limits for each round)
- **Return:** Name of the player who won the most rounds or None if the winner cannot be determined.
- **Constraints:** `n` and `x` will not exceed 10000, and no packages can be imported.
- **Example:**
  - `x = 3, nums = [4, 5, 1]`
    - First round: 4
      - Maria picks 2 and removes 2, 4, leaving 1, 3
      - Ben picks 3 and removes 3, leaving 1
      - Ben wins because there are no prime numbers left for Maria to choose
    - Second round: 5
      - Maria picks 2 and removes 2, 4, leaving 1, 3, 5
      - Ben picks 3 and removes 3, leaving 1, 5
      - Maria picks 5 and removes 5, leaving 1
      - Maria wins because there are no prime numbers left for Ben to choose
    - Third round: 1
      - Ben wins because there are no prime numbers for Maria to choose
    - Result: Ben has the most wins

---
