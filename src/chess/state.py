import chess
from chess.board import Board

class State:

    def get_initial_state(self):
        self.board = Board()

        self.parent = None
        self.turn = chess.WHITE
        self.rook_a1_moved = False
        self.rook_h1_moved = False
        self.rook_a8_moved = False
        self.rook_h8_moved = False
        self.white_king_moved = False
        self.white_king_in_check = False
        self.white_king_checkmate = False
        self.black_king_moved = False
        self.black_king_in_check = False
        self.black_king_checkmate = False
        self.en_passant_piece_position_bb = chess.BB_EMPTY
        self.en_passant_capture_bb = chess.BB_EMPTY
        self.WHITE_OCCUPIED = chess.BB_RANK_1 | chess.BB_RANK_2
        self.BLACK_OCCUPIED = chess.BB_RANK_7 | chess.BB_RANK_8
        self.OCCUPIED = self.WHITE_OCCUPIED | self.BLACK_OCCUPIED
        # self.fen_list = [chess.STARTING_BOARD_FEN]

    
    def get_actions(self):

        # if self.turn == chess.WHITE:

        return

    def choose_action(self):
        a = "smart stuff" # Smart shit happens here
        return a

    # def apply_action(self, a: Action):
    #     # Copy self
    #     s = copy(self)
    #     #modify s
    #     s.parent = self
    #     return s