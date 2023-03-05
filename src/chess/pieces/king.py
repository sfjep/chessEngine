from typing import Dict, Tuple
from chess.pieces.piece import Piece
import chess
from chess.moves import Moves
from chess.utils import get_individual_ones_in_bb, get_square_int_from_bb
from chess.action import Action


class King(Piece):
    def __init__(self, bb, color, piece_type):
        super().__init__(bb, color, piece_type)
        self.generate_move_lookup()

    def generate_move_lookup(self):
        self.moves_lookup = {}
        for color in chess.COLORS:
            for square, bb_square in zip(chess.SQUARES, chess.BB_SQUARES):
                new_square = (
                    Moves.move_left(bb_square)
                    | Moves.move_right(bb_square)
                    | Moves.move_up(bb_square)
                    | Moves.move_up_left(bb_square)
                    | Moves.move_up_right(bb_square)
                    | Moves.move_down(bb_square)
                    | Moves.move_down_left(bb_square)
                    | Moves.move_down_right(bb_square)
                )

                if color == chess.WHITE:
                    if square == chess.E1:
                        new_square += Moves.move_2_right(bb_square)
                        new_square += Moves.move_2_left(bb_square)
                else:
                    if square == chess.E8:
                        new_square += Moves.move_2_right(bb_square)
                        new_square += Moves.move_2_left(bb_square)

                self.moves_lookup[square, color] = new_square

    def get_moves(
        self, color: bool, opponent_occupied: chess.Bitboard, player_occupied: chess.Bitboard, castle_queenside: bool, castle_kingside: bool
    ):
        king_actions = []
        attack_actions = []

        for current_piece_position in get_individual_ones_in_bb(self.bb):
            sq = get_square_int_from_bb(current_piece_position)
            moves = self.moves_lookup[sq] & ~player_occupied
            attack_moves = self.moves_lookup[sq] & ~player_occupied & opponent_occupied

            king_actions += Action.generate_actions(
                moves, chess.KING, current_piece_position
            )
            attack_actions += Action.generate_actions(
                attack_moves, chess.KING, current_piece_position
            )

        return king_actions, attack_actions


"""
In check?

Castles?
    # Has moved?
    # Rook moved?
    # Squares in between occupied?
    # Squres in between attacked?
    # In check?

If BB_BLACK_ATTACKED & BB_WHITE_KING != 0:
    Check pinned
"""
