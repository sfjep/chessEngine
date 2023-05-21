import chess
from chess.action import Action, ActionType
from chess.masking import mask_own_pieces, mask_opponent_pieces
from chess.moves.move_utils import pawn_diag_moves, pawn_starting_rank, pawn_one_step, pawn_two_step
from chess.utils import get_individual_ones_in_bb, get_square_int_from_bb


class MoveGenerator:
    def __init__(self, state):
        self.state = state
        self.color = state.turn
        self.player_board = state.board.pieces[self.color]
        self.player_occupied = self.player_board['PLAYER_OCCUPIED']
        self.opponent_occupied = self.player_board['OPPONENT_OCCUPIED']
        self.moves = []
        self.attacks = []

    def get_piece_moves(self):
        self._get_pawn_moves()
        self._get_queen_moves()
        self._get_rook_moves()
        self._get_knight_moves()
        self._get_bishop_moves()
        self._get_king_moves()
        return self.moves, self.attacks

    def _get_pawn_moves(self):
        pawns = self.player_board["PAWN"]

        for current_piece_position in get_individual_ones_in_bb(pawns.bb):
            current_piece_index = get_square_int_from_bb(current_piece_position)
            attack_squares = pawn_diag_moves(current_piece_position, self.color) & (self.opponent_occupied)
            en_passant_dest_squares = pawn_diag_moves(current_piece_position, self.color) & (self.state.en_passant_capture_square)
            destination_squares = chess.BB_EMPTY
            if move_up := pawn_one_step(current_piece_position, self.color) & ~(self.player_occupied | self.opponent_occupied):
                destination_squares |= move_up
                if current_piece_position & pawn_starting_rank(self.color):
                    if move_2_up := pawn_two_step(current_piece_position, self.color) & ~(self.opponent_occupied | self.player_occupied):
                        destination_squares |= move_2_up

            self.moves += Action.generate_actions(destination_squares, pawns, current_piece_index, ActionType.MOVE)
            self.attacks += Action.generate_actions(attack_squares, pawns, current_piece_index, ActionType.ATTACK)
            self.attacks += Action.generate_actions(en_passant_dest_squares, pawns, current_piece_index, ActionType.EN_PASSANT)

        # TODO: separate action generation for PROMOTIONS


    def _get_rook_moves(self):
        rooks = self.player_board["ROOK"]
        move_ranges = [
            (["UP", "RIGHT"], True),
            (["LEFT", "DOWN"], False)
        ]
        return self._get_range_moves(rooks, move_ranges)

    def _get_knight_moves(self):
        knights = self.player_board["KNIGHT"]

        for piece_bb in get_individual_ones_in_bb(knights.bb):
            square_int = get_square_int_from_bb(piece_bb)
            destination_squares = knights.moves_lookup[square_int] & ~self.player_occupied
            attack_moves = knights.moves_lookup[square_int] & ~self.player_occupied & self.opponent_occupied

            self.moves += Action.generate_actions(destination_squares, knights, square_int, ActionType.MOVE)
            self.attacks += Action.generate_actions(attack_moves, knights, square_int, ActionType.ATTACK)

    def _get_bishop_moves(self):
        bishops = self.player_board["BISHOP"]
        move_ranges = [
            (["UP_RIGHT", "UP_LEFT"], True),
            (["DOWN_RIGHT", "DOWN_LEFT"], False)
        ]
        return self._get_range_moves(bishops, move_ranges)

    def _get_queen_moves(self):
        queen = self.player_board["QUEEN"]
        move_ranges = [
            (["UP_RIGHT", "RIGHT", "UP", "UP_LEFT"], True),
            (["DOWN_RIGHT", "DOWN", "LEFT", "DOWN_LEFT"], False)
        ]
        return self._get_range_moves(queen, move_ranges)

    def _get_king_moves(self):
        king = self.player_board["KING"]

        for current_piece_position_bb in get_individual_ones_in_bb(king.bb):
            square_int = get_square_int_from_bb(current_piece_position_bb)
            destination_squares = king.moves_lookup[(square_int, self.color)] & ~self.player_occupied
            castling_squares = self._add_castling()

            attack_squares = king.moves_lookup[(square_int, self.color)] & ~self.player_occupied & self.opponent_occupied

            self.moves += Action.generate_actions(destination_squares, king, square_int, ActionType.MOVE)
            self.moves += Action.generate_actions(castling_squares, king, square_int, ActionType.CASTLING)
            self.attacks += Action.generate_actions(attack_squares, king, square_int, ActionType.ATTACK)

    def _add_castling(self):
        castles_bb = chess.BB_EMPTY
        if self.state.can_castle_queenside[self.color] and self._queenside_castling_squares_empty():
            castles_bb += chess.QUEENSIDE_CASTLE_SQUARE[self.color]
        if self.state.can_castle_kingside[self.color] and self._kingside_castling_squares_empty():
            castles_bb += chess.KINGSIDE_CASTLE_SQUARE[self.color]
        return castles_bb

    def _queenside_castling_squares_empty(self):
        return (chess.BB_QUEENSIDE_CASTLE_SQUARES[self.color] & (self.opponent_occupied | self.player_occupied)) == chess.BB_EMPTY

    def _kingside_castling_squares_empty(self):
        return (chess.BB_KINGSIDE_CASTLE_SQUARES[self.color] & (self.opponent_occupied | self.player_occupied)) == chess.BB_EMPTY

    def _get_range_moves(self, piece, move_ranges: list):
        for piece_bb in get_individual_ones_in_bb(piece.bb):
            piece_pos_int = get_square_int_from_bb(piece_bb)
            destination_squares = piece.moves_lookup[piece_pos_int]

            for move_range, mask_upwards in move_ranges:
                destination_squares &= ~mask_own_pieces(piece_pos_int, move_range, self.player_occupied, mask_upwards)
                destination_squares &= ~mask_opponent_pieces(piece_pos_int, move_range, self.opponent_occupied, mask_upwards)

            # TODO: Take out attack moves from of the self.moves list
            self.moves += Action.generate_actions(destination_squares, piece, piece_pos_int, ActionType.MOVE)
            self.attacks += Action.generate_actions(destination_squares & self.opponent_occupied, piece, piece_pos_int, ActionType.ATTACK)



"""
In check?

Castles?
    # Has moved?
    # Rook moved?
    # Squares in between occupied?
    # Squres in between attacked?
    # In check?

If BB_BLACK_ATTACKED & BB_WHITE_KING != 0:
    Check pinned
"""
