import chess
from chess.pieces.piece import Piece
import chess
from chess.utils import get_individual_ones_in_bb, get_square_int_from_bb, get_bb_diagonals_from_square_int
from chess.action import Action, ActionType
from chess.masking import mask_own_pieces, mask_opponent_pieces

class Bishop(Piece):
    def __init__(self, bb, color, piece_type):
        super().__init__(bb, color, piece_type)
        self.generate_move_lookup()

    def generate_move_lookup(self):
        self.moves_lookup = {
            square: get_bb_diagonals_from_square_int(square)
            for square in chess.SQUARES
        }


    def get_moves(self, state):
        bishop_actions = []
        attack_actions = []
        for current_piece_bb in get_individual_ones_in_bb(self.bb):
            current_piece_position = get_square_int_from_bb(current_piece_bb)
            moves = self.moves_lookup[current_piece_position]

            move_ranges = [
                (["UP_RIGHT", "UP_LEFT"], True),
                (["DOWN_RIGHT", "DOWN_LEFT"], False)
            ]
            for move_range, mask_upwards in move_ranges:
                moves &= ~mask_own_pieces(current_piece_position, move_range, state.player_occupied, mask_upwards)
                moves &= ~mask_opponent_pieces(current_piece_position, move_range, state.opponent_occupied, mask_upwards)

            bishop_actions += Action.generate_actions(moves, chess.BISHOP, current_piece_position, ActionType.MOVE)
            attack_actions += Action.generate_actions(moves & state.opponent_occupied, chess.BISHOP, current_piece_position, ActionType.ATTACK)

        return bishop_actions, attack_actions