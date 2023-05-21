
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

BB_KINGSIDE_CASTLE_SQUARES = (BB_F8 | BB_G8, BB_F1 | BB_G1)
BB_QUEENSIDE_CASTLE_SQUARES = (BB_D8 | BB_C8 | BB_G1, BB_D1 | BB_C1 | BB_B1)

QUEENSIDE_CASTLE_SQUARE = (BB_C8, BB_C1)
KINGSIDE_CASTLE_SQUARE = (BB_G8, BB_G1)

# NOTATION
# STARTING_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
# """The FEN for the standard chess starting position."""

STARTING_BOARD_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
"""The board part of the FEN for the standard chess starting position."""

