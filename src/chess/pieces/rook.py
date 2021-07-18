from chess.pieces.piece import Piece
import chess
from chess import utils

class Rook(Piece):
    def __init__(self, bb, color):
        super().__init__(bb, color)
        self.generate_move_lookup()

    def generate_move_lookup(self):
        self.moves_lookup = {}

        for square in chess.SQUARES:
            newLocation = 1 << square
            self.moves_lookup[square] = (utils.get_rank_from_bb(newLocation) | utils.get_file_from_bb(newLocation)) & ~newLocation
        