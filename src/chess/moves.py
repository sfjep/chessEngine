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

    def move_2_up_1_left(b: chess.Bitboard) -> chess.Bitboard:
        return Moves.move_2_up(Moves.move_left(b))
    
    def move_2_up_1_right(b: chess.Bitboard) -> chess.Bitboard:
        return Moves.move_2_up(Moves.move_right(b))

    def move_2_down_1_left(b: chess.Bitboard) -> chess.Bitboard:
        return Moves.move_2_down(Moves.move_left(b))
    
    def move_2_down_1_right(b: chess.Bitboard) -> chess.Bitboard:
        return Moves.move_2_down(Moves.move_right(b))
    
    def move_2_left_1_up(b: chess.Bitboard) -> chess.Bitboard:
        return Moves.move_2_left(Moves.move_up(b))

    def move_2_left_1_down(b: chess.Bitboard) -> chess.Bitboard:
        return Moves.move_2_left(Moves.move_down(b))
    
    def move_2_right_1_up(b: chess.Bitboard) -> chess.Bitboard:
        return Moves.move_2_right(Moves.move_up(b))

    def move_2_right_1_down(b: chess.Bitboard) -> chess.Bitboard:
        return Moves.move_2_right(Moves.move_down(b))