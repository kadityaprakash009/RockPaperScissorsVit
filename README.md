# Rock, Paper, Scissors (CLI)

A simple command-line Rock, Paper, Scissors game written in Python. You play three rounds against the computer, and the program announces the winner at the end.

## Features

- Best-of-three format (3 rounds)
- Computer picks randomly each round
- Running score and final result printed at the end

## Requirements

- **Python 3.6 or newer** (no third-party packages required)
- A terminal / command prompt

The game uses only Python's standard library (`random`), so there are **no dependencies to install** and **no configuration files or environment variables** to set up.

## Setup

### 1. Check that Python is installed

```bash
python --version
```

or, on some systems (macOS / Linux):

```bash
python3 --version
```

If Python is not installed, download it from https://www.python.org/downloads/ and install it. On Windows, tick **"Add Python to PATH"** during installation.

### 2. Get the project

Clone the repository and move into its folder:

```bash
git clone <your-repository-url>
cd <repository-folder-name>
```

Alternatively, download the repository as a ZIP from GitHub, extract it, and open a terminal in the extracted folder.

### 3. (Optional) Create a virtual environment

Not required, since there are no dependencies, but supported if you prefer isolation:

```bash
python -m venv venv

# Activate it:
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows
```

### 4. Install dependencies

None needed. If a `requirements.txt` is present, it is intentionally empty of third-party packages.

## Running the Game

From the project's root folder, run (replace the filename if yours differs, e.g. `main.py`):

```bash
python rock_paper_scissors.py
```

or, on macOS / Linux if `python` is not found:

```bash
python3 rock_paper_scissors.py
```

## How to Play

1. The game runs **3 rounds**.
2. Each round, you'll see the prompt:
   ```
   Select rock, paper, or scissors:
   ```
   Type `rock`, `paper`, or `scissors` (all **lowercase**) and press **Enter**.
3. The computer's choice and the round result are displayed.
4. After round 3, the final scores and overall winner are shown.

### Rules

- Rock beats scissors
- Scissors beats paper
- Paper beats rock
- Same choice = tie (no points)

### Example Session

```
Round 1
Select rock, paper, or scissors: rock
Computer chose: scissors
You win!
Round 2
Select rock, paper, or scissors: paper
Computer chose: paper
It's a tie!
Round 3
Select rock, paper, or scissors: scissors
Computer chose: rock
Computer wins!
Final Score:
Your score: 1
Computer score: 1
It's a tie game!
```

## Known Limitations

- Input must be typed in lowercase and spelled exactly (`rock`, `paper`, `scissors`). Any other input (including typos or capital letters) is currently counted as a computer win for that round.
- The number of rounds is fixed at 3 (change the `range(1, 4)` value in the code to adjust).

## Project Structure

```
.
├── rock_paper_scissors.py   # Game source code
└── README.md                # This file
```

## Troubleshooting

| Problem | Solution |
| --- | --- |
| `python: command not found` | Try `python3` instead, or reinstall Python and ensure it is on your PATH. |
| `SyntaxError` on startup | You are likely using Python 2. Use Python 3.6+. |
| Every round says "Computer wins!" | Check that you're typing `rock`, `paper`, or `scissors` in lowercase with no extra spaces. |
