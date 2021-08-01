import unittest
import src.chess as chess
from src.chess.board import Board, InvalidFenException
from src.chess.utils import get_individual_ones_in_bb

class BoardTest(unittest.TestCase):
    
    def test_square_generator_corners(self):
        self.corners = chess.BB_A1 | chess.BB_A8 | chess.BB_H1 | chess.BB_H8
        squares = [bb for bb in get_individual_ones_in_bb(self.corners)]
        self.assertEqual(len(squares), 4)
        self.assertEqual(squares[0], chess.BB_H8)
        self.assertEqual(squares[1], chess.BB_A8)
        self.assertEqual(squares[2], chess.BB_H1)
        self.assertEqual(squares[3], chess.BB_A1)

    def test_square_generator_whitepawns(self):
        board = Board()
        squares = [bb for bb in get_individual_ones_in_bb(board.WP.bb)]
        self.assertEqual(len(squares), 8)
        self.assertEqual(chess.BB_RANK_2, board.WP.bb)

    def test_square_generator_whiterooks(self):
        board = Board()
        squares = [bb for bb in get_individual_ones_in_bb(board.WR.bb)]
        self.assertEqual(len(squares), 2)
        self.assertEqual(squares[0], chess.BB_H1)
        self.assertEqual(squares[1], chess.BB_A1)

    def test_square_generator_whiteknights(self):
        board = Board()
        squares = [bb for bb in get_individual_ones_in_bb(board.WN.bb)]
        self.assertEqual(len(squares), 2)
        self.assertEqual(squares[0], chess.BB_G1)
        self.assertEqual(squares[1], chess.BB_B1)

    def test_square_generator_whitebishops(self):
        board = Board()
        squares = [bb for bb in get_individual_ones_in_bb(board.WB.bb)]
        self.assertEqual(len(squares), 2)
        self.assertEqual(squares[0], chess.BB_F1)
        self.assertEqual(squares[1], chess.BB_C1)

    def test_square_generator_whiteking(self):
        board = Board()
        squares = [bb for bb in get_individual_ones_in_bb(board.WK.bb)]
        self.assertEqual(len(squares), 1)
        self.assertEqual(squares[0], chess.BB_E1)

    def test_square_generator_whitequeen(self):
        board = Board()
        squares = [bb for bb in get_individual_ones_in_bb(board.WQ.bb)]
        self.assertEqual(len(squares), 1)
        self.assertEqual(squares[0], chess.BB_D1)

    def test_board_from_fen(self):
        board = Board("rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R")
        self.assertEqual(board.WP.bb, chess.BB_RANK_2 ^ chess.BB_E2 | chess.BB_E4)
        self.assertEqual(board.WN.bb, chess.BB_B1 | chess.BB_F3)
        self.assertEqual(board.BP.bb, chess.BB_RANK_7 ^ chess.BB_C7 | chess.BB_C5)

    def test_board_from_empty_fen(self):
        board = Board("8/8/8/8/8/8/8/8")
        for piece in board.pieces:
            self.assertEqual(piece.bb, chess.BB_EMPTY)

    def test_board_from_fen_2(self):
        board = Board("8/8/8/4PPP1/8/R6r/8/k7")
        self.assertEqual(board.WP.bb, chess.BB_E5 | chess.BB_F5 | chess.BB_G5)
        self.assertEqual(board.WR.bb, chess.BB_A3)
        self.assertEqual(board.BR.bb, chess.BB_H3)
        self.assertEqual(board.BK.bb, chess.BB_A1)

    def test_board_from_invalid_fen(self):
        self.assertRaises(InvalidFenException, Board, "someinvalidfen")

    def test_board_from_too_many_spaces(self):
        self.assertRaises(InvalidFenException, Board, "8/8/8/5PPP1/8/R8r/8/k7")

    def test_board_from_too_many_rows(self):
        self.assertRaises(InvalidFenException, Board, "8/8/8/5PPP1/8/R8r/8/k7/8")



if __name__ == '__main__':
    unittest.main()
