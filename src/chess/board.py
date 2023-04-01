import numpy as np
import chess
import chess.pieces as Pieces
from chess import Bitboard
from chess.utils import get_individual_ones_in_bb, get_square_int_from_bb
from chess.pieces.piece import Piece

class Board:
    WP: Piece
    WR: Piece
    WN: Piece
    WB: Piece
    WQ: Piece
    WK: Piece
    BP: Piece
    BR: Piece
    BN: Piece
    BB: Piece
    BQ: Piece
    BK: Piece

    white_occupied: chess.Bitboard
    black_occupied: chess.Bitboard
    all_occupied: chess.Bitboard
    white_pieces: list
    black_pieces: list
    pieces: list

    def __init__(self, fen_board: str = None):
        self._create_pieces()

        if not fen_board:
            self._set_board_to_start_position()
        else:
            self._set_board_from_fen(fen_board)

        self._set_helper_bitboard()
        self._get_board_chararray()

    def _create_pieces(self):
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

    def _set_board_to_start_position(self):
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


    def _set_board_from_fen(self, fen_board: str):
        char_to_piece = {
            "P": self.WP,
            "R": self.WR,
            "N": self.WN,
            "B": self.WB,
            "Q": self.WQ,
            "K": self.WK,
            "p": self.BP,
            "r": self.BR,
            "n": self.BN,
            "b": self.BB,
            "q": self.BQ,
            "k": self.BK,
        }
        fen = fen_board.split("/")
        if len(fen) != 8:
            raise InvalidFenException
        blank_spaces = "1234567"
        # enumerating ranks from 7 to 0, as fen starts from black to white
        for rank, rank_content in zip(range(7, -1, -1), fen):
            if rank_content != "8":
                file_count = 0
                for char in rank_content:
                    if char in blank_spaces:
                        file_count += int(char)
                    else:
                        char_to_piece[char].bb |= chess.BB_SQUARES[
                            rank * 8 + file_count
                        ]
                        file_count += 1
                    if file_count > 8:
                        raise InvalidFenException

    def _set_helper_bitboard(self):
        self.white_occupied = (
            self.WP.bb | self.WR.bb | self.WB.bb | self.WN.bb | self.WQ.bb | self.WK.bb
        )
        self.black_occupied = (
            self.BP.bb | self.BR.bb | self.BB.bb | self.BN.bb | self.BQ.bb | self.BK.bb
        )
        self.all_occupied = self.white_occupied | self.black_occupied
        self.white_pieces = [self.WP, self.WR, self.WB, self.WN, self.WQ, self.WK]
        self.black_pieces = [self.BP, self.BR, self.BB, self.BN, self.BQ, self.BK]
        self.pieces = self.white_pieces + self.black_pieces


    @staticmethod
    def piece_squares(bb_pieces: Bitboard):
        """
        Generates 1 bit bitboards from the decomposition of a bitboard
        """
        while bb_pieces != 0:
            most_sig_bit = 2 ** (bb_pieces.bit_length() - 1)
            yield most_sig_bit
            bb_pieces ^= most_sig_bit

    def _get_board_chararray(self):
        self.board_arr = np.full([8, 8], " ", dtype=object)
        for piece in self.pieces:
            for bb in get_individual_ones_in_bb(piece.bb):
                idx = get_square_int_from_bb(bb)
                if piece.color == chess.WHITE:
                    self.board_arr[idx // 8, idx % 8] = f"W{chess.PIECE_SYMBOLS[piece.piece_type].upper()}"
                else:
                    self.board_arr[idx // 8, idx % 8] = f"B{chess.PIECE_SYMBOLS[piece.piece_type].upper()}"
        self.board_arr = np.flip(self.board_arr, axis=0)

    def get_piece_name_from_board_dim(self, row: int, column: int):
        return self.board_arr[row][column]

    def square_has_piece(self, row: int, column: int):
        return self.board_arr[row][column] != " "

class InvalidFenException(Exception):
    pass
