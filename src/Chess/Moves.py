import Chess

class Move:
    pass



def move_down(b: Chess.Bitboard) -> Chess.Bitboard:
    return b >> 8

def move_2_down(b: Chess.Bitboard) -> Chess.Bitboard:
    return b >> 16

def move_up(b: Chess.Bitboard) -> Chess.Bitboard:
    return (b << 8) & Chess.BB_ALL

def move_2_up(b: Chess.Bitboard) -> Chess.Bitboard:
    return (b << 16) & Chess.BB_ALL

def move_right(b: Chess.Bitboard) -> Chess.Bitboard:
    return (b << 1) & ~Chess.BB_FILE_A & Chess.BB_ALL

def move_2_right(b: Chess.Bitboard) -> Chess.Bitboard:
    return (b << 2) & ~Chess.BB_FILE_A & ~Chess.BB_FILE_B & Chess.BB_ALL

def move_left(b: Chess.Bitboard) -> Chess.Bitboard:
    return (b >> 1) & ~Chess.BB_FILE_H

def move_2_left(b: Chess.Bitboard) -> Chess.Bitboard:
    return (b >> 2) & ~Chess.BB_FILE_G & ~Chess.BB_FILE_H

def move_up_left(b: Chess.Bitboard) -> Chess.Bitboard:
    return (b << 7) & ~Chess.BB_FILE_H & Chess.BB_ALL

def move_up_right(b: Chess.Bitboard) -> Chess.Bitboard:
    return (b << 9) & ~Chess.BB_FILE_A & Chess.BB_ALL

def move_down_left(b: Chess.Bitboard) -> Chess.Bitboard:
    return (b >> 9) & ~Chess.BB_FILE_H

def move_down_right(b: Chess.Bitboard) -> Chess.Bitboard:
    return (b >> 7) & ~Chess.BB_FILE_A