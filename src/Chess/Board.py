import Chess
import Chess.pieces as Pieces

# from globalImport import *

class Board:

    def __init__(self):
        
        self.whitePawns = Pieces.Pawn(Chess.BB_RANK_2, Chess.COLORS[0])
        self.whiteKnights = Pieces.Knight(Chess.BB_B1 | Chess.BB_G1, Chess.COLORS[0])
        self.whiteBishops = Pieces.Bishop(Chess.BB_C1 | Chess.BB_F1, Chess.COLORS[0])
        self.whiteRooks = Pieces.Rook(Chess.BB_A1 | Chess.BB_H1, Chess.COLORS[0])
        self.whiteQueen = Pieces.Queen(Chess.BB_D1, Chess.COLORS[0])
        self.whiteKing = Pieces.Rook(Chess.BB_E1, Chess.COLORS[0])

        self.blackPawns = Pieces.Pawn(Chess.BB_RANK_7, Chess.COLORS[1])
        self.blackKnights = Pieces.Knight(Chess.BB_B8 | Chess.BB_G8, Chess.COLORS[1])
        self.blackBishops = Pieces.Bishop(Chess.BB_C8 | Chess.BB_F8, Chess.COLORS[1])
        self.blackRooks = Pieces.Rook(Chess.BB_A8 | Chess.BB_H8, Chess.COLORS[1])
        self.blackQueen = Pieces.Queen(Chess.BB_D8, Chess.COLORS[1])
        self.blackKing = Pieces.Queen(Chess.BB_E8, Chess.COLORS[1])


