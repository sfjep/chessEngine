from chess.board import Board
from chess.pieces.knight import Knight
from chess.state import State
import chess

if __name__ == '__main__':
    state = State("rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq e3 1 2")
    print(state.get_fen_from_state())
    pawn_actions, attack_actions = state.board.WP.get_moves(
        chess.WHITE, 
        state.BLACK_OCCUPIED, 
        state.WHITE_OCCUPIED, 
        state.en_passant_capture_bb
    )
    # print(pawn_actions)
    # print(attack_actions)