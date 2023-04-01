from enum import Enum
import chess
from chess.utils import get_individual_ones_in_bb, get_square_int_from_bb

from dataclasses import dataclass


class ActionType(Enum):
    MOVE = 0
    EN_PASSANT = 1
    ATTACK = 2
    PROMOTION = 3

@dataclass
class Action:
    piece_type: int
    origin_square: int
    destination_square: int
    player: chess.Color
    type: ActionType

    def __repr__(self):
        return f"""\nAction({chess.PIECE_SYMBOLS[self.piece_type]} {chess.SQUARE_NAMES[self.origin_square]} - {chess.SQUARE_NAMES[self.destination_square]})"""

    @staticmethod
    def generate_actions(moves: chess.Bitboard, piece_type: int, current_square: int, player: chess.Color, type: ActionType):
        """
        Params
            moves : bitboard containing destination squares of the piece to move
            piece_type : piece type int
            current_piece_position : bitboard containint current position of piece to move
            player: player performing the action
            action_type : type of action (move, attack, promotion)
        Returns:
            A list of 'Action' instances representing each source and destination square for piece to move.
        """
        return [
            Action(
                piece_type,
                current_square,
                get_square_int_from_bb(new_piece_position),
                player,
                type
            )
            for new_piece_position in get_individual_ones_in_bb(moves)
        ]
