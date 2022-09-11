import chess
from chess.board import Board
from dataclasses import dataclass
from typing import Optional


@dataclass
class State:
    parent: Optional["State"]
    fen: str
    board: Board
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
    en_passant_capture_square: chess.Bitboard  # Destination square of attacking piece
    halfmove_count: int
    move_count: int

    def __init__(self, fen=None) -> None:
        if fen:
            self.get_state_from_fen(fen)
        else:
            self.get_state_from_fen(chess.STARTING_BOARD_FEN)

    def get_state_from_fen(self, fen: str):
        fields = fen.split()
        fen_board = fields[0]
        player = fields[1]
        castling_rights = fields[2]
        en_passant = fields[3]
        halfmove_clock = fields[4]
        fullmove_number = fields[5]

        self.fen = fen
        self.board = Board(fen_board)
        self.turn = player == "w"

        self.white_can_castle_kingside = "K" in castling_rights
        self.white_can_castle_queenside = "Q" in castling_rights
        self.black_can_castle_kingside = "k" in castling_rights
        self.black_can_castle_queenside = "q" in castling_rights

        if en_passant != "-":
            self.en_passant_capture_square = chess.BB_SQUARES[
                chess.SQUARE_NAMES.index(en_passant)
            ]
        else:
            self.en_passant_capture_square = chess.BB_EMPTY

        self.halfmove_count = int(halfmove_clock)
        self.move_count = int(fullmove_number)

    def get_possible_actions(self):
        """
        Generate list of actions possible in state
            Check which color is playing
            Iterate through all pieces of color
            Take index of piece and get moves lookup
            Convert possible moves to list of
        """
        possible_actions = []
        if self.turn == chess.WHITE:
            for piece in self.board_white_pieces:  # HECK
                if piece.piece_type == chess.PAWN:
                    moves, attacks = piece.get_moves(
                        chess.WHTIE,
                        self.board.black_occupied,
                        self.board.white_occupied,
                        self.en_passant_capture_square,
                    )
                elif piece.piece_type == chess.KING:
                    moves, attacks = piece.get_moves(
                        chess.WHITE,

                    )
                else:
                    moves, attacks = piece.get_moves(
                        self.board.white_occupied, self.board.black_occupied
                    )
                possible_actions.append(moves)
        else:
            for piece in self.board_black_pieces:
                if piece.piece_type == chess.PAWN:
                    moves, attacks = piece.get_moves(
                        chess.BLACK,
                        self.board.black_occupied,
                        self.board.white_occupied,
                        self.en_passant_capture_square,
                    )
                else:
                    moves, attacks = piece.get_moves(
                        self.board.black_occupied, self.board.white_occupied
                    )
                possible_actions.append(moves)
