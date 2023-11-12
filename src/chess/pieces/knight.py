import chess
from chess.moves.move_utils import *
from chess.pieces.piece import Piece

class Knight(Piece):
    def __init__(self, bb, color):
        super().__init__(bb, color, chess.KNIGHT)
        self.generate_move_lookup()

    def generate_move_lookup(self):
        self.moves_lookup = {}
        for square, bb_square in zip(chess.SQUARES, chess.BB_SQUARES):
            new_square = 0
            new_square += move_2_down_1_left(bb_square)
            new_square += move_2_down_1_right(bb_square)
            new_square += move_2_up_1_left(bb_square)
            new_square += move_2_up_1_right(bb_square)
            new_square += move_2_left_1_up(bb_square)
            new_square += move_2_left_1_down(bb_square)
            new_square += move_2_right_1_up(bb_square)
            new_square += move_2_right_1_down(bb_square)
            self.moves_lookup[square] = new_square





