from chess.state import State
import pygame as p
from chess.gui.gui import GUI
import sys


def main():
    gui = GUI()
    state = State("r1bqkbnr/pp1ppppp/2n5/7P/1P1pP1Q1/8/PPP3PP/2B1KB1R w KQkq - 3 6")
    
    while True:
        gui.show_background(gui.screen)

        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                sys.exit()
            
            p.display.update()
    

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
