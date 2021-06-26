from chess.board import Board
from chess.utils import printBitboard

if __name__ == '__main__':
    board = Board()
    test = [bb for bb in Board.piece_squares(board.BB.bb)]
    for bb in test:
        printBitboard(bb)
        print("")
    print("Hello")