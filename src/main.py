from chess.board import Board
from chess.utils import print_bitboard
from chess.pieces.knight import Knight
import chess

if __name__ == '__main__':
    for square in chess.SQUARES:
        print_bitboard(Knight.moves_lookup[square])
        print("test")