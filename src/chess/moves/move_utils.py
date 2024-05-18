import chess

def move_down(b: chess.Bitboard) -> chess.Bitboard:
    return (b >> 8) & chess.BB_ALL

def move_2_down(b: chess.Bitboard) -> chess.Bitboard:
    return (b >> 16) & chess.BB_ALL

def move_up(b: chess.Bitboard) -> chess.Bitboard:
    return (b << 8) & chess.BB_ALL

def move_2_up(b: chess.Bitboard) -> chess.Bitboard:
    return (b << 16) & chess.BB_ALL

def move_right(b: chess.Bitboard) -> chess.Bitboard:
    return (b << 1) & ~chess.BB_FILE_A & chess.BB_ALL

def move_2_right(b: chess.Bitboard) -> chess.Bitboard:
    return (b << 2) & ~chess.BB_FILE_A & ~chess.BB_FILE_B & chess.BB_ALL

def move_left(b: chess.Bitboard) -> chess.Bitboard:
    return (b >> 1) & ~chess.BB_FILE_H & chess.BB_ALL

def move_2_left(b: chess.Bitboard) -> chess.Bitboard:
    return (b >> 2) & ~chess.BB_FILE_G & ~chess.BB_FILE_H & chess.BB_ALL

def move_up_left(b: chess.Bitboard) -> chess.Bitboard:
    return (b << 7) & ~chess.BB_FILE_H & chess.BB_ALL

def move_up_right(b: chess.Bitboard) -> chess.Bitboard:
    return (b << 9) & ~chess.BB_FILE_A & chess.BB_ALL

def move_down_left(b: chess.Bitboard) -> chess.Bitboard:
    return (b >> 9) & ~chess.BB_FILE_H & chess.BB_ALL

def move_down_right(b: chess.Bitboard) -> chess.Bitboard:
    return (b >> 7) & ~chess.BB_FILE_A & chess.BB_ALL

def move_up_left_full_range(b: chess.Bitboard) -> chess.Bitboard:
    diag = 0
    while (b := move_up_left(b)) != 0 :
        diag |= b
    return diag

def move_up_full_range(b: chess.Bitboard) -> chess.Bitboard:
    diag = 0
    while (b := move_up(b)) != 0 :
        diag |= b
    return diag

def move_down_full_range(b: chess.Bitboard) -> chess.Bitboard:
    diag = 0
    while (b := move_down(b)) != 0 :
        diag |= b
    return diag

def move_left_full_range(b: chess.Bitboard) -> chess.Bitboard:
    diag = 0
    while (b := move_left(b)) != 0 :
        diag |= b
    return diag

def move_right_full_range(b: chess.Bitboard) -> chess.Bitboard:
    diag = 0
    while (b := move_right(b)) != 0 :
        diag |= b
    return diag

def move_up_right_full_range(b: chess.Bitboard) -> chess.Bitboard:
    diag = 0
    while (b := move_up_right(b)) != 0 :
        diag |= b
    return diag

def move_down_left_full_range(b: chess.Bitboard) -> chess.Bitboard:
    diag = 0
    while (b := move_down_left(b)) != 0 :
        diag |= b
    return diag

def move_down_right_full_range(b: chess.Bitboard) -> chess.Bitboard:
    diag = 0
    while (b := move_down_right(b)) != 0 :
        diag |= b
    return diag

def move_2_up_1_left(b: chess.Bitboard) -> chess.Bitboard:
    return move_2_up(move_left(b))

def move_2_up_1_right(b: chess.Bitboard) -> chess.Bitboard:
    return move_2_up(move_right(b))

def move_2_down_1_left(b: chess.Bitboard) -> chess.Bitboard:
    return move_2_down(move_left(b))

def move_2_down_1_right(b: chess.Bitboard) -> chess.Bitboard:
    return move_2_down(move_right(b))

def move_2_left_1_up(b: chess.Bitboard) -> chess.Bitboard:
    return move_2_left(move_up(b))

def move_2_left_1_down(b: chess.Bitboard) -> chess.Bitboard:
    return move_2_left(move_down(b))

def move_2_right_1_up(b: chess.Bitboard) -> chess.Bitboard:
    return move_2_right(move_up(b))

def move_2_right_1_down(b: chess.Bitboard) -> chess.Bitboard:
    return move_2_right(move_down(b))

def pawn_starting_rank(color):
    if color == chess.WHITE:
        return chess.BB_RANK_2
    else:
        return chess.BB_RANK_7

def pawn_diag_moves(bb, color):
    if color == chess.WHITE:
        return move_up_left(bb) | move_up_right(bb)
    else:
        return move_down_left(bb) | move_down_right(bb)

def pawn_one_step(bb, color):
    if color == chess.WHITE:
        return move_up(bb)
    else:
        return move_down(bb)

def pawn_two_step(bb, color):
    if color == chess.WHITE:
        return move_2_up(bb)
    else:
        return move_2_down(bb)
    

MOVE_FUNCTION = {
    "UP_RIGHT": move_up_right,
    "RIGHT": move_right,
    "DOWN_RIGHT": move_down_right,
    "DOWN": move_down,
    "DOWN_LEFT": move_down_left,
    "LEFT": move_left,
    "UP_LEFT": move_up_left,
    "UP": move_up,
}

SQUARE_XRAYS = {
    square: {
        "UP_RIGHT": move_up_right_full_range(chess.BB_SQUARES[square]),
        "RIGHT": move_right_full_range(chess.BB_SQUARES[square]),
        "DOWN_RIGHT": move_down_right_full_range(chess.BB_SQUARES[square]),
        "DOWN": move_down_full_range(chess.BB_SQUARES[square]),
        "DOWN_LEFT": move_down_left_full_range(chess.BB_SQUARES[square]),
        "LEFT": move_left_full_range(chess.BB_SQUARES[square]),
        "UP_LEFT": move_up_left_full_range(chess.BB_SQUARES[square]),
        "UP": move_up_full_range(chess.BB_SQUARES[square]),
    }
    for square in chess.SQUARES
}

