import numpy as np

import chess

class Fen:

    @classmethod
    def get_fen_from_state(cls, state):
        fen = cls._get_board_fen(state) + " "
        fen += cls._get_turn_fen(state) + " "
        fen += cls._get_castling_fen(state) + " "
        fen += cls._get_en_passant_fen(state) + " "
        fen += cls._get_halfmove_count_fen(state) + " "
        fen += cls._get_move_count_fen(state)
        return fen


    @staticmethod
    def _get_board_fen(state):
        board_arr = state.board.board_arr
        fen = ''
        for i in range(board_arr.shape[0]):
            empty_count = 0
            for j in range(board_arr.shape[1]):
                if board_arr[i, j] == ' ':
                    empty_count += 1
                else:
                    if empty_count != 0:
                        fen += str(empty_count)
                        empty_count = 0
                    fen += chess.PIECE_STRING_TO_CHAR[board_arr[i, j]]
            if empty_count != 0:
                fen += str(empty_count)
            if i != (board_arr.shape[0] - 1):
                fen += "/"
        return fen


    @staticmethod
    def _get_turn_fen(state):
        return "w" if state.turn else "b"

    @staticmethod
    def _get_castling_fen(state):
        fen = ''
        if state.can_castle_kingside[chess.WHITE]:
            fen += "K"
        if state.can_castle_queenside[chess.WHITE]:
            fen += "Q"
        if state.can_castle_kingside[chess.BLACK]:
            fen += "k"
        if state.can_castle_queenside[chess.BLACK]:
            fen += "q"
        if len(fen) == 0:
            fen += "-"
        return fen

    @staticmethod
    def _get_en_passant_fen(state):
        if state.en_passant_capture_square == chess.BB_EMPTY:
            return "-"
        else:
            return chess.SQUARE_NAMES[chess.BB_SQUARES.index(state.en_passant_capture_square)]

    @staticmethod
    def _get_halfmove_count_fen(state):
        return str(state.halfmove_count)

    @staticmethod
    def _get_move_count_fen(state):
        return str(state.move_count)

