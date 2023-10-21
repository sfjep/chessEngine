"""
Missing utils:
- FEN TO BBs
- BBs TO FEN
- FEN to pretty board
"""
from chess.moves.move_utils import SQUARE_XRAYS
import chess
from textwrap import wrap
from typing import Tuple

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


def dec_to_signed_bin(num: int):
    if num >= 0:
        return bin(num)[2:].zfill(64)
    else:
        # Two's complement
        return bin((1 << 64) + num)[2:]

def get_bb_diagonals_from_square_int(square: int):
    return (
        SQUARE_XRAYS[square]["UP_RIGHT"] |
        SQUARE_XRAYS[square]["UP_LEFT"] |
        SQUARE_XRAYS[square]["DOWN_RIGHT"] |
        SQUARE_XRAYS[square]["DOWN_LEFT"]
    )

def get_square_notation(n: int) -> str:
    if n < 0 or n > 63:
        raise ValueError("n must be between 0 and 63")
    row = chr(ord('a') + n % 8)
    col = str(n // 8 + 1)
    return row + col

def convert_rank_and_file_to_square_int(rank: int, file: int) -> int:
    return rank * 8 + file

def get_bb_from_rank_and_file(rank: int, file: int) -> chess.Bitboard:
    square_int = convert_rank_and_file_to_square_int(rank, file)
    return get_bb_from_square_int(square_int)

def lsb(n: int) -> int:
    return n & -n

def typename(obj):
    return type(obj).__name__

def get_rank_file_from_square_int(square: int) -> Tuple[int, int]:
    if square < 0 or square > 63:
        raise ValueError("Square value must be between 0 and 63.")

    rank = square // 8  # The quotient represents the rank.
    file = square % 8   # The remainder represents the file.
    return rank, file