import chess
from chess import utils
from chess.pieces.piece import Piece

class Rook(Piece):
    def __init__(self, bb, color):
        super().__init__(bb, color, chess.ROOK)
        self.generate_move_lookup()

    def generate_move_lookup(self):
        self.moves_lookup = {}
        for square, bb_square in zip(chess.SQUARES, chess.BB_SQUARES):
            self.moves_lookup[square] = (
                utils.get_rank_from_bb(bb_square) |
                utils.get_file_from_bb(bb_square)) & ~bb_square
