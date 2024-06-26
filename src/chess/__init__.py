
# for notation purposes
FILE_NAMES = ["a", "b", "c", "d", "e", "f", "g", "h"]
RANK_NAMES = ["1", "2", "3", "4", "5", "6", "7", "8"]
SQUARE_NAMES = [file + rank for rank in RANK_NAMES for file in FILE_NAMES]

Color = bool
COLORS = [WHITE, BLACK] = [True, False]
COLOR_NAMES = ["black", "white"]

PieceType = int
PIECE_TYPES = [PAWN, KNIGHT, BISHOP, ROOK, QUEEN, KING] = range(1, 7)
PIECE_SYMBOLS = [None, "p", "n", "b", "r", "q", "k"]
PIECE_STRINGS = ["WK", "WQ", "WN", "WB", "WR", "WP", "BK", "BQ", "BN", "BB", "BR", "BP"]

UNICODE_CHAR_TO_SYMBOL = {
    "r": "♖", "R": "♜",
    "n": "♘", "N": "♞",
    "b": "♗", "B": "♝",
    "q": "♕", "Q": "♛",
    "k": "♔", "K": "♚",
    "p": "♙", "P": "♟",
}
UNICODE_SYMBOL_TO_CHAR = {
    "♖": "r", "♜": "R",
    "♘": "n", "♞": "N",
    "♗": "b", "♝": "B",
    "♕": "q", "♛": "Q",
    "♔": "k", "♚": "K",
    "♙": "p", "♟": "P",
}

PIECE_STRING_TO_CHAR = {
    "WK": "K", "WQ": "Q", "WN": "N", "WB": "B", "WR": "R", "WP": "P",
    "BK": "k", "BQ": "q", "BN": "n", "BB": "b", "BR": "r", "BP": "p",
}

CHAR_TO_PIECE_STRING = {
    "K": "WK", "Q": "WQ", "N": "WN", "B": "WB", "R": "WR", "P": "WP",
    "k": "BK", "q": "BQ", "n": "BN", "b": "BB", "r": "BR", "p": "BP",
}

Square = int
SQUARES = [
    A1, B1, C1, D1, E1, F1, G1, H1,
    A2, B2, C2, D2, E2, F2, G2, H2,
    A3, B3, C3, D3, E3, F3, G3, H3,
    A4, B4, C4, D4, E4, F4, G4, H4,
    A5, B5, C5, D5, E5, F5, G5, H5,
    A6, B6, C6, D6, E6, F6, G6, H6,
    A7, B7, C7, D7, E7, F7, G7, H7,
    A8, B8, C8, D8, E8, F8, G8, H8,
] = range(64)

SQUARE_INT_NAME_DICT = {
    0: 'A1', 1: 'B1', 2: 'C1', 3: 'D1', 4: 'E1', 5: 'F1', 6: 'G1', 7: 'H1',
    8: 'A2', 9: 'B2', 10: 'C2', 11: 'D2', 12: 'E2', 13: 'F2', 14: 'G2', 15: 'H2',
    16: 'A3', 17: 'B3', 18: 'C3', 19: 'D3', 20: 'E3', 21: 'F3', 22: 'G3', 23: 'H3',
    24: 'A4', 25: 'B4', 26: 'C4', 27: 'D4', 28: 'E4', 29: 'F4', 30: 'G4', 31: 'H4',
    32: 'A5', 33: 'B5', 34: 'C5', 35: 'D5', 36: 'E5', 37: 'F5', 38: 'G5', 39: 'H5',
    40: 'A6', 41: 'B6', 42: 'C6', 43: 'D6', 44: 'E6', 45: 'F6', 46: 'G6', 47: 'H6',
    48: 'A7', 49: 'B7', 50: 'C7', 51: 'D7', 52: 'E7', 53: 'F7', 54: 'G7', 55: 'H7',
    56: 'A8', 57: 'B8', 58: 'C8', 59: 'D8', 60: 'E8', 61: 'F8', 62: 'G8', 63: 'H8',
}

Bitboard = int
BB_EMPTY = 0
BB_ALL = 0xffff_ffff_ffff_ffff

BB_SQUARES = [
    BB_A1, BB_B1, BB_C1, BB_D1, BB_E1, BB_F1, BB_G1, BB_H1,
    BB_A2, BB_B2, BB_C2, BB_D2, BB_E2, BB_F2, BB_G2, BB_H2,
    BB_A3, BB_B3, BB_C3, BB_D3, BB_E3, BB_F3, BB_G3, BB_H3,
    BB_A4, BB_B4, BB_C4, BB_D4, BB_E4, BB_F4, BB_G4, BB_H4,
    BB_A5, BB_B5, BB_C5, BB_D5, BB_E5, BB_F5, BB_G5, BB_H5,
    BB_A6, BB_B6, BB_C6, BB_D6, BB_E6, BB_F6, BB_G6, BB_H6,
    BB_A7, BB_B7, BB_C7, BB_D7, BB_E7, BB_F7, BB_G7, BB_H7,
    BB_A8, BB_B8, BB_C8, BB_D8, BB_E8, BB_F8, BB_G8, BB_H8,
] = [1 << square for square in SQUARES]

BB_LIGHT_SQUARES = 0x55aa_55aa_55aa_55aa
BB_DARK_SQUARES = 0xaa55_aa55_aa55_aa55

BB_FILES = [
    BB_FILE_A,
    BB_FILE_B,
    BB_FILE_C,
    BB_FILE_D,
    BB_FILE_E,
    BB_FILE_F,
    BB_FILE_G,
    BB_FILE_H,
] = [0x0101_0101_0101_0101 << i for i in range(8)]


BB_RANKS = [
    BB_RANK_1,
    BB_RANK_2,
    BB_RANK_3,
    BB_RANK_4,
    BB_RANK_5,
    BB_RANK_6,
    BB_RANK_7,
    BB_RANK_8,
] = [0xff << (8 * i) for i in range(8)]

BB_BACKRANKS = BB_RANK_1 | BB_RANK_8

BB_PROMOTION_RANK = (BB_RANK_1, BB_RANK_8)

BB_KINGSIDE_CASTLE_SQUARES = (BB_F8 | BB_G8, BB_F1 | BB_G1)
BB_QUEENSIDE_CASTLE_SQUARES = (BB_D8 | BB_C8 | BB_G1, BB_D1 | BB_C1 | BB_B1)

QUEENSIDE_CASTLE_SQUARE = (BB_C8, BB_C1)
KINGSIDE_CASTLE_SQUARE = (BB_G8, BB_G1)

STARTING_BOARD_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

