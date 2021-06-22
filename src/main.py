from chess.board import Board
from chess.utils import printBitboard

if __name__ == '__main__':
    board = Board()
    for bb in Board.piece_squares(board.BB.bb):
        printBitboard(bb)
        print()

    print("Hello")