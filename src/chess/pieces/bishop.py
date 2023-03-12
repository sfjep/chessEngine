from typing import Dict, Tuple
import chess
from chess.moves import Moves
from chess.pieces.piece import Piece
import chess
from chess.utils import get_individual_ones_in_bb, get_square_int_from_bb
from chess.action import Action
from chess.moves import SQUARE_XRAYS
from chess.masking import mask_own_pieces, mask_opponent_pieces

class Bishop(Piece):
    def __init__(self, bb, color, piece_type):
        super().__init__(bb, color, piece_type)
        self.generate_move_lookup()

    def generate_move_lookup(self):
        self.moves_lookup = {
            square: (
                SQUARE_XRAYS[square]["UP_RIGHT"]
                | SQUARE_XRAYS[square]["UP_LEFT"]
                | SQUARE_XRAYS[square]["DOWN_RIGHT"]
                | SQUARE_XRAYS[square]["DOWN_LEFT"]
            )
            for square in chess.SQUARES
        }


    def get_moves(self, opponent_occupied: chess.Bitboard, player_occupied: chess.Bitboard):
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
                moves &= ~mask_own_pieces(current_piece_position, move_range, player_occupied, mask_upwards)
                moves &= ~mask_opponent_pieces(current_piece_position, move_range, opponent_occupied, mask_upwards)

            bishop_actions += Action.generate_actions(moves, chess.BISHOP, current_piece_position)
            attack_actions += Action.generate_actions(moves & opponent_occupied, chess.BISHOP, current_piece_position)

        return bishop_actions, attack_actions