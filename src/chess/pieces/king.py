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
                self.moves_lookup[square, color] = new_square

    def get_moves(
        self, opponent_occupied: chess.Bitboard, player_occupied: chess.Bitboard, castle_queenside: bool, castle_kingside: bool
    ):
        king_actions = []
        attack_actions = []

        for current_piece_position_bb in get_individual_ones_in_bb(self.bb):
            square_int = get_square_int_from_bb(current_piece_position_bb)
            moves = self.moves_lookup[(square_int, self.color)] & ~player_occupied
            moves += self._add_castling(opponent_occupied, player_occupied, castle_queenside, castle_kingside)

            attack_moves = self.moves_lookup[(square_int, self.color)] & ~player_occupied & opponent_occupied

            king_actions += Action.generate_actions(
                moves, chess.KING, square_int
            )
            attack_actions += Action.generate_actions(
                attack_moves, chess.KING, square_int
            )

        return king_actions, attack_actions

    def _add_castling(self, opponent_occupied, player_occupied, castle_queenside: bool, castle_kingside: bool):
        castles_bb = chess.BB_EMPTY
        if self.color:
            if castle_queenside:
                if (chess.BB_WHITE_QUEENSIDE_CASTLE_SQUARES & (opponent_occupied | player_occupied)) == chess.BB_EMPTY:
                    castles_bb += chess.BB_C1
            if castle_kingside:
                if (chess.BB_WHITE_KINGSIDE_CASTLE_SQUARES & (opponent_occupied | player_occupied)) == chess.BB_EMPTY:
                    castles_bb += chess.BB_G1
        else:
            if castle_queenside:
                if (chess.BB_BLACK_QUEENSIDE_CASTLE_SQUARES & (opponent_occupied | player_occupied)) == chess.BB_EMPTY:
                    castles_bb += chess.BB_C8
            if castle_kingside:
                if (chess.BB_BLACK_KINGSIDE_CASTLE_SQUARES & (opponent_occupied | player_occupied)) == chess.BB_EMPTY:
                    castles_bb += chess.BB_G8

        return castles_bb




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
