import unittest
import chess
from chess.action import Action, ActionType
from chess.pieces.rook import Rook
from chess.pieces.king import King
from chess.pieces.pawn import Pawn

class TestAction(unittest.TestCase):

    def test_generate_actions_moves(self):
        moves = chess.BB_A1 | chess.BB_C1
        piece = Rook(chess.BB_B1, chess.WHITE)
        origin_square = chess.B1
        actions = Action.generate_actions(moves, piece, origin_square, ActionType.MOVE)
        expected_repr = ["rb1c1", "rb1a1"]
        actual_repr = [str(action) for action in actions]
        self.assertCountEqual(actual_repr, expected_repr)

    def test_generate_actions_attacks(self):
        moves = chess.BB_A1 | chess.BB_C1
        piece = Rook(chess.BB_B1, chess.WHITE)
        origin_square = chess.B1
        actions = Action.generate_actions(moves, piece, origin_square, ActionType.ATTACK)
        expected_repr = ["rb1xc1", "rb1xa1"]
        actual_repr = [str(action) for action in actions]
        self.assertCountEqual(actual_repr, expected_repr)

    def test_generate_actions_castling(self):
        piece = King(chess.BB_E1, chess.WHITE)
        origin_square = chess.E1
        long_castle = Action.generate_actions(chess.BB_C1, piece, origin_square, ActionType.CASTLING, is_long_castles=True)
        short_castle = Action.generate_actions(chess.BB_G1, piece, origin_square, ActionType.CASTLING, is_long_castles=False)
        actions = long_castle + short_castle
        expected_repr = ["O-O-O", "O-O"]
        actual_repr = [str(action) for action in actions]
        self.assertCountEqual(actual_repr, expected_repr)

    def test_generate_actions_promotion(self):
        piece = Pawn(chess.BB_H7, chess.WHITE)
        origin_square = chess.H7
        action = Action.generate_actions(chess.BB_H8, piece, origin_square, ActionType.PROMOTION, promotion_to=chess.QUEEN)
        expected_repr = ["ph7h8/Q"]
        actual_repr = [str(action) for action in action]
        self.assertCountEqual(actual_repr, expected_repr)

    def test_generate_actions_enpassant(self):
        piece = Pawn(chess.BB_D6, chess.WHITE)
        origin_square = chess.D6
        action = Action.generate_actions(chess.BB_E7, piece, origin_square, ActionType.EN_PASSANT)
        expected_repr = ["pd6xe7"]
        actual_repr = [str(action) for action in action]
        self.assertCountEqual(actual_repr, expected_repr)


