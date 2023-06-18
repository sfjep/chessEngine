import chess
from chess.pieces.piece import Piece
from chess.utils import get_bb_diagonals_from_square_int

class Bishop(Piece):
    def __init__(self, bb, color):
        super().__init__(bb, color, chess.BISHOP)
        self.generate_move_lookup()

    def generate_move_lookup(self):
        self.moves_lookup = {
            square: get_bb_diagonals_from_square_int(square)
            for square in chess.SQUARES
        }
