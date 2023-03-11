import chess

class Moves:

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
        while (b := Moves.move_up_left(b)) != 0 :
            diag |= b
        return diag

    @staticmethod
    def move_up_full_range(b: chess.Bitboard) -> chess.Bitboard:
        diag = 0
        while (b := Moves.move_up(b)) != 0 :
            diag |= b
        return diag

    @staticmethod
    def move_down_full_range(b: chess.Bitboard) -> chess.Bitboard:
        diag = 0
        while (b := Moves.move_down(b)) != 0 :
            diag |= b
        return diag

    @staticmethod
    def move_left_full_range(b: chess.Bitboard) -> chess.Bitboard:
        diag = 0
        while (b := Moves.move_left(b)) != 0 :
            diag |= b
        return diag

    @staticmethod
    def move_right_full_range(b: chess.Bitboard) -> chess.Bitboard:
        diag = 0
        while (b := Moves.move_right(b)) != 0 :
            diag |= b
        return diag

    @staticmethod
    def move_up_right_full_range(b: chess.Bitboard) -> chess.Bitboard:
        diag = 0
        while (b := Moves.move_up_right(b)) != 0 :
            diag |= b
        return diag

    @staticmethod
    def move_down_left_full_range(b: chess.Bitboard) -> chess.Bitboard:
        diag = 0
        while (b := Moves.move_down_left(b)) != 0 :
            diag |= b
        return diag

    @staticmethod
    def move_down_right_full_range(b: chess.Bitboard) -> chess.Bitboard:
        diag = 0
        while (b := Moves.move_down_right(b)) != 0 :
            diag |= b
        return diag


    @staticmethod
    def move_2_up_1_left(b: chess.Bitboard) -> chess.Bitboard:
        return Moves.move_2_up(Moves.move_left(b))

    @staticmethod
    def move_2_up_1_right(b: chess.Bitboard) -> chess.Bitboard:
        return Moves.move_2_up(Moves.move_right(b))

    @staticmethod
    def move_2_down_1_left(b: chess.Bitboard) -> chess.Bitboard:
        return Moves.move_2_down(Moves.move_left(b))

    @staticmethod
    def move_2_down_1_right(b: chess.Bitboard) -> chess.Bitboard:
        return Moves.move_2_down(Moves.move_right(b))

    @staticmethod
    def move_2_left_1_up(b: chess.Bitboard) -> chess.Bitboard:
        return Moves.move_2_left(Moves.move_up(b))

    @staticmethod
    def move_2_left_1_down(b: chess.Bitboard) -> chess.Bitboard:
        return Moves.move_2_left(Moves.move_down(b))

    @staticmethod
    def move_2_right_1_up(b: chess.Bitboard) -> chess.Bitboard:
        return Moves.move_2_right(Moves.move_up(b))

    @staticmethod
    def move_2_right_1_down(b: chess.Bitboard) -> chess.Bitboard:
        return Moves.move_2_right(Moves.move_down(b))


SQUARE_XRAYS = {}
for square in chess.SQUARES:
    SQUARE_XRAYS[square] = {
        "UP_RIGHT": Moves.move_up_right_full_range(chess.BB_SQUARES[square]),
        "RIGHT": Moves.move_right_full_range(chess.BB_SQUARES[square]),
        "DOWN_RIGHT": Moves.move_down_right_full_range(chess.BB_SQUARES[square]),
        "DOWN": Moves.move_down_full_range(chess.BB_SQUARES[square]),
        "DOWN_LEFT": Moves.move_down_left_full_range(chess.BB_SQUARES[square]),
        "LEFT": Moves.move_left_full_range(chess.BB_SQUARES[square]),
        "UP_LEFT": Moves.move_up_left_full_range(chess.BB_SQUARES[square]),
        "UP": Moves.move_up_full_range(chess.BB_SQUARES[square]),
    }
