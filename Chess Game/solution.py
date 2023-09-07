# Define a class for chess pieces
class Piece:
    def __init__(self, sort, color, position):
        self.sort = sort
        self.color = color
        self.position = position

# Define a class for the chess board
class Board():
    def __init__(self):
        # Initialize an empty dictionary to represent the board
        self.kingDic = {}

    def add(self, piece):
        # Add a chess piece to the board if it's a valid move
        if (
            (piece.sort, piece.color) in self.kingDic.values()
            or piece.position in self.kingDic.keys()
        ):
            print("Invalid query: This move is not allowed.")
        else:
            self.kingDic.update({piece.position: (piece.sort, piece.color)})

    def remove(self, position):
        # Remove a chess piece from the board if it's a valid move
        if (
            position not in self.kingDic.keys()
            or ("K", "black") not in self.kingDic.values()
            or ("P", "white") not in self.kingDic.values()
        ):
            print("Invalid query: This move is not allowed.")
        else:
            self.kingDic.pop(position)

    def move(self, piece, position2):
        # Move a chess piece to a new position if it's a valid move
        if (
            piece.position in self.kingDic.keys()
            and (piece.sort, piece.color) in self.kingDic.values()
            and position2 not in self.kingDic.keys()
        ):
            self.kingDic.update({position2: (piece.sort, piece.color)})
        elif (
            position2 in self.kingDic.keys()
            and piece.color != self.kingDic[position2][-1]
            and self.kingDic[position2[0]] != "K"
        ):
            # If a piece of the opposite color is present at the target position,
            # and it's not a king, remove it and move the current piece.
            self.kingDic.pop(position2)
            self.kingDic.update({position2: (piece.sort, piece.color)})
        else:
            print("Invalid query: This move is not allowed.")

    def is_mate(self, color):
        # Check if the given color is in a checkmate position
        pass

