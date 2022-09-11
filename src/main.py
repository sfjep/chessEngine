from chess.board import Board
from chess.pieces.knight import Knight
from chess.state import State
from chess.fen import Fen
import chess


if __name__ == '__main__':
    state = State("rnbqkbnr/pp1ppppp/8/2p5/3PP3/5N2/PPP2PPP/RNBQKB1R b KQkq e3 1 2")
    print(Fen.get_fen_from_state(state))
    pawn_actions, attack_actions = state.board.BP.get_moves(
        chess.BLACK,
        state.board.white_occupied,
        state.board.black_occupied,
        state.en_passant_capture_square
    )
    print(pawn_actions)
    print(attack_actions)
    state.board.print_board_from_board_obj()
