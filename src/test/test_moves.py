import unittest
import src.chess as chess
from src.chess.state import State
from src.chess.action import Action, ActionType
from src.chess.moves.moves import MoveGenerator

class MovesTest(unittest.TestCase):

    def setUp(self):
        self.state_white_promote = State("8/6P1/2k5/4K3/8/8/8/8 w - - 0 1")
        self.state_white_promote_check = State("4k3/6P1/8/4K3/8/8/8/8 w - - 0 1")
        self.state_white_promote_checkmate = State("4k3/6P1/4K3/8/8/8/8/8 w - - 0 1")
        self.state_white_promote_stalemate = State("8/k5P1/2K5/8/2B5/8/8/8 w - - 0 1")

        self.state_white_en_passant = State("3k4/8/8/5Pp1/8/8/8/4K3 w - g6 0 1")
        self.state_white_rook_blocked = State("4k3/8/3p4/8/1p1R1P2/8/3P4/4K3 w - - 0 1")
        self.state_white_bishop_blocked = State("4k3/8/1p3P2/8/3B4/8/1P3p2/3K4 w - - 0 1")
        self.state_white_queen_blocked = State("4k3/8/1P1p1P2/8/1p1Q1Pp1/8/1P1P1p2/3K4 w - - 0 1")
        self.state_white_kingside_castle = State("3k4/8/8/8/8/8/8/4K2R w K - 0 1")
        self.state_white_kingside_castle_blocked = State("4k3/8/1b6/8/8/8/8/4K2R w K - 0 1")
        self.state_white_queenside_castle = State("3k4/8/8/8/8/8/8/R3K3 w K - 0 1")
        self.state_white_queenside_castle_blocked = State("4k3/8/8/7b/8/8/8/R3K3 w Q - 0 1")
        self.state_white_queenside_castle_in_check = State("4k3/4r3/8/8/8/8/8/R3K3 w Q - 0 1")
        self.state_white_pinned_pawn = State("4k3/8/8/8/7b/8/5P2/4K3 w - - 0 1")
        self.state_white_pinned_bishop = State("4k3/8/8/8/7b/8/5B2/4K3 w - - 0 1")


        self.state_black_promote = State("4k3/8/8/8/8/8/3K3p/8 b - - 0 1")
        self.state_black_promote_check = State("8/8/8/8/4k3/8/6p1/4K3 b - - 0 1")
        self.state_black_promote_checkmate = State("8/8/8/8/8/4k3/6p1/4K3 b - - 0 1")
        self.state_black_promote_stalemate = State("8/4b3/8/8/8/2k5/K5p1/8 b - - 0 1")
        self.state_black_en_passant = State("4k3/8/8/8/1Pp5/8/8/4K3 b - b3 0 1")
        self.state_black_rook_blocked = State("4k3/8/3p4/8/1p1r1P2/8/3P4/4K3 w - - 0 1")
        self.state_black_bishop_blocked = State("4k3/8/1p3P2/8/3b4/8/1P3p2/4K3 w - - 0 1")
        self.state_black_queen_blocked = State("4k3/8/1P1p1P2/8/1Ppq1Pp1/8/1P1P1p2/3K4 w - - 0 1")
        self.state_black_kingside_castle = State("4k2r/8/8/8/8/8/8/4K3 b k - 0 1")
        self.state_black_kingside_castle_blocked = State("4k2r/8/8/8/1B6/8/8/4K3 b k - 0 1")
        self.state_black_queenside_castle = State("r3k3/8/8/8/8/8/8/4K3 b q - 0 1")
        self.state_black_queenside_castle_blocked = State("r3k3/8/8/8/6B1/8/8/4K3 b q - 0 1")
        self.state_black_queenside_castle_in_check = State("r3k3/8/8/8/8/8/4R3/4K3 b q - 0 1")
        self.state_black_pinned_pawn = State("4k3/5p2/8/7B/8/8/8/4K3 b - - 0 1")
        self.state_black_pinned_bishop = State("4k3/5b2/8/7B/8/8/8/4K3 b - - 0 1")

    # def test_white_promotion(self):
    #     state_white_promote = State("8/6P1/2k5/4K3/8/8/8/8 w - - 0 1")
    #     move_gen = MoveGenerator(state_white_promote)
    #     move_gen.get_piece_moves()
    #     promotion_strings = [repr(promo).lower() for promo in move_gen.promotions]
    #     self.assertIn("pg7g8/q", promotion_strings)
    #     self.assertIn("pg7g8/n", promotion_strings)
    #     self.assertIn("pg7g8/r", promotion_strings)
    #     self.assertIn("pg7g8/b", promotion_strings)
    #     self.assertEqual(len(promotion_strings), 4)

    def test_white_enpassant(self):
        state_white_en_passant = State("3k4/8/8/4pPp1/8/8/8/4K3 w - g6 0 1")
        move_gen = MoveGenerator(state_white_en_passant)
        move_gen.get_piece_moves()
        en_passant_string = [str(action).lower() for action in move_gen.moves]
        self.assertIn("pf5xg6", en_passant_string)

    def test_white_rook_blocked(self):
        state_white_rook_blocked = State("3k4/8/3p4/8/1p1R1P2/8/3P4/4K3 w - - 0 1")
        move_gen = MoveGenerator(state_white_rook_blocked)
        move_gen.get_piece_moves()
        rook_move_repr = [str(move).lower() for move in move_gen.moves if str(move)[0] =="r"]
        self.assertIn("rd4d3", rook_move_repr)
        self.assertIn("rd4d5", rook_move_repr)
        self.assertIn("rd4c4", rook_move_repr)
        self.assertIn("rd4e4", rook_move_repr)
        self.assertIn("rd4xb4", rook_move_repr)
        self.assertIn("rd4xd6", rook_move_repr)
        self.assertEqual(len(rook_move_repr), 6)


    # def test_number_of_valid_moves_from_start(self):
    #     depth_1 = 20
    #     depth_2 = 400
    #     depth_3 = 8902
    #     depth_4 = 197281
    #     depth_5 = 4865609
    #     depth_6 = 119060324
    #     state = State()
    #     result = {}
    #     for depth in range(1, 7):
    #         state.get_possible_actions()
    #         result[depth] = len(state.valid_moves)

    #     self.assertEqual(depth_1, result[1])
    #     self.assertEqual(depth_2, result[2])
    #     self.assertEqual(depth_3, result[3])
    #     self.assertEqual(depth_4, result[4])
    #     self.assertEqual(depth_5, result[5])
    #     self.assertEqual(depth_6, result[6])

    # def test_number_of_valid_moves_from_fen(self):
    #     depth_1 = 44
    #     depth_2 = 1486
    #     depth_3 = 62379
    #     depth_4 = 2103487
    #     depth_5 = 89941194
    #     state = State('rnbq1kr/pp1Pbppp/2p5/8/2B5/8/PP1NnPP/RNBQK2R w KQ - 1 8')
    #     result = {}

    #     for depth in range(1,6):
    #         state.get_possible_actions()
    #         result[depth] = len(state.valid_moves)

    #     self.assertEqual(depth_1, result[1])
    #     self.assertEqual(depth_2, result[2])
    #     self.assertEqual(depth_3, result[3])
    #     self.assertEqual(depth_4, result[4])
    #     self.assertEqual(depth_5, result[5])