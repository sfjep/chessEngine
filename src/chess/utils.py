"""
Missing utils:
- FEN TO BBs
- BBs TO FEN
- FEN to pretty board
"""
import chess
from textwrap import wrap


def get_binary_string_from_bb(bb: int) -> str:
    return "{:064b}".format(bb)


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


def mask_up_right_own_pieces(diagonal_bb: chess.Bitboard, player_occupied: chess.Bitboard):
    """Minus 1 flips the sign of all less significant bits from the LEAST significant 1-bit in player occupied
    For example, subtracting 1 from the binary number 0b1010 gives you 0b1001.
    If you then take the complement of this mask with ~(bitboard2 | (bitboard2 - 1)), you get a mask with all the bits set above the most significant bit in bitboard2.
    This mask can be used to filter out any values in bitboard1 that have a bit set below the most significant bit in bitboard2.
    """
    _mask = diagonal_bb & player_occupied
    return diagonal_bb & ~((_mask) | (_mask - 1)) | (_mask)

def mask_up_right_opponent_pieces(diagonal_bb: chess.Bitboard, opponent_occupied: chess.Bitboard):
    _mask = diagonal_bb & opponent_occupied
    return diagonal_bb & ~(_mask | (_mask - 1))