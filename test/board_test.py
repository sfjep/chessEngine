import unittest
import chess
from src.chess.board import Board

class BoardTests(unittest.TestCase):
    
    def setUp(self):
        self.board = Board()
        # define some bitboards for testing purposes
        self.corners = chess.BB_A1 | chess.BB_A8 | chess.BB_H1 | chess.BB_H8

    def square_generator_test_corners(self):
        squares = [Board.piece_squares(self.corners)]
        self.assertEqual(len(squares), 4)
        self.assertEqual(squares[0], chess.BB_H8)
        self.assertEqual(squares[1], chess.BB_H1)
        self.assertEqual(squares[2], chess.BB_A8)
        self.assertEqual(squares[3], chess.BB_A1)

    def square_generator_test_whitepawns(self):
        squares = [Board.piece_squares(self.board.WP.bb)]
        self.assertEqual(len(squares), 8)
        self.assertEqual(chess.BB_RANK_2, self.board.WP.bb)

    def square_generator_test_whiterooks(self):
        squares = [Board.piece_squares(self.board.WR.bb)]
        self.assertEqual(len(squares), 2)
        self.assertEqual(squares[0], chess.BB_H1)
        self.assertEqual(squares[1], chess.BB_A1)

    def square_generator_test_whiteknights(self):
        squares = [Board.piece_squares(self.board.WN.bb)]
        self.assertEqual(len(squares), 2)
        self.assertEqual(squares[0], chess.BB_G1)
        self.assertEqual(squares[1], chess.BB_B1)

    def square_generator_test_whitebishops(self):
        squares = [Board.piece_squares(self.board.WB.bb)]
        self.assertEqual(len(squares), 2)
        self.assertEqual(squares[0], chess.BB_F1)
        self.assertEqual(squares[1], chess.BB_C1)

    def square_generator_test_whiteking(self):
        squares = [Board.piece_squares(self.board.WK.bb)]
        self.assertEqual(len(squares), 1)
        self.assertEqual(squares[0], chess.BB_E1)

    def square_generator_test_whitequeen(self):
        squares = [Board.piece_squares(self.board.WQ.bb)]
        self.assertEqual(len(squares), 1)
        self.assertEqual(squares[0], chess.BB_D1)






