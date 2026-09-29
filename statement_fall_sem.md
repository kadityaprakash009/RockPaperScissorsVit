# Problem Statement

**Project:** Rock, Paper, Scissors (CLI Game)
**Language:** Python 3.6+
**Institution:** VIT Bhopal University
**Author:** K Aditya Prakash (26BSA10013), BTech CSE 1021
**Faculty:** Pradeep Kumar Mishra
**Date:** 29/09/2026

## Problem Description

Rock, Paper, Scissors is a classic two-player hand game in which each player simultaneously chooses one of three options. The goal of this project is to build a **command-line version** of the game where a human player competes against a computer opponent over a fixed number of rounds, with the program keeping score and announcing an overall winner.

## Objectives

- Build a fully terminal-based, interactive game that runs without any GUI.
- Implement the standard rules of Rock, Paper, Scissors.
- Let the computer choose its move randomly and fairly each round.
- Track the score of both the player and the computer across rounds.
- Display the result of every round and the final outcome of the game.

## Game Rules

| Player | Computer | Result |
| --- | --- | --- |
| rock | scissors | Player wins |
| paper | rock | Player wins |
| scissors | paper | Player wins |
| same choice | same choice | Tie (no points) |
| any other combination | | Computer wins |

## Input

- The player's choice for each round, typed in the terminal: `rock`, `paper` or `scissors` (lowercase).

## Output

- The computer's choice and the result of each round (win, loss or tie).
- The final scores of the player and the computer.
- A closing message declaring the player the winner, the computer the winner, or a tie game.

## Constraints and Assumptions

- The game consists of exactly **3 rounds**.
- Only the Python standard library (`random`) is used, so there are no external dependencies.
- The program must run entirely from a terminal using `python rock_paper_scissors.py`.
- Input is case-sensitive; invalid input is currently treated as a computer win for that round.

## Expected Outcome

A working, dependency-free command-line game that follows the standard rules, keeps accurate scores, and clearly reports the final result.

## Possible Extensions

- Validate input and re-prompt on invalid entries.
- Make the number of rounds configurable.
- Add a play-again option and score history.
- Add extra modes such as best-of-N or Rock-Paper-Scissors-Lizard-Spock.
