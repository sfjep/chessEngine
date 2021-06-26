import unittest
import src.chess as chess
from src.chess.board import Board

class BoardTest(unittest.TestCase):
    
    def test_square_generator_corners(self):
        self.board = Board()
        self.corners = chess.BB_A1 | chess.BB_A8 | chess.BB_H1 | chess.BB_H8
        squares = [bb for bb in Board.piece_squares(self.corners)]
        self.assertEqual(len(squares), 4)
        self.assertEqual(squares[0], chess.BB_H8)
        self.assertEqual(squares[1], chess.BB_A8)
        self.assertEqual(squares[2], chess.BB_H1)
        self.assertEqual(squares[3], chess.BB_A1)

    def test_square_generator_whitepawns(self):
        self.board = Board()
        squares = [bb for bb in Board.piece_squares(self.board.WP.bb)]
        self.assertEqual(len(squares), 8)
        self.assertEqual(chess.BB_RANK_2, self.board.WP.bb)

    def test_square_generator_whiterooks(self):
        self.board = Board()
        squares = [bb for bb in Board.piece_squares(self.board.WR.bb)]
        self.assertEqual(len(squares), 2)
        self.assertEqual(squares[0], chess.BB_H1)
        self.assertEqual(squares[1], chess.BB_A1)

    def test_square_generator_whiteknights(self):
        self.board = Board()
        squares = [bb for bb in Board.piece_squares(self.board.WN.bb)]
        self.assertEqual(len(squares), 2)
        self.assertEqual(squares[0], chess.BB_G1)
        self.assertEqual(squares[1], chess.BB_B1)

    def test_square_generator_whitebishops(self):
        self.board = Board()
        squares = [bb for bb in Board.piece_squares(self.board.WB.bb)]
        self.assertEqual(len(squares), 2)
        self.assertEqual(squares[0], chess.BB_F1)
        self.assertEqual(squares[1], chess.BB_C1)

    def test_square_generator_whiteking(self):
        self.board = Board()
        squares = [bb for bb in Board.piece_squares(self.board.WK.bb)]
        self.assertEqual(len(squares), 1)
        self.assertEqual(squares[0], chess.BB_E1)

    def test_square_generator_whitequeen(self):
        self.board = Board()
        squares = [bb for bb in Board.piece_squares(self.board.WQ.bb)]
        self.assertEqual(len(squares), 1)
        self.assertEqual(squares[0], chess.BB_D1)

if __name__ == '__main__':
    unittest.main()
