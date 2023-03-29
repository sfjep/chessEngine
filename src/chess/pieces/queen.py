from typing import Dict, Tuple
import chess
from chess.moves import MoveUtils
from chess.pieces.piece import Piece
import chess.utils as utils
from chess.action import Action
from chess.moves import SQUARE_XRAYS
from chess.masking import mask_own_pieces, mask_opponent_pieces

class Queen(Piece):
    def __init__(self, bb, color, piece_type):
        super().__init__(bb, color, piece_type)
        self.generate_move_lookup()

    def generate_move_lookup(self):
        self.moves_lookup = {}
        for square, bb_square in zip(chess.SQUARES, chess.BB_SQUARES):
            self.moves_lookup[square] = (
                ((utils.get_rank_from_bb(bb_square) | utils.get_file_from_bb(bb_square)) & ~bb_square) |
                utils.get_bb_diagonals_from_square_int(square)
            )


    def get_moves(self, state):
        queen_actions = []
        attack_actions = []

        # Positions of each individual piece among pieces of this piece type/color

        for current_piece_bb in utils.get_individual_ones_in_bb(self.bb):
            current_piece_position = utils.get_square_int_from_bb(current_piece_bb)
            moves = self.moves_lookup[current_piece_position]

            move_ranges = [
                (["UP_RIGHT", "RIGHT", "UP", "UP_LEFT"], True),
                (["DOWN_RIGHT", "DOWN", "LEFT", "DOWN_LEFT"], False)
            ]
            for move_range, mask_upwards in move_ranges:
                moves &= ~mask_own_pieces(current_piece_position, move_range, state.player_occupied, mask_upwards)
                moves &= ~mask_opponent_pieces(current_piece_position, move_range, state.opponent_occupied, mask_upwards)


            queen_actions += Action.generate_actions(moves, chess.QUEEN, current_piece_position)
            attack_actions += Action.generate_actions(moves & state.opponent_occupied, chess.QUEEN, current_piece_position)

        return queen_actions, attack_actions

