from chess.board import Board
from chess.pieces.knight import Knight
from chess.state import State
from chess.fen import Fen
import chess
import pygame as p
from chess.gui import GUI



def main():
    gui = GUI()
    state = State("r1bqkbnr/pp1ppppp/2n5/7P/3pP3/5N2/PPP3PP/2BQKB1R w KQkq - 3 6")
    gui.load_images()
    gui.run(state.board)

    # print(Fen.get_fen_from_state(state))
    queen_actions, attack_actions = state.board.WQ.get_moves(
        state.board.black_occupied,
        state.board.white_occupied,
    )
    print(queen_actions)
    # print(attack_actions)
    # state.board.print_board_from_board_obj()




if __name__ == '__main__':
    main()
