# Below is the unit test code
import unittest
from solution import Piece
from solution import Board

class Test(unittest.TestCase):

    def test_add_piece(self):
        # Create a new chess board
        board = Board()

        # Create a chess piece (Pawn) and add it to the board
        piece = Piece("P", "white", (1, 1))
        board.add(piece)

        # Check if the piece's position is in the board's positions
        self.assertTrue((1, 1) in board.kingDic.keys())

# Note: The test case provided checks if a chess piece is correctly added to the board.
