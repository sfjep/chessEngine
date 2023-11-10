from abc import ABC, abstractmethod
import chess
from chess.utils import typename

class Piece(ABC):

    bb: chess.Bitboard
    color: bool
    type: int

    def __init__(self, bb, color, piece_type):
        self.bb = bb
        self.color = color
        self.type = piece_type


    def __repr__(self):
        return f"{typename(self)}(bb={self.bb}, color={self.color}, piece_type={self.type})"

    def __str__(self):
        return f"{chess.PIECE_SYMBOLS[self.type]}"

    @abstractmethod
    def generate_move_lookup(self):
        pass

