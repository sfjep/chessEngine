from dataclasses import dataclass
from enum import Enum
from typing import Optional

import chess
from chess.pieces.piece import Piece
from chess.utils import get_individual_ones_in_bb, get_square_int_from_bb, get_square_notation


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
    promotion_to: Optional[Piece]
    is_long_castles: Optional[bool]
    is_check: Optional[bool]
    is_checkmate: Optional[bool]

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__ and self.__repr__() == other.__repr__()
        else:
            return False

    def __repr__(self):
        if self.type == ActionType.CASTLING:
            return "O-O-O" if self.is_long_castles else "O-O"
        piece = chess.PIECE_SYMBOLS[self.piece_type].upper()
        start = get_square_notation(self.origin_square)
        captures = "x" if self.type in [ActionType.ATTACK, ActionType.EN_PASSANT] else ""
        end = get_square_notation(self.destination_square)
        promotion_to = f"/{chess.PIECE_SYMBOLS[self.promotion_to].upper()}" if self.type == ActionType.PROMOTION else ""
        check = "+" if self.is_check and not self.is_checkmate else ""
        checkmate = "#" if self.is_checkmate else ""
        return f"{piece}{start}{captures}{end}{promotion_to}{check}{checkmate}"

    @staticmethod
    def generate_actions(moves: chess.Bitboard, piece: Piece, origin_square: int, action_type: ActionType, **kwargs):
        """
        Params
            moves : bitboard containing destination squares of the piece to move
            piece : piece object
            origin_square : bitboard containint current position of piece to move
            action_type : type of action (move, attack, promotion)
            kwargs:
                promotion_to: pawn promotes to this piece type
                is_long_castles: True if long castles (queenside), False if short castles (kingside)
                is_check: True if this action puts the king in check
                is_checkmate: True if this action is a checkmate
        Returns:
            A list of 'Action' instances representing each source and destination square for piece to move.
        """

        return [
            Action(
                piece_type=piece.type,
                origin_square=origin_square,
                destination_square=get_square_int_from_bb(new_piece_position),
                player=piece.color,
                type=action_type,
                promotion_to=kwargs.get("promotion_to", None),
                is_long_castles=kwargs.get("is_long_castles", None),
                is_check=kwargs.get("is_check", None),
                is_checkmate=kwargs.get("is_checkmate", None)
            )
            for new_piece_position in get_individual_ones_in_bb(moves)
        ]


