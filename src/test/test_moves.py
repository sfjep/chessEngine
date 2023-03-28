import unittest
import src.chess as chess
from src.chess.state import State
from src.chess.action import Action

class MovesTest(unittest.TestCase):
    def test_en_passant_white(self):
        state = State("4k3/pp1ppppp/8/2pP4/8/8/PPP3PP/3K4 w KQkq c6 3 6")
        pawn_actions, attack_actions = state.board.WP.get_moves(
			state.board.black_occupied,
			state.board.white_occupied,
			state.en_passant_capture_square
		)
        target_attack_actions = [Action(chess.PAWN, chess.D5, chess.C6)]
        self.assertEqual(repr(attack_actions), repr(target_attack_actions))

    def test_en_passant_black(self):
        state = State("4k3/pp1ppppp/8/8/2pP4/8/PPP3PP/3K4 b KQkq d3 4 7")
        pawn_actions, attack_actions = state.board.BP.get_moves(
			state.board.white_occupied,
			state.board.black_occupied,
			state.en_passant_capture_square
		)
        target_attack_actions = [Action(chess.PAWN, chess.C4, chess.D3)]
        self.assertEqual(repr(attack_actions), repr(target_attack_actions))


