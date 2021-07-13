
import chess
# FEN TO BB
# BB TO FEN
# FEN to pretty board
from textwrap import wrap

def getBinaryFromBitboard(bb: int) -> str:
    return '{:064b}'.format(bb)


def print_bitboard(bb: int):
    print('\n'.join([' '.join(wrap(line[::-1], 1)) for line in wrap(getBinaryFromBitboard(bb), 8)]))


def getBitboardFromBinary(bb: int):
    pass


def getFileFromBB(bb: int):
    if bb & chess.BB_FILE_A != 0: return chess.BB_FILE_A
    if bb & chess.BB_FILE_B != 0: return chess.BB_FILE_B
    if bb & chess.BB_FILE_C != 0: return chess.BB_FILE_C
    if bb & chess.BB_FILE_D != 0: return chess.BB_FILE_D
    if bb & chess.BB_FILE_E != 0: return chess.BB_FILE_E
    if bb & chess.BB_FILE_F != 0: return chess.BB_FILE_F
    if bb & chess.BB_FILE_G != 0: return chess.BB_FILE_G
    if bb & chess.BB_FILE_H != 0: return chess.BB_FILE_H
    return 0

def getRankFromBB(bb: int):
    if bb & chess.BB_RANK_1 != 0: return chess.BB_RANK_1
    if bb & chess.BB_RANK_2 != 0: return chess.BB_RANK_2
    if bb & chess.BB_RANK_3 != 0: return chess.BB_RANK_3
    if bb & chess.BB_RANK_4 != 0: return chess.BB_RANK_4
    if bb & chess.BB_RANK_5 != 0: return chess.BB_RANK_5
    if bb & chess.BB_RANK_6 != 0: return chess.BB_RANK_6
    if bb & chess.BB_RANK_7 != 0: return chess.BB_RANK_7
    if bb & chess.BB_RANK_8 != 0: return chess.BB_RANK_8
    return 0