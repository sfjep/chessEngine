from Chess.pieces.piece import Piece

class Pawn(Piece):
    def __init__(self, bb, color):
        super().__init__(bb, color)
    # En passant
    # Two steps forward
    # One step forward
    # Captures
    # Promotion
    