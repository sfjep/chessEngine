from chess.state import State
import pygame as p
from chess.gui.gui import GUI
from chess.state import State

def main():
    # start_game("rQbqk2r/pp1ppppp/8/2pPB2P/1P1pP3/8/PPP3PP/R1n1K1NR w KQkq c6 3 6")
    state = State("rQbqk2r/pp1pppPp/8/2pPB2P/1P1pP3/8/PPP3PP/R3K2R w KQkq c6 3 6")
    state.get_possible_actions()

    print("Moves: ", state.moves)
    print("Attacks: ", state.attacks)
    print("Castles: ", state.castles)
    print("Promo: ", state.promotion)

    gui = GUI()
    gui.run(state)

    # print(Fen.get_fen_from_state(state))
    # print(attack_actions)
    # state.board.print_board_from_board_obj()




if __name__ == '__main__':
    main()
