from chess.pieces.piece import Piece
import chess
from chess import utils
from chess.action import Action, ActionType
from chess.masking import mask_own_pieces, mask_opponent_pieces

class Rook(Piece):
    def __init__(self, bb, color, piece_type):
        super().__init__(bb, color, piece_type)
        self.generate_move_lookup()

    def generate_move_lookup(self):
        self.moves_lookup = {}
        for square, bb_square in zip(chess.SQUARES, chess.BB_SQUARES):
            self.moves_lookup[square] = (
                utils.get_rank_from_bb(bb_square) |
                utils.get_file_from_bb(bb_square)) & ~bb_square


    def get_moves(self, state):
        rook_actions = []
        attack_actions = []
        for current_piece_bb in utils.get_individual_ones_in_bb(self.bb):
            current_piece_position = utils.get_square_int_from_bb(current_piece_bb)
            moves = self.moves_lookup[current_piece_position]

            move_ranges = [
                (["UP", "RIGHT"], True),
                (["LEFT", "DOWN"], False)
            ]
            for move_range, mask_upwards in move_ranges:
                moves &= ~mask_own_pieces(current_piece_position, move_range, state.player_occupied, mask_upwards)
                moves &= ~mask_opponent_pieces(current_piece_position, move_range, state.opponent_occupied, mask_upwards)


            rook_actions += Action.generate_actions(moves, chess.ROOK, current_piece_position, ActionType.MOVE)
            attack_actions += Action.generate_actions(moves & state.opponent_occupied, chess.ROOK, current_piece_position, ActionType.ATTACK)

        return rook_actions, attack_actions
