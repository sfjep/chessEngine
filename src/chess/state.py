import numpy as np
import chess
from chess.board import Board
from dataclasses import dataclass

@dataclass
class State:
    board: Board
    parent: Optional['State']
    turn: bool
    white_can_castle_kingside: bool
    white_can_castle_queenside: bool
    black_can_castle_kingside: bool
    black_can_castle_queenside: bool
    white_king_in_check: bool
    white_king_checkmate: bool
    black_king_in_check: bool
    black_king_checkmate: bool
    en_passant_pawn_position: chess.Bitboard
    en_passant_capture_square: chess.Bitboard
    halfmove_count: int
    move_count: int

    def __init__(self, fen=None) -> None:
        if fen:
            self.get_state_from_fen(fen)
        else:
            self.get_initial_state()


    def get_initial_state(self):
        self.board = Board()

        self.parent = None
        self.turn = chess.WHITE

        self.white_can_castle_kingside = False
        self.white_can_castle_queenside = False
        self.black_can_castle_kingside = False
        self.black_can_castle_queenside = False

        self.white_king_in_check = False
        self.white_king_checkmate = False
        self.black_king_in_check = False
        self.black_king_checkmate = False
        self.en_passant_pawn_position = chess.BB_EMPTY
        self.en_passant_capture_square = chess.BB_EMPTY
        self.halfmove_count = 0
        self.move_count = 0
        # self.fen_list = [chess.STARTING_BOARD_FEN]

    def get_fen_from_state(self):
        fen = self._get_board_fen() + " "
        fen += self._get_turn_fen() + " "
        fen += self._get_castling_fen() + " "
        fen += self._get_en_passant_fen() + " "
        fen += self._get_halfmove_count_fen() + " "
        fen += self._get_move_count_fen()
        return fen

    def _get_turn_fen(self):
        if self.turn:
            return "w"
        else:
            return "b"

    def _get_castling_fen(self):
        fen = ''
        if self.white_can_castle_kingside:
            fen += "K"
        if self.white_can_castle_queenside:
            fen += "Q"
        if self.black_can_castle_kingside:
            fen += "k"
        if self.black_can_castle_queenside:
            fen += "q"
        if len(fen) == 0:
            fen += "-"
        return fen      

    def _get_en_passant_fen(self):
        if self.en_passant_capture_square == chess.BB_EMPTY:
            return "-"
        else:
            return chess.SQUARE_NAMES[chess.BB_SQUARES.index(self.en_passant_capture_square)]

    def _get_halfmove_count_fen(self):
        return str(self.halfmove_count)
    
    def _get_move_count_fen(self):
        return str(self.move_count)

    def get_state_from_fen(self, fen: str):
        fields = fen.split()
        fen_board = fields[0]
        player = fields[1]
        castling_rights = fields[2]
        en_passant = fields[3]
        halfmove_clock = fields[4]
        fullmove_number = fields[5]

        self.board = Board(fen_board)
        self.turn = player == "w"

        self.white_can_castle_kingside = "K" in castling_rights
        self.white_can_castle_queenside = "Q" in castling_rights
        self.black_can_castle_kingside = "k" in castling_rights
        self.black_can_castle_queenside = "q" in castling_rights

        if en_passant != "-":
            self.en_passant_capture_square = chess.BB_SQUARES[chess.SQUARE_NAMES.index(en_passant)]
        else:
            self.en_passant_capture_square = chess.BB_EMPTY

        self.halfmove_count = int(halfmove_clock)
        self.move_count = int(fullmove_number)

    def _get_board_fen(self):
        board_arr = np.flip(self.board.get_board_arr_from_board_obj(self.board), axis=0)
        fen = ''
        for i in range(board_arr.shape[0]):
            empty_count = 0
            for j in range(board_arr.shape[1]):
                if board_arr[i, j] == ' ':
                    empty_count += 1
                else:
                    if empty_count == 0:
                        fen += chess.UNICODE_SYMBOL_TO_CHAR[board_arr[i, j]]
                    else:
                        fen += str(empty_count)
                        fen += chess.UNICODE_SYMBOL_TO_CHAR[board_arr[i, j]]
                        empty_count = 0
            if empty_count != 0:
                fen += str(empty_count)
            if i != (board_arr.shape[0] - 1):
                fen += "/"
        return fen