from chess.pieces.piece import Piece

class Bishop(Piece):
    def __init__(self, bb, color):
        super().__init__(bb, color)

    def getMovesLookupDict(self):
        pass