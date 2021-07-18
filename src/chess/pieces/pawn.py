from typing import Dict, Tuple
from chess.pieces.piece import Piece
from chess.moves import Moves
import chess

class Pawn(Piece):
    def __init__(self, bb, color):
        super().__init__(bb, color)

    def generate_move_lookup() -> Dict[Tuple[chess.Square, chess.Color], chess.Bitboard]:
        '''
        Pawns are color dependent as white moves up the board and black moves down the board
        '''
        moves_lookup = {}

        for color in chess.COLORS:
            for square, bb_square in zip(chess.SQUARES, chess.BB_SQUARES):

                if color == chess.WHITE:
                    if chess.BB_SQUARES[square] & chess.BB_RANK_1 != 0:
                        moves_lookup[square, color] = chess.BB_EMPTY
                    elif chess.BB_SQUARES[square] & chess.BB_RANK_2 != 0:
                        moves_lookup[square, color] = Moves.move_up(bb_square) | Moves.move_2_up(bb_square) | Moves.move_up_left(bb_square) | Moves.move_up_right(bb_square)
                    else:
                        moves_lookup[square, color] = Moves.move_up(bb_square) | Moves.move_up_left(bb_square) | Moves.move_up_right(bb_square)
                
                else:
                    if chess.BB_SQUARES[square] & chess.BB_RANK_8 != 0:
                        moves_lookup[square, color] = chess.BB_EMPTY
                    elif chess.BB_SQUARES[square] & chess.BB_RANK_7 != 0:
                        moves_lookup[square, color] = Moves.move_down(bb_square) | Moves.move_2_down(bb_square) | Moves.move_down_left(bb_square) | Moves.move_down_right(bb_square)
                    else:
                        moves_lookup[square, color] = Moves.move_down(bb_square) | Moves.move_down_left(bb_square) | Moves.move_down_right(bb_square)
        
        return moves_lookup

    move_lookup = generate_move_lookup()
