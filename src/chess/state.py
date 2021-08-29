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
