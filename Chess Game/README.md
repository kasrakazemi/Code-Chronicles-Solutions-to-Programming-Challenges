# Chess Board and Piece Management

This programming challenge involves creating a Python program for managing a chess board and its pieces. The goal is to implement various operations, such as adding, removing, and moving chess pieces, while ensuring that the moves are valid according to the rules of chess.

## Problem Statement

You are tasked with implementing two classes: `Piece` and `Board`.

### `Piece` Class

The `Piece` class represents a chess piece and has the following attributes:
- `sort`: The type of chess piece (e.g., "P" for pawn, "K" for king).
- `color`: The color of the piece ("white" or "black").
- `position`: The current position of the piece on the chess board.

### `Board` Class

The `Board` class represents the chess board and has the following methods:

1. `add(piece)`: Adds a chess piece to the board. The move is valid if the target position is empty, and the same piece (color and sort) does not exist on the board.
2. `remove(position)`: Removes a chess piece from the board. The move is valid if the target position contains a piece, and specific conditions are met (e.g., both a black king and a white pawn must exist on the board).
3. `move(piece, position2)`: Moves a chess piece to a new position. The move is valid if the piece exists on the board, the target position is empty, or the target position contains a piece of the opposite color, and specific conditions are met (e.g., not moving the king to a check position).
4. `is_mate(color)`: Checks if the specified color is in a checkmate position (this part can be implemented as an additional challenge).

## How to Use

To use this program, you can follow these steps:

1. Create instances of the `Piece` class to represent chess pieces with different attributes.
2. Create an instance of the `Board` class to represent the chess board.
3. Use the `add`, `remove`, and `move` methods to manipulate the board based on the rules of chess.
4. Test the program with various scenarios to ensure that the moves are valid and that the board state is correctly updated.

## Unit Testing

Included in this repository is a unit test file that checks the functionality of the `add` method. You can use this as a template to create additional test cases for the `remove`, `move`, and `is_mate` methods.

## Contributions

Contributions to this project are welcome! If you have suggestions for improvements or encounter any issues, please feel free to open a pull request or an issue.
