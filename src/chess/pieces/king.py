import chess
from chess.pieces.piece import Piece
from chess.moves.move_utils import MoveUtils


class King(Piece):
    def __init__(self, bb, color, piece_type):
        super().__init__(bb, color, piece_type)
        self.generate_move_lookup()

    def generate_move_lookup(self):
        self.moves_lookup = {}
        for color in chess.COLORS:
            for square, bb_square in zip(chess.SQUARES, chess.BB_SQUARES):
                new_square = (
                    MoveUtils.move_left(bb_square)
                    | MoveUtils.move_right(bb_square)
                    | MoveUtils.move_up(bb_square)
                    | MoveUtils.move_up_left(bb_square)
                    | MoveUtils.move_up_right(bb_square)
                    | MoveUtils.move_down(bb_square)
                    | MoveUtils.move_down_left(bb_square)
                    | MoveUtils.move_down_right(bb_square)
                )
                self.moves_lookup[square, color] = new_square
