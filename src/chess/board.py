import chess
import chess.pieces as Pieces
from chess import Bitboard

class Board:

    def __init__(self):
        
        self.WP = Pieces.Pawn(chess.BB_RANK_2, chess.COLORS[0])
        self.WR = Pieces.Rook(chess.BB_A1 | chess.BB_H1, chess.COLORS[0])
        self.WN = Pieces.Knight(chess.BB_B1 | chess.BB_G1, chess.COLORS[0])
        self.WB = Pieces.Bishop(chess.BB_C1 | chess.BB_F1, chess.COLORS[0])
        self.WQ = Pieces.Queen(chess.BB_D1, chess.COLORS[0])
        self.WK = Pieces.King(chess.BB_E1, chess.COLORS[0])

        self.BP = Pieces.Pawn(chess.BB_RANK_7, chess.COLORS[1])
        self.BR = Pieces.Rook(chess.BB_A8 | chess.BB_H8, chess.COLORS[1])
        self.BN = Pieces.Knight(chess.BB_B8 | chess.BB_G8, chess.COLORS[1])
        self.BB = Pieces.Bishop(chess.BB_C8 | chess.BB_F8, chess.COLORS[1])
        self.BQ = Pieces.Queen(chess.BB_D8, chess.COLORS[1])
        self.BK = Pieces.King(chess.BB_E8, chess.COLORS[1])

    @staticmethod
    def piece_squares(bb_pieces: 'Bitboard'):
        """
        Generates 1 bit bitboards from the decomposition of a bitboard
        """
        while bb_pieces != 0:
            most_sig_bit = 2**(bb_pieces.bit_length()-1)
            yield most_sig_bit
            bb_pieces ^= most_sig_bit
