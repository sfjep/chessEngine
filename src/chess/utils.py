"""
Missing utils:
- FEN TO BBs
- BBs TO FEN
- FEN to pretty board
"""
from types import MethodType
from typing import Callable, List
import chess
from textwrap import wrap


def get_binary_string_from_bb(bb: int) -> str:
    return "{:064b}".format(bb)

def get_bb_from_binary_string(bin_str: str):
    return int(bin_str, 2)


def print_bitboard(bb: int):
    print(
        "\n".join(
            [
                " ".join(wrap(line[::-1], 1))
                for line in wrap(get_binary_string_from_bb(bb), 8)
            ]
        )
    )

def get_bb_from_binary(bb: int):
    pass


def get_square_int_from_bb(bb: int):
    return chess.BB_SQUARES.index(bb)

def get_bb_from_square_int(square_int: int):
    return chess.BB_SQUARES[square_int]

def get_file_from_bb(bb: int):
    if bb & chess.BB_FILE_A != 0: return chess.BB_FILE_A
    if bb & chess.BB_FILE_B != 0: return chess.BB_FILE_B
    if bb & chess.BB_FILE_C != 0: return chess.BB_FILE_C
    if bb & chess.BB_FILE_D != 0: return chess.BB_FILE_D
    if bb & chess.BB_FILE_E != 0: return chess.BB_FILE_E
    if bb & chess.BB_FILE_F != 0: return chess.BB_FILE_F
    if bb & chess.BB_FILE_G != 0: return chess.BB_FILE_G
    if bb & chess.BB_FILE_H != 0: return chess.BB_FILE_H
    return 0


def get_rank_from_bb(bb: int):
    if bb & chess.BB_RANK_1 != 0: return chess.BB_RANK_1
    if bb & chess.BB_RANK_2 != 0: return chess.BB_RANK_2
    if bb & chess.BB_RANK_3 != 0: return chess.BB_RANK_3
    if bb & chess.BB_RANK_4 != 0: return chess.BB_RANK_4
    if bb & chess.BB_RANK_5 != 0: return chess.BB_RANK_5
    if bb & chess.BB_RANK_6 != 0: return chess.BB_RANK_6
    if bb & chess.BB_RANK_7 != 0: return chess.BB_RANK_7
    if bb & chess.BB_RANK_8 != 0: return chess.BB_RANK_8
    return 0


def get_individual_ones_in_bb(bb_pieces: chess.Bitboard):
    """
    Generates 1 bit bitboards from the decomposition of a bitboard
    """
    while bb_pieces != 0:
        most_sig_bit = 2 ** (bb_pieces.bit_length() - 1)
        yield most_sig_bit
        bb_pieces ^= most_sig_bit


def mask_own_pieces_upward_range(range_bb: chess.Bitboard, own_pieces: chess.Bitboard):
    """
    Input:
    A range BB (vertical, horizontal or diagonal) from the current position UPWARDS or RIGHTWARD
    and the BB of squares occupied by current player.
    Output:
    BB of squares on that range that the acting player CANNOT move to given its own pieces.
    Note: This function works ONLY for movements from a square i (curreny position) to a square j,
    where i < j, for i,j in [0..63].
    Minus 1 flips the sign of all less significant bits from the LEAST significant 1-bit in player occupied
    For example, subtracting 1 from the binary number 0b1010 gives you 0b1001.
    If you then take the complement of this mask with ~(bitboard2 | (bitboard2 - 1)),
    you get a mask with all the bits set above the most significant bit in bitboard2.
    This mask can be used to filter out any values in bitboard1 that have a bit set below the most significant bit in bitboard2.
    """
    _mask = range_bb & own_pieces
    return range_bb & ~((_mask) | (_mask - 1)) | (_mask)

def mask_own_pieces_downward_range(range_bb: chess.Bitboard, opponent_pieces: chess.Bitboard):
    """
    Input:
    A range BB (vertical, horizontal or diagonal) from the current position DOWNWARDS or LEFTWARD
    and the BB of squares occupied by current player.
    Output:
    BB of squares on that range that the acting player CANNOT move to given its own pieces.
    Note: This function works ONLY for movements from a square i (curreny position) to a square j,
    where i > j, for i,j in [0..63].
    """
    msb_index = (range_bb & opponent_pieces).bit_length()
    if msb_index == 0:
        return 0
    else:
        # bit_length is counting from 1, index is counting from 0, therefore we subtract 1 from the bit length to get the index
        _mask = get_bb_from_square_int(msb_index-1) - 1
        return (_mask | opponent_pieces) & range_bb

def mask_own_pieces_upwards(current_position: chess.Bitboard, move_ranges: List[Callable[[chess.Bitboard], chess.Bitboard]], own_pieces: chess.Bitboard):
    target_squares = chess.BB_EMPTY
    for move_range in move_ranges:
        target_squares |= mask_own_pieces_upward_range(move_range(current_position), own_pieces)
    return target_squares

def mask_own_pieces_downwards(current_position: chess.Bitboard, move_ranges: List[Callable[[chess.Bitboard], chess.Bitboard]], own_pieces: chess.Bitboard):
    target_squares = chess.BB_EMPTY
    for move_range in move_ranges:
        target_squares |= mask_own_pieces_downward_range(move_range(current_position), own_pieces)
    return target_squares


def dec_to_signed_bin(num: int):
    if num >= 0:
        return bin(num)[2:].zfill(64)
    else:
        # Two's complement
        return bin((1 << 64) + num)[2:]