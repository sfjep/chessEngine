from chess.state import State
import pygame as p
from chess.gui.gui import GUI


def main():
    state = State("rQbqk2r/pp1ppppp/8/2pPB2P/1P1pP3/8/PPP3PP/R1n1K1NR w KQkq c6 3 6")
    moves, attacks = state.get_possible_actions()

    print("Actions: ", moves)
    print("Attacks: ", attacks)
    gui = GUI()
    gui.run(state)

    # print(Fen.get_fen_from_state(state))
    # print(attack_actions)
    # state.board.print_board_from_board_obj()




if __name__ == '__main__':
    main()
