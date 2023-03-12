from typing import Dict, Tuple
from chess.moves import Moves
from chess.pieces.piece import Piece
import chess
from chess import utils
from chess.action import Action
from chess.masking import mask_own_pieces, mask_opponent_pieces

class Rook(Piece):
    def __init__(self, bb, color, piece_type):
        super().__init__(bb, color, piece_type)
        self.generate_move_lookup()

    def generate_move_lookup(self) -> Dict[Tuple[chess.Square, chess.Color], chess.Bitboard]:
        self.moves_lookup = {}
        for square, bb_square in zip(chess.SQUARES, chess.BB_SQUARES):
            self.moves_lookup[square] = (
                utils.get_rank_from_bb(bb_square) |
                utils.get_file_from_bb(bb_square)) & ~bb_square


    def get_moves(self, opponent_occupied: chess.Bitboard, player_occupied: chess.Bitboard):
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
                moves &= ~mask_own_pieces(current_piece_position, move_range, player_occupied, mask_upwards)
                moves &= ~mask_opponent_pieces(current_piece_position, move_range, opponent_occupied, mask_upwards)


            rook_actions += Action.generate_actions(moves, chess.ROOK, current_piece_position)
            attack_actions += Action.generate_actions(moves & opponent_occupied, chess.ROOK, current_piece_position)

        return rook_actions, attack_actions
