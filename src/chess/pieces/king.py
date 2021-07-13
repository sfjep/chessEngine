from typing import Dict, Tuple
from chess import moves_lookup
from chess.pieces.piece import Piece
import chess
from chess.moves import Moves

class King(Piece):

    def __init__(self, bb, color):
        super().__init__(bb, color)

    def generate_move_lookup() -> Dict[Tuple[chess.Square, chess.Color], chess.Bitboard]:
        moves_lookup = {}

        for color in chess.COLORS:
                
            for square, bb_square in zip(chess.SQUARES, chess.BB_SQUARES):
            
                new_square = (
                    Moves.move_left(bb_square) | Moves.move_right(bb_square) |
                    Moves.move_up(bb_square) | Moves.move_up_left(bb_square) | Moves.move_up_right(bb_square) |
                    Moves.move_down(bb_square) | Moves.move_down_left(bb_square) | Moves.move_down_right(bb_square)
                )
                
                if color == chess.WHITE:
                    if square == chess.E1:
                        new_square += Moves.move_2_right(bb_square)
                        new_square += Moves.move_2_left(bb_square)
                else:
                    if square == chess.E8:
                        new_square += Moves.move_2_right(bb_square)
                        new_square += Moves.move_2_left(bb_square)
                                 
                moves_lookup[square, color] = new_square
        
        return moves_lookup

    moves_lookup = generate_move_lookup()

'''
In check?

Castles?
    # Has moved?
    # Rook moved?
    # Squares in between occupied?
    # Squres in between attacked?
    # In check?

If BB_BLACK_ATTACKED & BB_WHITE_KING != 0:
    Check pinned
'''