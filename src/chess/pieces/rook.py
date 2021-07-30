from typing import Dict, Tuple
from chess.moves import Moves
from chess.pieces.piece import Piece
import chess
from chess import utils

class Rook(Piece):
    def __init__(self, bb, color, piece_type):
        super().__init__(bb, color, piece_type)

    def generate_move_lookup() -> Dict[Tuple[chess.Square, chess.Color], chess.Bitboard]:
        moves_lookup = {}

        for square, bb_square in zip(chess.SQUARES, chess.BB_SQUARES):
            moves_lookup[square] = (
                utils.get_rank_from_bb(bb_square) | 
                utils.get_file_from_bb(bb_square)) & ~bb_square
        
        return moves_lookup

    moves_lookup = generate_move_lookup()
        
    def get_moves(self, opponent_occupied: chess.Bitboard, player_occupied: chess.Bitboard):
        rook_actions = {}
        attack_actions = {}
        for current_piece_position in utils.get_individual_ones_in_bb(self.bb):
            target_moves = chess.BB_EMPTY
            attack_moves = chess.BB_EMPTY
            move_generator = [
                Moves.move_up,
                Moves.move_down,
                Moves.move_left,
                Moves.move_right 
            ]
            for next_move in move_generator:
                continue_in_direction = True
                next_square = current_piece_position
                while continue_in_direction:
                    next_square = next_move(next_square)
                    if not next_square & chess.BB_ALL:
                        continue_in_direction = False
                    elif next_square & player_occupied:
                        continue_in_direction = False
                    else:
                        target_moves |= next_square
                        if target_moves & opponent_occupied:
                            attack_moves |= next_square
                            continue_in_direction = False

            rook_actions[current_piece_position] = target_moves
            attack_actions[current_piece_position] = attack_moves

        return rook_actions, attack_actions
