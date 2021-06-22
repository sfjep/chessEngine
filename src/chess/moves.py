import chess

class Moves:
        
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
