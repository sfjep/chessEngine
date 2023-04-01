from chess.moves.move_utils import MoveUtils
from chess.pieces.piece import Piece
import chess
from chess.utils import get_individual_ones_in_bb, get_square_int_from_bb
from chess.action import Action, ActionType

class Knight(Piece):
    def __init__(self, bb, color, piece_type):
        super().__init__(bb, color, piece_type)
        self.generate_move_lookup()

    def generate_move_lookup(self):
        self.moves_lookup = {}
        for square, bb_square in zip(chess.SQUARES, chess.BB_SQUARES):
            new_square = 0
            new_square += MoveUtils.move_2_down_1_left(bb_square)
            new_square += MoveUtils.move_2_down_1_right(bb_square)
            new_square += MoveUtils.move_2_up_1_left(bb_square)
            new_square += MoveUtils.move_2_up_1_right(bb_square)
            new_square += MoveUtils.move_2_left_1_up(bb_square)
            new_square += MoveUtils.move_2_left_1_down(bb_square)
            new_square += MoveUtils.move_2_right_1_up(bb_square)
            new_square += MoveUtils.move_2_right_1_down(bb_square)
            self.moves_lookup[square] = new_square


    def get_moves(self, state):
        knight_actions = []
        attack_actions = []

        for piece_bb in get_individual_ones_in_bb(self.bb):
            sq = get_square_int_from_bb(piece_bb)
            moves = self.moves_lookup[sq] & ~state.player_occupied
            attack_moves = self.moves_lookup[sq] & ~state.player_occupied & state.opponent_occupied

            knight_actions += Action.generate_actions(moves, chess.KNIGHT, piece_bb, ActionType.MOVE)
            attack_actions += Action.generate_actions(attack_moves, chess.KNIGHT, piece_bb, ActionType.ATTACK)

        return knight_actions, attack_actions




