from typing import Dict, Tuple
from chess.pieces.piece import Piece
import chess

class Queen(Piece):
    def __init__(self, bb, color):
        super().__init__(bb, color)

    def generate_move_lookup() -> Dict[Tuple[chess.Square, chess.Color], chess.Bitboard]:
        return
