from chess.board import Board
from chess.utils import print_board_from_board_obj
from chess.pieces.knight import Knight
from chess.state import State
import chess

if __name__ == '__main__':
    # board = Board()
    # print_board_from_board_obj(board)
    
    state = State()
    state.get_initial_state()
    pawn_actions, attack_actions = state.board.WP.get_moves(chess.WHITE, state.BLACK_OCCUPIED, state.WHITE_OCCUPIED, state.en_passant_capture_bb)
    print(pawn_actions)
    print(attack_actions)