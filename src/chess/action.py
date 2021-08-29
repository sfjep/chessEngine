import chess
from chess.utils import get_individual_ones_in_bb, get_square_int_from_bb

from dataclasses import dataclass

@dataclass
class Action:
    piece_type: int
    origin_square: int
    new_square: int

    @staticmethod
    def generate_actions(moves: chess.Bitboard, piece_type: int, current_piece_position: chess.Bitboard):
        actions = []
        for new_piece_position in get_individual_ones_in_bb(moves):
            actions.append(
                Action(
                    piece_type, 
                    get_square_int_from_bb(current_piece_position), 
                    get_square_int_from_bb(new_piece_position)
                )
            )
        return actions