from chess.state import State
import pygame as p
from chess.gui.gui import GUI


def main():
    state = State("rQbqkbnr/pp1ppppp/2n5/7P/1P1pP3/8/PPP3PP/2B1KB1R w KQkq - 3 6")
    queen_actions, attack_actions = state.board.WQ.get_moves(
        state.board.black_occupied,
        state.board.white_occupied,
    )
    print("Queen actions: ", queen_actions)
    print("Queen attacks: ", attack_actions)
    # gui = GUI()
    # gui.run(state)




    # print(Fen.get_fen_from_state(state))
    # print(attack_actions)
    # state.board.print_board_from_board_obj()




if __name__ == '__main__':
    main()
