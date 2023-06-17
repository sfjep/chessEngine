import unittest
import src.chess as chess
from src.chess.state import State
from src.chess.action import Action, ActionType
from src.chess.moves.moves import MoveGenerator

class MovesTest(unittest.TestCase):
    def test_en_passant_white(self):
        state = State("4k3/pp1ppppp/8/2pP4/8/8/PPP3PP/3K4 w KQkq c6 3 6")
        state.get_possible_actions()
        pawn_en_passant_action = Action(chess.PAWN, chess.D5, chess.C6, chess.WHITE, ActionType.EN_PASSANT)
        self.assertIn(repr(pawn_en_passant_action),  [repr(action) for action in state.attacks])

    def test_en_passant_black(self):
        state = State("4k3/pp1ppppp/8/8/2pP4/8/PPP3PP/3K4 b KQkq d3 4 7")
        state.get_possible_actions()
        pawn_en_passant_action = Action(chess.PAWN, chess.C4, chess.D3, chess.BLACK, ActionType.EN_PASSANT)
        self.assertIn(repr(pawn_en_passant_action),  [repr(action) for action in state.attacks])

    def test_queen_moves(self):
        state = State("8/2B2p2/8/1p6/2Q2Rp1/8/p1N1p3/K6k w - - 0 1")
        state.get_possible_actions()
        moves_repr_list = [repr(action) for action in state.moves]
        attack_repr_list = [repr(action) for action in state.attacks]

        # MOVE UP THE BOARD

        # Attack up-right
        queen_attack_action = Action(chess.QUEEN, chess.C4, chess.F7, chess.WHITE, ActionType.ATTACK)
        self.assertIn(repr(queen_attack_action), attack_repr_list)

        # Masked out square behind opponent piece
        queen_impossible_move = Action(chess.QUEEN, chess.C4, chess.G8, chess.WHITE, ActionType.MOVE)
        self.assertNotIn(repr(queen_impossible_move), moves_repr_list)

        # Masked out by own piece block
        block_squares = [chess.F4, chess.G4, chess.H4]
        for square in block_squares:
            action = Action(chess.QUEEN, chess.C4, square, chess.WHITE, ActionType.MOVE)
            self.assertNotIn(repr(action), moves_repr_list)


