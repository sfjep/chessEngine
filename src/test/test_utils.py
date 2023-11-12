import unittest
import src.chess as chess
from src.chess.utils import (
    get_binary_string_from_bb,
    get_bb_from_binary_string,
    get_square_int_from_bb,
    get_bb_from_square_int,
    get_file_from_bb,
    get_rank_from_bb,
    get_individual_ones_in_bb,
    dec_to_signed_bin,
    get_bb_diagonals_from_square_int,
    get_square_notation,
    convert_rank_and_file_to_square_int,
    get_bb_from_rank_and_file
)

class TestBitboardUtils(unittest.TestCase):

    def test_get_binary_string_from_bb(self):
        bb = chess.BB_A1
        result = get_binary_string_from_bb(bb)
        self.assertEqual(result, '0' * 63 + '1')

        bb = chess.BB_H8
        result = get_binary_string_from_bb(bb)
        self.assertEqual(result, '1' + '0' * 63)

    def test_get_bb_from_binary_string(self):
        binary_string = '0' * 63 + '1'
        result = get_bb_from_binary_string(binary_string)
        self.assertEqual(result, chess.BB_A1)

    def test_get_square_int_from_bb(self):
        bb = chess.BB_A1
        result = get_square_int_from_bb(bb)
        self.assertEqual(result, 0)

    def test_get_bb_from_square_int(self):
        square = 0
        result = get_bb_from_square_int(square)
        self.assertEqual(result, chess.BB_A1)

    def test_get_file_from_bb(self):
        bb = chess.BB_C1
        result = get_file_from_bb(bb)
        self.assertEqual(result, chess.BB_FILE_C)

    def test_get_rank_from_bb(self):
        bb = chess.BB_H5
        result = get_rank_from_bb(bb)
        self.assertEqual(result, chess.BB_RANK_5)

    def test_get_individual_ones_in_bb(self):
        bb = chess.BB_RANK_1  # Rank 1 has 8 pieces
        result = list(get_individual_ones_in_bb(bb))
        self.assertEqual(len(result), 8)
        self.assertTrue(all(isinstance(x, int) for x in result))
        self.assertTrue(all(x & chess.BB_RANK_1 for x in result))
        self.assertTrue(not(any(x & chess.BB_RANK_2 for x in result)))

    def test_dec_to_signed_bin(self):
        number = 5
        result = dec_to_signed_bin(number)
        self.assertEqual(result, '0' * 61 + '101')

    def test_get_square_notation(self):
        square_int = 0  # A1
        result = get_square_notation(square_int)
        self.assertEqual(result, 'a1')

    def test_convert_rank_and_file_to_square_int(self):
        rank, file = 0, 0  # A1
        result = convert_rank_and_file_to_square_int(rank, file)
        self.assertEqual(result, 0)

    def test_get_bb_from_rank_and_file(self):
        rank, file = 0, 0  # A1
        result = get_bb_from_rank_and_file(rank, file)
        self.assertEqual(result, chess.BB_A1)

