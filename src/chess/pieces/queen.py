from typing import Dict, Tuple
import chess
from chess.moves import Moves
from chess.pieces.piece import Piece
from chess import utils


class Queen(Piece):
    def __init__(self, bb, color):
        super().__init__(bb, color)

    def generate_move_lookup() -> Dict[Tuple[chess.Square, chess.Color], chess.Bitboard]:
        moves_lookup = {}

        for square, bb_square in zip(chess.SQUARES, chess.BB_SQUARES):
            moves_lookup[square] = (
                ((utils.get_rank_from_bb(bb_square) | utils.get_file_from_bb(bb_square)) & ~bb_square) |
                Moves.move_down_left_diagonal(bb_square) |
                Moves.move_down_right_diagonal(bb_square) |
                Moves.move_up_left_diagonal(bb_square) |
                Moves.move_up_right_diagonal(bb_square) 
            )

        return moves_lookup

    moves_lookup = generate_move_lookup()
