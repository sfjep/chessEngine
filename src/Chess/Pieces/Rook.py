from chess.pieces.piece import Piece
import chess
from chess import utils

class Rook(Piece):
    def __init__(self, bb, color):
        super().__init__(bb, color)
        self.getMovesLookupDict()

    def getMovesLookupDict(self):
        self.moves_lookup = {}

        for square in chess.SQUARES:
            newLocation = 1 << square
            self.moves_lookup[square] = (utils.getRankFromBB(newLocation) | utils.getFileFromBB(newLocation)) & ~newLocation
        