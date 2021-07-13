from typing import Dict
from chess import moves_lookup
from chess.moves import Moves
from chess.pieces.piece import Piece
import chess

class Knight(Piece):
    def __init__(self, bb, color):
        super().__init__(bb, color)

    def generate_move_lookup() -> Dict[chess.Square, chess.Bitboard]:
        moves_lookup = {}        
        for square, bb_square in zip(chess.SQUARES, chess.BB_SQUARES):
            new_square = 0
            new_square += Moves.move_2_down_1_left(bb_square)
            new_square += Moves.move_2_down_1_right(bb_square)
            new_square += Moves.move_2_up_1_left(bb_square)
            new_square += Moves.move_2_up_1_right(bb_square)
            new_square += Moves.move_2_left_1_up(bb_square)
            new_square += Moves.move_2_left_1_down(bb_square)
            new_square += Moves.move_2_right_1_up(bb_square)
            new_square += Moves.move_2_right_1_down(bb_square)

            moves_lookup[square] = new_square
        
        return moves_lookup
    
    moves_lookup = generate_move_lookup()

                
    
