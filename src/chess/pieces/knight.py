from typing import Dict
from chess.moves import Moves
from chess.pieces.piece import Piece
import chess
from chess.utils import get_individual_ones_in_bb, get_square_int_from_bb
from chess.action import Action

class Knight(Piece):
    def __init__(self, bb, color, piece_type):
        super().__init__(bb, color, piece_type)

    def generate_move_lookup() -> Dict[chess.Square, chess.Bitboard]:
        moves_lookup = {}        
        for square, bb_square in zip(chess.SQUARES, chess.BB_SQUARES):
            new_square = 0
            new_square += Moves.move_2_down_1_left(bb_square)
            new_square += Moves.move_2_down_1_right(bb_square)
            new_square += Moves.move_2_up_1_left(bb_square)
            new_square += Moves.move_2_up_1_right(bb_square)
            new_square += Moves.move_2_left_1_up(bb_square)
            new_square += Moves.move_2_left_1_down(bb_square)
            new_square += Moves.move_2_right_1_up(bb_square)
            new_square += Moves.move_2_right_1_down(bb_square)

            moves_lookup[square] = new_square
        
        return moves_lookup
    
    MOVES_LOOKUP = generate_move_lookup()

    def get_moves(self, opponent_occupied: chess.Bitboard, player_occupied: chess.Bitboard):
        knight_actions = []
        attack_actions = []
        
        for current_piece_position in get_individual_ones_in_bb(self.bb):
            sq = get_square_int_from_bb(current_piece_position)
            target_moves = self.moves_lookup[sq] & ~player_occupied
            attack_moves = self.moves_lookup[sq] & ~player_occupied & opponent_occupied

            knight_actions += Action.generate_actions(target_moves, chess.KNIGHT, current_piece_position)
            attack_actions += Action.generate_actions(attack_moves, chess.KNIGHT, current_piece_position)

        return knight_actions, attack_actions


                
    
