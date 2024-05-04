from copy import copy, deepcopy
import chess
from chess.board import Board
from dataclasses import dataclass
from typing import List, Optional
from chess.action import Action
from chess.utils import convert_rank_and_file_to_square_int, print_bitboard
from chess.fen_utils import FenUtils
from chess.moves.moves import MoveGenerator
from chess.fen import Fen
import logging
import time

#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

@dataclass
class State:
    parent: Optional["State"]
    fen: str
    board: Board
    turn: bool
    can_castle_kingside: List[bool]
    can_castle_queenside: List[bool]
    en_passant_capture_square: chess.Bitboard  # Destination square of attacking piece
    halfmove_count: int
    move_count: int
    opponent_moves: List[Action]

    def __init__(self, fen=None) -> None:
        if fen:
            self.get_state_from_fen(fen)
        else:
            self.get_state_from_fen(chess.STARTING_BOARD_FEN)
        self.opponent_moves = []
        self.is_in_check()

    def get_state_from_fen(self, fen_str: str):
        fen = FenUtils(fen_str)
        self.parent = None
        self.fen = fen_str
        self.board = fen.get_board(Board)
        self.turn = fen.get_player()
        self.can_castle_kingside = fen.get_can_castle_kingside()
        self.can_castle_queenside = fen.get_can_castle_queenside()
        self.en_passant_capture_square = fen.get_en_passant_capture_square()
        self.halfmove_count = fen.get_halfmove_count()
        self.move_count = fen.get_move_count()

    def is_in_check(self):
        if self.opponent_moves:
            if any([move.is_check for move in self.opponent_moves]):
                self.in_check[self.turn] = True
            else:
                self.in_check[self.turn] = False
        else:
            self.in_check = [False, False]
            self.opponent_moves = self.get_all_moves(not(self.turn))
            self.is_in_check()

    def is_checkmate(self):
        # TODO
        self.in_checkmate = [False, False]

    def get_legal_moves(self, color=None):
        if not color:
            color = self.turn
        all_moves = self.get_all_moves(color)
        return self.filter_suicides(all_moves)

    def get_all_moves(self, color):
        """
        Generate list of actions possible in state
            Check which color is playing
            Iterate through all pieces of color
            Take index of piece and get moves lookup
            Convert possible moves to list of Actions
        """
        move_gen = MoveGenerator(self, color)
        return move_gen.get_piece_moves()

    def filter_suicides(self, all_moves):
        legal_moves = []
        for move in all_moves:
            if str(move) == "e8d7":
                pass
            search_state = deepcopy(self)
            if not search_state.is_suicide(move):
                legal_moves.append(move)
        return legal_moves


    def choose_action(self):
        '''Result is a state variable called self.chosen_action'''
        pass

    def apply_action(self, action: Action, depth=0):
        start_time = time.time()
        logging.debug("Starting action application.")

        self.parent = deepcopy(self)

        logging.debug(f"Deepcopy of state took {time.time() - start_time:.5f} seconds.")
        intermediate_time = time.time()

        self.board.apply_action(action)
        logging.debug(f"Applying action on board took {time.time() - intermediate_time:.5f} seconds.")
        intermediate_time = time.time()

        self.increment_move_counters()
        self.en_passant_capture_square = chess.BB_EMPTY
        if action.is_two_step_pawn_move():
            self.en_passant_capture_square = action.get_en_passent_capture_square()
        self.update_castling_rights(action)
        self.turn = not self.parent.turn

        logging.debug(f"Updating state variables took {time.time() - intermediate_time:.5f} seconds.")
        intermediate_time = time.time()

        self.fen = Fen.get_fen_from_state(self)
        self.opponent_moves = []

        logging.debug(f"Getting fen took {time.time() - intermediate_time:.5f} seconds.")
        intermediate_time = time.time()


    def is_suicide(self, action):
        self.board.apply_action(action)
        return self.is_in_check()

    def update_castling_rights(self, action):
        if action.piece.type == chess.KING:
            self.can_castle_kingside[action.piece.color] = False
            self.can_castle_queenside[action.piece.color] = False

        if action.piece.type == chess.ROOK:
            if (action.origin_square == chess.A1 or action.origin_square == chess.A8):
                self.can_castle_queenside[action.piece.color] = False
            if (action.origin_square == chess.H1 or action.origin_square == chess.H8):
                self.can_castle_kingside[action.piece.color] = False

    def increment_move_counters(self):
        self.halfmove_count += 1
        self.move_count = self.halfmove_count // 2

    def undo_action(self):
        return self.parent

    def get_actions_from_origin_square(self, rank: int, file: int):
        square_int = convert_rank_and_file_to_square_int(rank, file)
        return Action.get_actions_from_origin_square(self.get_legal_moves(), square_int)