from chess.state import State
import pygame as p
from chess.gui.gui import GUI


def main():
    state = State("r1bqkbnr/pp1ppppp/2n5/7P/1P1pP1Q1/8/PPP3PP/2B1KB1R w KQkq - 3 6")
    gui = GUI()
    gui.run(state)




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
