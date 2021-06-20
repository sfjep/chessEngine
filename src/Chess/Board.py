
import Chess
import numpy as np

class Board:

    def __init__(self):
        
        self.pawns = Chess.BB_RANK_2 | Chess.BB_RANK_7
        self.knights = Chess.BB_B1 | Chess.BB_G1 | Chess.BB_B8 | Chess.BB_G8
        self.bishops = Chess.BB_C1 | Chess.BB_F1 | Chess.BB_C8 | Chess.BB_F8
        self.rooks = Chess.BB_A1 | Chess.BB_H1 | Chess.BB_A8 | Chess.BB_H8
        self.queens = Chess.BB_D1 | Chess.BB_D8
        self.kings = Chess.BB_E1 | Chess.BB_E8
        
        # CASTLING RIGHTS
        self.rook_a1_moved = False
        self.rook_h1_moved = False
        self.rook_a8_moved = False
        self.rook_h8_moved = False
        self.white_king_moved = False
        self.black_king_moved = False
        
        self.occupied = Chess.BB_RANK_1 | Chess.BB_RANK_2 | Chess.BB_RANK_7 | Chess.BB_RANK_8

