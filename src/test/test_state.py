import unittest
import src.chess as chess
from src.chess.state import State
from src.chess.fen import Fen

class StateTest(unittest.TestCase):
    
    def test_get_state_from_fen_en_passant(self):
        state = State("rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq e3 1 2")
        self.assertEqual(state.board.WP.bb, chess.BB_RANK_2 ^ chess.BB_E2 | chess.BB_E4)
        self.assertEqual(state.board.WN.bb, chess.BB_B1 | chess.BB_F3)
        self.assertEqual(state.board.BP.bb, chess.BB_RANK_7 ^ chess.BB_C7 | chess.BB_C5)
        self.assertFalse(state.turn)
        self.assertTrue(state.white_can_castle_kingside)
        self.assertTrue(state.white_can_castle_queenside)
        self.assertTrue(state.black_can_castle_kingside)
        self.assertTrue(state.black_can_castle_queenside)
        self.assertEqual(state.halfmove_count, 1)
        self.assertEqual(state.move_count, 2)
        self.assertEqual(state.en_passant_capture_square, chess.BB_E3)

    def test_get_state_from_fen_no_castling(self):
        state = State("8/8/8/4PPP1/8/R6r/8/k7 w - - 12 24")
        self.assertEqual(state.board.WP.bb, chess.BB_E5 | chess.BB_F5 | chess.BB_G5)
        self.assertEqual(state.board.WR.bb, chess.BB_A3)
        self.assertEqual(state.board.BR.bb, chess.BB_H3)
        self.assertEqual(state.board.BK.bb, chess.BB_A1)
        self.assertTrue(state.turn)
        self.assertFalse(state.white_can_castle_kingside)
        self.assertFalse(state.white_can_castle_queenside)
        self.assertFalse(state.black_can_castle_kingside)
        self.assertFalse(state.black_can_castle_queenside)
        self.assertEqual(state.halfmove_count, 12)
        self.assertEqual(state.move_count, 24)

    def test_get_fen_from_state_1(self):
        state = State("rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq e3 1 2")
        fen = Fen.get_fen_from_state(state)
        print(fen)
        self.assertEqual(
           fen,
           "rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq e3 1 2" 
        )

    def test_get_fen_from_state_2(self):
        state = State("rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R w - - 0 1")
        fen = Fen.get_fen_from_state(state)
        self.assertEqual(
           fen,
           "rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R w - - 0 1" 
        )

if __name__ == '__main__':
    unittest.main()
