from dataclasses import dataclass
from enum import Enum

import chess
from chess.pieces.piece import Piece
from chess.utils import get_individual_ones_in_bb, get_square_int_from_bb



class ActionType(Enum):
    MOVE = 0
    EN_PASSANT = 1
    ATTACK = 2
    PROMOTION = 3
    CASTLING = 4

@dataclass
class Action:
    piece_type: int
    origin_square: int
    destination_square: int
    player: chess.Color
    type: ActionType

    def __repr__(self):
        return f"""\nAction({self.type} - {chess.PIECE_SYMBOLS[self.piece_type]} {chess.SQUARE_NAMES[self.origin_square]} - {chess.SQUARE_NAMES[self.destination_square]})"""

    @staticmethod
    def generate_actions(moves: chess.Bitboard, piece: Piece, origin_square: int, type: ActionType):
        """
        Params
            moves : bitboard containing destination squares of the piece to move
            piece : piece object
            origin_square : bitboard containint current position of piece to move
            action_type : type of action (move, attack, promotion)
        Returns:
            A list of 'Action' instances representing each source and destination square for piece to move.
        """
        return [
            Action(
                piece.type,
                origin_square,
                get_square_int_from_bb(new_piece_position),
                piece.color,
                type
            )
            for new_piece_position in get_individual_ones_in_bb(moves)
        ]
