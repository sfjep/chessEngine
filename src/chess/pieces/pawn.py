from chess.pieces.piece import Piece
from chess.moves.move_utils import MoveUtils
from chess.utils import get_individual_ones_in_bb, get_square_int_from_bb
from chess.action import Action, ActionType
import chess

class Pawn(Piece):
    def __init__(self, bb, color, piece_type):
        super().__init__(bb, color, piece_type)
        self.generate_move_lookup()

    def generate_move_lookup(self):
        self.moves_lookup = {}
        for color in chess.COLORS:
            for square, bb_square in zip(chess.SQUARES, chess.BB_SQUARES):
                if color == chess.WHITE:
                    if (chess.BB_SQUARES[square] & chess.BB_RANK_1) != 0:
                        self.moves_lookup[square, color] = chess.BB_EMPTY
                    elif (chess.BB_SQUARES[square] & chess.BB_RANK_2) != 0:
                        self.moves_lookup[square, color] = MoveUtils.move_up(bb_square) | MoveUtils.move_2_up(bb_square) | MoveUtils.move_up_left(bb_square) | MoveUtils.move_up_right(bb_square)
                    else:
                        self.moves_lookup[square, color] = MoveUtils.move_up(bb_square) | MoveUtils.move_up_left(bb_square) | MoveUtils.move_up_right(bb_square)
                else:
                    if (chess.BB_SQUARES[square] & chess.BB_RANK_8) != 0:
                        self.moves_lookup[square, color] = chess.BB_EMPTY
                    elif (chess.BB_SQUARES[square] & chess.BB_RANK_7) != 0:
                        self.moves_lookup[square, color] = MoveUtils.move_down(bb_square) | MoveUtils.move_2_down(bb_square) | MoveUtils.move_down_left(bb_square) | MoveUtils.move_down_right(bb_square)
                    else:
                        self.moves_lookup[square, color] = MoveUtils.move_down(bb_square) | MoveUtils.move_down_left(bb_square) | MoveUtils.move_down_right(bb_square)


    def get_moves(self, state):
        pawn_moves = []
        pawn_attacks = []
        pawn_en_passants = []

        for current_piece_position in get_individual_ones_in_bb(self.bb):
            current_piece_index = get_square_int_from_bb(current_piece_position)
            attack_squares = self.diag_moves(current_piece_position, self.color) & (state.opponent_occupied | state.en_passant_capture_square)
            destination_squares = attack_squares
            en_passant_dest_squares = chess.BB_EMPTY
            if move_up := self.forward_move(current_piece_position, self.color) & ~(state.opponent_occupied | state.player_occupied):
                destination_squares |= move_up
                if current_piece_position & self.pawn_starting_rank(self.color):
                    if move_2_up := self.two_forward_move(current_piece_position, self.color) & ~(state.opponent_occupied | state.player_occupied):
                        en_passant_dest_squares |= move_2_up

            pawn_moves += Action.generate_actions(destination_squares, chess.PAWN, current_piece_index, state.turn, ActionType.MOVE)
            pawn_attacks += Action.generate_actions(attack_squares, chess.PAWN, current_piece_index, state.turn, ActionType.ATTACK)
            pawn_en_passants += Action.generate_actions(en_passant_dest_squares, chess.PAWN, current_piece_index, state.turn, ActionType.EN_PASSANT)

        # TODO: separate action generation for PROMOTIONS

        return pawn_moves, pawn_attacks

    @staticmethod
    def pawn_starting_rank(color):
        if color == chess.WHITE:
            return chess.BB_RANK_2
        else:
            return chess.BB_RANK_7

    @staticmethod
    def diag_moves(bb, color):
        if color == chess.WHITE:
            return MoveUtils.move_up_left(bb) | MoveUtils.move_up_right(bb)
        else:
            return MoveUtils.move_down_left(bb) | MoveUtils.move_down_right(bb)

    @staticmethod
    def forward_move(bb, color):
        if color == chess.WHITE:
            return MoveUtils.move_up(bb)
        else:
            return MoveUtils.move_down(bb)

    @staticmethod
    def two_forward_move(bb, color):
        if color == chess.WHITE:
            return MoveUtils.move_2_up(bb)
        else:
            return MoveUtils.move_2_down(bb)