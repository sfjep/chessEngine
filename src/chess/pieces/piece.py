from abc import ABC, abstractmethod
import chess
import chess.utils as utils
from chess.masking import mask_own_pieces, mask_opponent_pieces
from chess.action import Action, ActionType

class Piece(ABC):

    bb: chess.Bitboard
    color: bool
    piece_type: int

    def __init__(self, bb, color, piece_type):
        self.bb = bb
        self.color = color
        self.piece_type = piece_type

    def __repr__(self):
        return f"{chess.COLOR_NAMES[self.color]} {chess.PIECE_SYMBOLS[self.piece_type]}"

    @abstractmethod
    def generate_move_lookup(self):
        pass

    def get_range_moves(self, state, moves_lookup, move_ranges: list):
        actions = []
        attacks = []

        for piece_bb in utils.get_individual_ones_in_bb(self.bb):
            piece_pos_int = utils.get_square_int_from_bb(piece_bb)
            moves = moves_lookup[piece_pos_int]

            for move_range, mask_upwards in move_ranges:
                moves &= ~mask_own_pieces(piece_pos_int, move_range, state.player_occupied, mask_upwards)
                moves &= ~mask_opponent_pieces(piece_pos_int, move_range, state.opponent_occupied, mask_upwards)

            actions += Action.generate_actions(moves, self.piece_type, piece_pos_int, ActionType.MOVE)
            attacks += Action.generate_actions(moves & state.opponent_occupied, self.piece_type, piece_pos_int, ActionType.ATTACK)

        return actions, attacks

