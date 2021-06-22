from chess.pieces.piece import Piece
from chess.moves import Moves
import chess

class Pawn(Piece):
    def __init__(self, bb, color):
        super().__init__(bb, color)

    def generate_move_lookup(self):
        '''
        Pawns are color dependent as white moves up the board and black moves down the board
        '''
        self.moves_lookup = {}

        for square in chess.SQUARES:

            if self.color == chess.COLORS[0]:
                if chess.BB_SQUARES[square] & chess.BB_RANK_1 != 0:
                    self.moves_lookup[square] = chess.BB_EMPTY
                elif chess.BB_SQUARES[square] & chess.BB_RANK_2 != 0:
                    self.moves_lookup[square] += Moves.move_up(self.bb) | Moves.move_2_up(self.bb) | Moves.move_up_left(self.bb) | Moves.move_up_right(self.bb)
                else:
                    self.moves_lookup[square] = Moves.move_up(self.bb) | Moves.move_up_left(self.bb) | Moves.move_up_right(self.bb)
            
            else:
                if chess.BB_SQUARES[square] & chess.BB_RANK_8 != 0:
                    self.moves_lookup[square] = chess.BB_EMPTY
                elif chess.BB_SQUARES[square] & chess.BB_RANK_7 != 0:
                    self.moves_lookup[square] = Moves.move_down(self.bb) | Moves.move_2_down(self.bb) | Moves.move_up_left(self.bb) | Moves.move_up_right(self.bb)
                else:
                    self.moves_lookup[square] = Moves.move_down(self.bb) | Moves.move_up_left(self.bb) | Moves.move_up_right(self.bb)
