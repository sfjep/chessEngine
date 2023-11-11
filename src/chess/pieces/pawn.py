import chess
from chess.moves.move_utils import *
from chess.pieces.piece import Piece

class Pawn(Piece):
    def __init__(self, bb, color):
        super().__init__(bb, color, chess.PAWN)
        self.generate_move_lookup()

    def generate_move_lookup(self):
        self.moves_lookup = {}
        for color in chess.COLORS:
            for square, bb_square in zip(chess.SQUARES, chess.BB_SQUARES):
                if color == chess.WHITE:
                    if (chess.BB_SQUARES[square] & chess.BB_RANK_1) != 0:
                        self.moves_lookup[square, color] = chess.BB_EMPTY
                    elif (chess.BB_SQUARES[square] & chess.BB_RANK_2) != 0:
                        self.moves_lookup[square, color] = move_up(bb_square) | move_2_up(bb_square) | move_up_left(bb_square) | move_up_right(bb_square)
                    else:
                        self.moves_lookup[square, color] = move_up(bb_square) | move_up_left(bb_square) | move_up_right(bb_square)
                else:
                    if (chess.BB_SQUARES[square] & chess.BB_RANK_8) != 0:
                        self.moves_lookup[square, color] = chess.BB_EMPTY
                    elif (chess.BB_SQUARES[square] & chess.BB_RANK_7) != 0:
                        self.moves_lookup[square, color] = move_down(bb_square) | move_2_down(bb_square) | move_down_left(bb_square) | move_down_right(bb_square)
                    else:
                        self.moves_lookup[square, color] = move_down(bb_square) | move_down_left(bb_square) | move_down_right(bb_square)
