Question source :

https://github.com/RahnemaCollegee/algorithm_challenge/tree/main/challenge4

* This question is in persian language

# Wheel of Fortune Solver

Welcome to the Wheel of Fortune Solver, a JavaScript/python program that calculates the minimum rotations required to reach specific characters on a circular "wheel" based on a given password. This program is designed to tackle programming challenges involving character positioning and rotation.

## Problem Statement

Imagine a circular wheel with characters arranged along its edge. The goal is to find the shortest path (minimum rotations) to reach a specific set of characters indicated by a password. The wheel can rotate in both clockwise and counterclockwise directions.

### Example

Consider the following scenario:

- Wheel: "RTIGFIPR"
- Password: "GFI"

The program will find the shortest path to reach the characters "G," "F," and "I" on the wheel, calculating the total number of rotations needed.

## How the Code Works

The code is divided into two main functions:

1. `findLetters(character)`: This function finds all occurrences of a character in the wheel and returns their positions.

2. `findDistance(pointer, letters)`: This function calculates the minimum rotations needed to reach a character from the current pointer position.

The program then iterates through each character in the password, calculates the rotations needed for each character, and updates the pointer's position. Finally, it prints the total duration, which is the sum of time taken (number of characters visited) and rotations.

## Usage

To use this program, follow these steps:

1. Open a JavaScript/python environment.

2. Copy and paste the code into your environment.

3. Modify the `wheel` and `password` variables to test different scenarios.

4. Run the code to calculate the minimum rotations and total duration.

## Contributions

Contributions to this project are welcome! If you have suggestions for improvements or encounter any issues, please feel free to open a pull request or an issue.


Happy coding!
