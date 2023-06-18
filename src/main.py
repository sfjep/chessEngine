from chess.state import State
import pygame as p
from chess.gui.gui import GUI
from chess.state import State

def main():
    # start_game("rQbqk2r/pp1ppppp/8/2pPB2P/1P1pP3/8/PPP3PP/R1n1K1NR w KQkq c6 3 6")
    state = State("3k4/8/3p4/8/1p3P2/3R4/3P4/4K3 w - - 0 1")
    state.get_possible_actions()

    print("Moves: ", state.possible_actions.moves)
    print("Attacks: ", state.possible_actions.attacks)
    print("Castles: ", state.possible_actions.castles)
    print("Promo: ", state.possible_actions.promotions)

    gui = GUI()
    gui.run(state)

    # print(Fen.get_fen_from_state(state))
    # print(attack_actions)
    # state.board.print_board_from_board_obj()




if __name__ == '__main__':
    main()
