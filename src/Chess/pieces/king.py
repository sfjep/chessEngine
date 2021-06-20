from chess.pieces.piece import Piece

class King(Piece):


    def __init__(self, bb, color):
        super().__init__(bb, color)

    def getMovesLookupDict(self):
        pass    

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