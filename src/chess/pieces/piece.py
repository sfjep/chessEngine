from abc import ABC, abstractmethod
import chess

class Piece(ABC):

    bb: chess.Bitboard
    color: bool
    piece_type: int

    def __init__(self, bb, color, piece_type):
        self.bb = bb
        self.color = color
        self.piece_type = piece_type

    @abstractmethod
    def generate_move_lookup(self):
        pass
