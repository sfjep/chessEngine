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
    in_check: List[bool]
    in_checkmate: List[bool]
    valid_moves: List[Action]
    opponent_moves: List[Action]

    def __init__(self, fen=None) -> None:
        if fen:
            self.get_state_from_fen(fen)
        else:
            self.get_state_from_fen(chess.STARTING_BOARD_FEN)
        self.opponent_moves = []
        self.is_in_check()
        self.opponent_moves = self.get_possible_actions(not(self.turn))
        self.is_checkmate()
        self.valid_moves = self.get_possible_actions(self.turn)

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
        self.king_bb = [self.board.BK.bb, self.board.WK.bb]

        self.occupied_co = (self.board.black_occupied, self.board.white_occupied)

        # set player_occupied
        if self.turn == chess.WHITE:
            self.player_occupied = self.board.white_occupied
            self.opponent_occupied = self.board.black_occupied
        else:
            self.player_occupied = self.board.black_occupied
            self.opponent_occupied = self.board.white_occupied

    def is_in_check(self):
        if self.opponent_moves:
            if any([move.is_check for move in self.opponent_moves]):
                self.in_check[self.turn] = True
            else:
                self.in_check[self.turn] = False
        else:
            self.in_check = [False, False]
            self.opponent_moves = self.get_possible_actions(not(self.turn))
            self.is_in_check()

    def is_checkmate(self):
        # TODO
        self.in_checkmate = [False, False]

    def get_possible_actions(self, color):
        """
        Generate list of actions possible in state
            Check which color is playing
            Iterate through all pieces of color
            Take index of piece and get moves lookup
            Convert possible moves to list of Actions
        """
        move_gen = MoveGenerator(self, color)
        self.moves = move_gen.get_piece_moves()
        return self.moves

    def choose_action(self):
        '''
        Result is a state variable called self.chosen_action
        '''
        pass

    def apply_action(self, action: Action, depth=0):
        print(f"Applying action {action} with depth {depth}")
        new_state = self
        new_state.parent = deepcopy(self)

        new_state.board.apply_action(action)

        new_state.increment_move_counters()
        new_state.en_passant_capture_square = chess.BB_EMPTY
        new_state.update_castling_rights(action)

        new_state.turn = not new_state.parent.turn

        new_state.set_opponent_moves()
        new_state.is_in_check()

        if action.is_two_step_pawn_move():
            new_state.en_passant_capture_square = action.get_en_passent_capture_square()

        new_state.fen = Fen.get_fen_from_state(new_state)

        if depth == 0:
            new_state.valid_moves = new_state.get_possible_actions(new_state.turn)

            deep_copies = dict()
            # remove moves that put me in check in the next state
            for count, move in enumerate(new_state.valid_moves):
                search_state = deepcopy(self)
                deep_copies[count] = id(search_state.board)
                if search_state.is_reveal_check_move(move):
                    assert move in new_state.valid_moves
                    new_state.valid_moves.remove(move)
                    assert move not in new_state.valid_moves

        return new_state


    def is_reveal_check_move(self, action):
        self.board.apply_action(action)
        self.set_opponent_moves()
        self.is_in_check()
        return self.in_check[self.turn]

    def set_opponent_moves(self):
        self.opponent_moves = self.get_possible_actions(not self.turn)


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
        return Action.get_actions_from_origin_square(self.valid_moves, square_int)