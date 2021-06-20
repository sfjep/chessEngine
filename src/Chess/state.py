import Chess

class State:

    def __init__(self):

        self.rook_a1_moved = False
        self.rook_h1_moved = False
        self.rook_a8_moved = False
        self.rook_h8_moved = False
        self.white_king_moved = False
        self.white_king_in_check = False
        self.white_king_checkmate = False
        self.black_king_moved = False
        self.black_king_in_check = False
        self.black_king_checkmate = False
        self.pawn_two_step_last_move = False # Which pawn though, we need BB.
        
        self.fenList = [Chess.STARTING_BOARD_FEN]
 
        self.occupied = Chess.BB_RANK_1 | Chess.BB_RANK_2 | Chess.BB_RANK_7 | Chess.BB_RANK_8

    
    