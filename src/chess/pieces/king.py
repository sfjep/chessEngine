import chess
from chess.pieces.piece import Piece
from chess.moves.move_utils import *


class King(Piece):
    def __init__(self, bb, color):
        super().__init__(bb, color, chess.KING)
        self.generate_move_lookup()

    def generate_move_lookup(self):
        self.moves_lookup = {}
        for color in chess.COLORS:
            for square, bb_square in zip(chess.SQUARES, chess.BB_SQUARES):
                new_square = (
                    move_left(bb_square)
                    | move_right(bb_square)
                    | move_up(bb_square)
                    | move_up_left(bb_square)
                    | move_up_right(bb_square)
                    | move_down(bb_square)
                    | move_down_left(bb_square)
                    | move_down_right(bb_square)
                )
                self.moves_lookup[square, color] = new_square
