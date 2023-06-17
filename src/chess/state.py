from copy import deepcopy
import chess
from chess.board import Board
from dataclasses import dataclass
from typing import Optional, Tuple
from chess.action import Action, ActionType
from chess.utils import get_bb_from_square_int
from chess.fen_utils import FenUtils
from chess.moves.moves import MoveGenerator

@dataclass
class State:
    parent: Optional["State"]
    fen: str
    board: Board
    turn: bool
    can_castle_kingside: Tuple[bool, bool]
    can_castle_queenside: Tuple[bool, bool]
    en_passant_capture_square: chess.Bitboard  # Destination square of attacking piece
    halfmove_count: int
    move_count: int
    in_check: Tuple[bool, bool]
    in_checkmate: Tuple[bool, bool]

    def __init__(self, fen=None) -> None:
        if fen:
            self.get_state_from_fen(fen)
        else:
            self.get_state_from_fen(chess.STARTING_BOARD_FEN)

    def get_state_from_fen(self, fen_str: str):
        fen = FenUtils(fen_str)
        self.parent = self
        self.fen = fen_str
        self.board = fen.get_board(Board)
        self.turn = fen.get_player()
        self.can_castle_kingside = fen.get_can_castle_kingside()
        self.can_castle_queenside = fen.get_can_castle_queenside()
        self.en_passant_capture_square = fen.get_en_passant_capture_square()
        self.halfmove_count = fen.get_halfmove_count()
        self.move_count = fen.get_move_count()

        self.occupied_co = (self.board.black_occupied, self.board.white_occupied)

        # set player_occupied
        if self.turn == chess.WHITE:
            self.player_occupied = self.board.white_occupied
        else:
            self.player_occupied = self.board.black_occupied

        # set opponent_ocupied
        if self.turn == chess.WHITE:
            self.opponent_occupied = self.board.black_occupied
        else:
            self.opponent_occupied = self.board.white_occupied


    def get_possible_actions(self):
        """
        Generate list of actions possible in state
            Check which color is playing
            Iterate through all pieces of color
            Take index of piece and get moves lookup
            Convert possible moves to list of
        """
        move_gen = MoveGenerator(self)
        self.moves, self.attacks, self.castles, self.promotion = move_gen.get_piece_moves()

    def choose_action(self):
        '''
        Result is a state variable called self.chosen_action
        '''
        pass

    def apply_action(self, action: Action):
        new_state = deepcopy(self)
        new_state.parent = self
        new_state.board.apply_action(action)
        new_state.turn = ~self.turn
        new_state.halfmove_count = self.halfmove_count + 1
        new_state.move_count = new_state.halfmove_count // 2

        if action.piece_type == chess.KING:
            new_state.can_castle_kingside[action.player] = False
            new_state.can_castle_queenside[action.player] = False

        # Set en passant