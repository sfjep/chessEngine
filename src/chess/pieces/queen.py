from typing import Dict, Tuple
import chess
from chess.moves import Moves
from chess.pieces.piece import Piece
import chess.utils as utils
from chess.action import Action


class Queen(Piece):
    def __init__(self, bb, color, piece_type):
        super().__init__(bb, color, piece_type)

    def generate_move_lookup() -> Dict[Tuple[chess.Square, chess.Color], chess.Bitboard]:
        moves_lookup = {}

        for square, bb_square in zip(chess.SQUARES, chess.BB_SQUARES):
            moves_lookup[square] = (
                ((utils.get_rank_from_bb(bb_square) | utils.get_file_from_bb(bb_square)) & ~bb_square) |
                Moves.move_down_left_full_range(bb_square) |
                Moves.move_down_right_full_range(bb_square) |
                Moves.move_up_left_full_range(bb_square) |
                Moves.move_up_right_full_range(bb_square)
            )

        return moves_lookup

    MOVES_LOOKUP = generate_move_lookup()

    def get_moves(self, opponent_occupied: chess.Bitboard, player_occupied: chess.Bitboard):
        queen_actions = []
        attack_actions = []

        for current_piece_position in utils.get_individual_ones_in_bb(self.bb):
            square_int = utils.get_square_int_from_bb(current_piece_position)
            moves = Queen.MOVES_LOOKUP[square_int]

            for move_range in [
                Moves.move_up_right_full_range,
                Moves.move_up_left_full_range,
                Moves.move_up_full_range,
                Moves.move_right_full_range
            ]:
                moves &= ~utils.mask_up_own_pieces(move_range(current_piece_position), player_occupied)
            for move_range in [
                Moves.move_down_left_full_range,
                Moves.move_left_full_range,
                Moves.move_down_right_full_range,
                Moves.move_down_full_range
            ]:
                moves &= ~utils.mask_down_own_pieces(move_range(current_piece_position), player_occupied)
            # moves = moves & ~up_right_mask & ~up_left_mask & ~up_mask

            # Mask out downward moves (left, down, downleft)
            # mask = get_rank_from_bb(current_piece_position)
                    # | get_file_from_bb(current_piece_position)) & player_occupied

            # mask |= (
            #     (Moves.move_down_left_full_range(current_piece_position) & player_occupied) |
            #     (Moves.move_down_right_full_range(current_piece_position) & player_occupied) |
            #     (Moves.move_up_left_full_range(current_piece_position) & player_occupied) |
            #     (Moves.move_up_right_full_range(current_piece_position) & player_occupied)
            # )
            # # moves &= ~mask

            # moves = chess.BB_EMPTY
            # attack_moves = chess.BB_EMPTY
            # move_generator = [
            #     Moves.move_up,
            #     Moves.move_down,
            #     Moves.move_left,
            #     Moves.move_right,
            #     Moves.move_down_left,
            #     Moves.move_down_right,
            #     Moves.move_up_left,
            #     Moves.move_up_right
            # ]
            # for next_move in move_generator:
            #     continue_in_direction = True
            #     next_square = current_piece_position
            #     while continue_in_direction:
            #         next_square = next_move(next_square)
            #         if not next_square & chess.BB_ALL:
            #             continue_in_direction = False
            #         elif next_square & player_occupied:
            #             continue_in_direction = False
            #         else:
            #             moves |= next_square
            #             if moves & opponent_occupied:
            #                 attack_moves |= next_square
            #                 continue_in_direction = False

            # queen_actions += Action.generate_actions(moves, chess.QUEEN, current_piece_position)
            # attack_actions += Action.generate_actions(attack_moves, chess.QUEEN, current_piece_position)

        return queen_actions, attack_actions

