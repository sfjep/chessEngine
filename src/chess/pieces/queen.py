import chess
import chess.utils as utils
from chess.pieces.piece import Piece

class Queen(Piece):
    def __init__(self, bb, color, piece_type):
        super().__init__(bb, color, piece_type)
        self.generate_move_lookup()

    def generate_move_lookup(self):
        self.moves_lookup = {}
        for square, bb_square in zip(chess.SQUARES, chess.BB_SQUARES):
            self.moves_lookup[square] = (
                ((utils.get_rank_from_bb(bb_square) | utils.get_file_from_bb(bb_square)) & ~bb_square) |
                utils.get_bb_diagonals_from_square_int(square)
            )
