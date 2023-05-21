import chess

class MoveUtils:

    @staticmethod
    def move_down(b: chess.Bitboard) -> chess.Bitboard:
        return (b >> 8) & chess.BB_ALL

    @staticmethod
    def move_2_down(b: chess.Bitboard) -> chess.Bitboard:
        return (b >> 16) & chess.BB_ALL

    @staticmethod
    def move_up(b: chess.Bitboard) -> chess.Bitboard:
        return (b << 8) & chess.BB_ALL

    @staticmethod
    def move_2_up(b: chess.Bitboard) -> chess.Bitboard:
        return (b << 16) & chess.BB_ALL

    @staticmethod
    def move_right(b: chess.Bitboard) -> chess.Bitboard:
        return (b << 1) & ~chess.BB_FILE_A & chess.BB_ALL

    @staticmethod
    def move_2_right(b: chess.Bitboard) -> chess.Bitboard:
        return (b << 2) & ~chess.BB_FILE_A & ~chess.BB_FILE_B & chess.BB_ALL

    @staticmethod
    def move_left(b: chess.Bitboard) -> chess.Bitboard:
        return (b >> 1) & ~chess.BB_FILE_H & chess.BB_ALL

    @staticmethod
    def move_2_left(b: chess.Bitboard) -> chess.Bitboard:
        return (b >> 2) & ~chess.BB_FILE_G & ~chess.BB_FILE_H & chess.BB_ALL

    @staticmethod
    def move_up_left(b: chess.Bitboard) -> chess.Bitboard:
        return (b << 7) & ~chess.BB_FILE_H & chess.BB_ALL

    @staticmethod
    def move_up_right(b: chess.Bitboard) -> chess.Bitboard:
        return (b << 9) & ~chess.BB_FILE_A & chess.BB_ALL

    @staticmethod
    def move_down_left(b: chess.Bitboard) -> chess.Bitboard:
        return (b >> 9) & ~chess.BB_FILE_H & chess.BB_ALL

    @staticmethod
    def move_down_right(b: chess.Bitboard) -> chess.Bitboard:
        return (b >> 7) & ~chess.BB_FILE_A & chess.BB_ALL

    @staticmethod
    def move_up_left_full_range(b: chess.Bitboard) -> chess.Bitboard:
        diag = 0
        while (b := MoveUtils.move_up_left(b)) != 0 :
            diag |= b
        return diag

    @staticmethod
    def move_up_full_range(b: chess.Bitboard) -> chess.Bitboard:
        diag = 0
        while (b := MoveUtils.move_up(b)) != 0 :
            diag |= b
        return diag

    @staticmethod
    def move_down_full_range(b: chess.Bitboard) -> chess.Bitboard:
        diag = 0
        while (b := MoveUtils.move_down(b)) != 0 :
            diag |= b
        return diag

    @staticmethod
    def move_left_full_range(b: chess.Bitboard) -> chess.Bitboard:
        diag = 0
        while (b := MoveUtils.move_left(b)) != 0 :
            diag |= b
        return diag

    @staticmethod
    def move_right_full_range(b: chess.Bitboard) -> chess.Bitboard:
        diag = 0
        while (b := MoveUtils.move_right(b)) != 0 :
            diag |= b
        return diag

    @staticmethod
    def move_up_right_full_range(b: chess.Bitboard) -> chess.Bitboard:
        diag = 0
        while (b := MoveUtils.move_up_right(b)) != 0 :
            diag |= b
        return diag

    @staticmethod
    def move_down_left_full_range(b: chess.Bitboard) -> chess.Bitboard:
        diag = 0
        while (b := MoveUtils.move_down_left(b)) != 0 :
            diag |= b
        return diag

    @staticmethod
    def move_down_right_full_range(b: chess.Bitboard) -> chess.Bitboard:
        diag = 0
        while (b := MoveUtils.move_down_right(b)) != 0 :
            diag |= b
        return diag


    @staticmethod
    def move_2_up_1_left(b: chess.Bitboard) -> chess.Bitboard:
        return MoveUtils.move_2_up(MoveUtils.move_left(b))

    @staticmethod
    def move_2_up_1_right(b: chess.Bitboard) -> chess.Bitboard:
        return MoveUtils.move_2_up(MoveUtils.move_right(b))

    @staticmethod
    def move_2_down_1_left(b: chess.Bitboard) -> chess.Bitboard:
        return MoveUtils.move_2_down(MoveUtils.move_left(b))

    @staticmethod
    def move_2_down_1_right(b: chess.Bitboard) -> chess.Bitboard:
        return MoveUtils.move_2_down(MoveUtils.move_right(b))

    @staticmethod
    def move_2_left_1_up(b: chess.Bitboard) -> chess.Bitboard:
        return MoveUtils.move_2_left(MoveUtils.move_up(b))

    @staticmethod
    def move_2_left_1_down(b: chess.Bitboard) -> chess.Bitboard:
        return MoveUtils.move_2_left(MoveUtils.move_down(b))

    @staticmethod
    def move_2_right_1_up(b: chess.Bitboard) -> chess.Bitboard:
        return MoveUtils.move_2_right(MoveUtils.move_up(b))

    @staticmethod
    def move_2_right_1_down(b: chess.Bitboard) -> chess.Bitboard:
        return MoveUtils.move_2_right(MoveUtils.move_down(b))

def pawn_starting_rank(color):
    if color == chess.WHITE:
        return chess.BB_RANK_2
    else:
        return chess.BB_RANK_7

def pawn_diag_moves(bb, color):
    if color == chess.WHITE:
        return MoveUtils.move_up_left(bb) | MoveUtils.move_up_right(bb)
    else:
        return MoveUtils.move_down_left(bb) | MoveUtils.move_down_right(bb)

def pawn_one_step(bb, color):
    if color == chess.WHITE:
        return MoveUtils.move_up(bb)
    else:
        return MoveUtils.move_down(bb)

def pawn_two_step(bb, color):
    if color == chess.WHITE:
        return MoveUtils.move_2_up(bb)
    else:
        return MoveUtils.move_2_down(bb)

SQUARE_XRAYS = {
    square: {
        "UP_RIGHT": MoveUtils.move_up_right_full_range(chess.BB_SQUARES[square]),
        "RIGHT": MoveUtils.move_right_full_range(chess.BB_SQUARES[square]),
        "DOWN_RIGHT": MoveUtils.move_down_right_full_range(chess.BB_SQUARES[square]),
        "DOWN": MoveUtils.move_down_full_range(chess.BB_SQUARES[square]),
        "DOWN_LEFT": MoveUtils.move_down_left_full_range(chess.BB_SQUARES[square]),
        "LEFT": MoveUtils.move_left_full_range(chess.BB_SQUARES[square]),
        "UP_LEFT": MoveUtils.move_up_left_full_range(chess.BB_SQUARES[square]),
        "UP": MoveUtils.move_up_full_range(chess.BB_SQUARES[square]),
    }
    for square in chess.SQUARES
}
