import chess
import chess.pieces as Pieces
from chess import Bitboard

class Board:

    def __init__(self, fen_board:str=None):
        self.WP = Pieces.Pawn(chess.BB_EMPTY, chess.WHITE, chess.PAWN)
        self.WR = Pieces.Rook(chess.BB_EMPTY, chess.WHITE, chess.ROOK)
        self.WN = Pieces.Knight(chess.BB_EMPTY, chess.WHITE, chess.KNIGHT)
        self.WB = Pieces.Bishop(chess.BB_EMPTY, chess.WHITE, chess.BISHOP)
        self.WQ = Pieces.Queen(chess.BB_EMPTY, chess.WHITE, chess.QUEEN)
        self.WK = Pieces.King(chess.BB_EMPTY, chess.WHITE, chess.KING)

        self.BP = Pieces.Pawn(chess.BB_EMPTY, chess.BLACK, chess.PAWN)
        self.BR = Pieces.Rook(chess.BB_EMPTY, chess.BLACK, chess.ROOK)
        self.BN = Pieces.Knight(chess.BB_EMPTY, chess.BLACK, chess.KNIGHT)
        self.BB = Pieces.Bishop(chess.BB_EMPTY, chess.BLACK, chess.BISHOP)
        self.BQ = Pieces.Queen(chess.BB_EMPTY, chess.BLACK, chess.QUEEN)
        self.BK = Pieces.King(chess.BB_EMPTY, chess.BLACK, chess.KING)

        self.white_pieces = [self.WP, self.WR, self.WB, self.WN, self.WQ, self.WK]
        self.black_pieces = [self.BP, self.BR, self.BB, self.BN, self.BQ, self.BK]
        self.pieces = self.white_pieces + self.black_pieces

        if not fen_board: # starting board from initial game position
            self.WP.bb = chess.BB_RANK_2
            self.WR.bb = chess.BB_A1 | chess.BB_H1
            self.WN.bb = chess.BB_B1 | chess.BB_G1
            self.WB.bb = chess.BB_C1 | chess.BB_F1
            self.WQ.bb = chess.BB_D1
            self.WK.bb = chess.BB_E1

            self.BP.bb = chess.BB_RANK_7
            self.BN.bb = chess.BB_B8 | chess.BB_G8
            self.BR.bb = chess.BB_A8 | chess.BB_H8
            self.BB.bb = chess.BB_C8 | chess.BB_F8
            self.BQ.bb = chess.BB_D8
            self.BK.bb = chess.BB_E8

    @staticmethod
    def piece_squares(bb_pieces: Bitboard):
        """
        Generates 1 bit bitboards from the decomposition of a bitboard
        """
        while bb_pieces != 0:
            most_sig_bit = 2**(bb_pieces.bit_length()-1)
            yield most_sig_bit
            bb_pieces ^= most_sig_bit
