import chess
from chess.utils import get_individual_ones_in_bb, get_square_int_from_bb

from dataclasses import dataclass

@dataclass
class Action:
    piece_type: int
    origin_square: int
    new_square: int

    def __repr__(self):
        return f"""\nAction({chess.PIECE_SYMBOLS[self.piece_type]} {chess.SQUARE_NAMES[self.origin_square]} - {chess.SQUARE_NAMES[self.new_square]})"""

    @staticmethod
    def generate_actions(moves: chess.Bitboard, piece_type: int, current_square: int):
        """
        Params
            moves : bitboard containing destination squares of the piece to move the
            piece_type : piece type int
            current_piece_position : bitboard containint current position of piece to move
        Returns:
            A list of 'Action' instances representing each source and destination square for piece to move.
        """
        return [
            Action(
                piece_type,
                current_square,
                get_square_int_from_bb(new_piece_position),
            )
            for new_piece_position in get_individual_ones_in_bb(moves)
        ]