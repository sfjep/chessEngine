import chess
from chess import utils
from chess.action import Action, ActionType
from chess.masking import mask_own_pieces, mask_opponent_pieces
from chess.moves.move_utils import pawn_diag_moves, pawn_starting_rank, pawn_one_step, pawn_two_step, SQUARE_XRAYS, MOVE_FUNCTION
from chess.utils import get_individual_ones_in_bb, get_square_int_from_bb

class MoveGenerator:

    def __init__(self, state, color):
        self.state = state
        self.color = color
        self.player_board = state.board.pieces[color]
        self.opponent_board = state.board.pieces[not(color)]
        self.player_occupied = self.player_board["PLAYER_OCCUPIED"]
        self.opponent_occupied = self.player_board["OPPONENT_OCCUPIED"]
        self.opponent_king = state.board.pieces[not(color)]["KING"].bb
        self.player_king = state.board.pieces[color]["KING"].bb
        
        self.moves = []

        self.in_check = False
        self.in_double_check = False
        self.pin_squares = chess.BB_EMPTY
        self.attacked_squares = chess.BB_EMPTY

        # dict mapping a single pinned piece's bb to the bb of the ray along which it is allowed to move
        self.pin_ray_map = {}

        self.compute_attack_map()

    def get_piece_moves(self):
        if self.in_double_check:
            self._get_king_moves()
            return
        
        self._get_pawn_moves()
        self._get_queen_moves()
        self._get_rook_moves()
        self._get_knight_moves()
        self._get_bishop_moves()
        self._get_king_moves()
        return self.moves
    
    def is_pinned(self, piece_bb):
        return piece_bb & self.pin_squares != 0
    
    def _get_pawn_moves(self):
        pawns = self.player_board["PAWN"]

        for single_pawn_bb in get_individual_ones_in_bb(pawns.bb):

            current_piece_index = get_square_int_from_bb(single_pawn_bb)
            attack_squares = pawn_diag_moves(single_pawn_bb, self.color) & (self.opponent_occupied)
            en_passant_dest_squares = pawn_diag_moves(single_pawn_bb, self.color) & (self.state.en_passant_capture_square)
            destination_squares = chess.BB_EMPTY
            if move_up := pawn_one_step(single_pawn_bb, self.color) & ~(self.player_occupied | self.opponent_occupied):
                destination_squares |= move_up
                if single_pawn_bb & pawn_starting_rank(self.color):
                    if move_2_up := pawn_two_step(single_pawn_bb, self.color) & ~(self.opponent_occupied | self.player_occupied):
                        destination_squares |= move_2_up

            if self.is_pinned(single_pawn_bb):
                pin_ray = self.pin_ray_map[single_pawn_bb]
                destination_squares &= pin_ray
                attack_squares &= pin_ray
                en_passant_dest_squares &= pin_ray

            promotion_rank = chess.BB_PROMOTION_RANK[self.color]
            self.moves += Action.generate_actions(destination_squares & ~attack_squares & ~promotion_rank, pawns, current_piece_index, ActionType.MOVE)
            self.moves += Action.generate_actions(attack_squares & ~promotion_rank & self.opponent_king, pawns, current_piece_index, ActionType.ATTACK, is_check=True)
            self.moves += Action.generate_actions(attack_squares & ~promotion_rank & ~self.opponent_king, pawns, current_piece_index, ActionType.ATTACK)
            self.moves += Action.generate_actions(en_passant_dest_squares, pawns, current_piece_index, ActionType.EN_PASSANT)
            self._get_promotion_moves(destination_squares | attack_squares, current_piece_index, pawns)

    def _get_promotion_moves(self, destination_squares, current_piece_index, pawns):
        promotion_ranks = chess.BB_PROMOTION_RANK[self.color]
        promotion_squares = destination_squares & promotion_ranks
        for promotion_square in get_individual_ones_in_bb(promotion_squares):
            self.moves += Action.generate_actions(promotion_square, pawns, current_piece_index, ActionType.PROMOTION, promotion_to=chess.KNIGHT)
            self.moves += Action.generate_actions(promotion_square, pawns, current_piece_index, ActionType.PROMOTION, promotion_to=chess.BISHOP)
            self.moves += Action.generate_actions(promotion_square, pawns, current_piece_index, ActionType.PROMOTION, promotion_to=chess.ROOK)
            self.moves += Action.generate_actions(promotion_square, pawns, current_piece_index, ActionType.PROMOTION, promotion_to=chess.QUEEN)

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
            destination_squares = knights.moves_lookup[square_int] & ~self.player_occupied & ~self.opponent_occupied
            attack_squares = knights.moves_lookup[square_int] & ~self.player_occupied & self.opponent_occupied
            
            if self.is_pinned(piece_bb):
                pin_ray = self.pin_ray_map[piece_bb]
                destination_squares &= pin_ray
                attack_squares &= pin_ray

            self.moves += Action.generate_actions(destination_squares, knights, square_int, ActionType.MOVE)
            self.moves += Action.generate_actions(attack_squares & ~self.opponent_king, knights, square_int, ActionType.ATTACK)
            self.moves += Action.generate_actions(attack_squares & self.opponent_king, knights, square_int, ActionType.ATTACK, is_check=True)

    def _get_bishop_moves(self):
        bishops = self.player_board["BISHOP"]
        directions = [
            (["UP_RIGHT", "UP_LEFT"], True),
            (["DOWN_RIGHT", "DOWN_LEFT"], False)
        ]
        return self._get_range_moves(bishops, directions)

    def _get_queen_moves(self):
        queen = self.player_board["QUEEN"]
        directions = [
            (["UP_RIGHT", "RIGHT", "UP", "UP_LEFT"], True),
            (["DOWN_RIGHT", "DOWN", "LEFT", "DOWN_LEFT"], False)
        ]
        return self._get_range_moves(queen, directions)

    def _get_king_moves(self):
        king = self.player_board["KING"]

        square_int = get_square_int_from_bb(king.bb)
        destination_squares = king.moves_lookup[(square_int, self.color)] & ~self.player_occupied & ~self.opponent_occupied
        kingside_castles_bb, queenside_castles_bb = self._add_castling()

        king_attack_squares = king.moves_lookup[(square_int, self.color)] & ~self.player_occupied & self.opponent_occupied

        # do not let friendly king move to a square attacked by opponent
        destination_squares &= ~self.attacked_squares
        king_attack_squares &= ~self.attacked_squares

        self.moves += Action.generate_actions(destination_squares, king, square_int, ActionType.MOVE)
        self.moves += Action.generate_actions(king_attack_squares, king, square_int, ActionType.ATTACK)

        if not(self.in_check):
            self.moves += Action.generate_actions(queenside_castles_bb, king, square_int, ActionType.CASTLING, is_long_castles=True)
            self.moves += Action.generate_actions(kingside_castles_bb, king, square_int, ActionType.CASTLING, is_long_castles=False)


    def _add_castling(self):
        # Cannot castle when in check
        if not self.in_check:
            kingside_castles_bb = chess.BB_EMPTY
            queenside_castles_bb = chess.BB_EMPTY
            if self.state.can_castle_queenside[self.color] and self._queenside_castling_squares_empty():
                queenside_castles_bb = chess.QUEENSIDE_CASTLE_SQUARE[self.color]
            if self.state.can_castle_kingside[self.color] and self._kingside_castling_squares_empty():
                kingside_castles_bb = chess.KINGSIDE_CASTLE_SQUARE[self.color]
            return kingside_castles_bb, queenside_castles_bb
        return chess.BB_EMPTY, chess.BB_EMPTY

    def _queenside_castling_squares_empty(self):
        return (chess.BB_QUEENSIDE_CASTLE_SQUARES[self.color] & (self.opponent_occupied | self.player_occupied)) == chess.BB_EMPTY

    def _kingside_castling_squares_empty(self):
        return (chess.BB_KINGSIDE_CASTLE_SQUARES[self.color] & (self.opponent_occupied | self.player_occupied)) == chess.BB_EMPTY

    def _get_range_moves(self, piece, directions: list, compute_slide_attacks=False):
        # if opponent_attacks is True, we are calculating attack squares by opponent sliding pieces, so we swap opponent and player pieces
        # Else we are computing friendly pieces moves
        moving_pieces = self.player_occupied if not compute_slide_attacks else self.opponent_occupied
        opponent_pieces = self.opponent_occupied if not compute_slide_attacks else self.player_occupied


        for piece_bb in get_individual_ones_in_bb(piece.bb):

            piece_square = get_square_int_from_bb(piece_bb)
            destination_squares = piece.moves_lookup[piece_square]

            for direction, mask_upwards in directions:

                if not compute_slide_attacks:
                    destination_squares &= ~mask_own_pieces(piece_square, direction, moving_pieces, mask_upwards)
                    destination_squares &= ~mask_opponent_pieces(piece_square, direction, opponent_pieces, mask_upwards)
                
                # when computing sliding attacks, the sliding piece should be considered allowed to get to a space occupied by pieces of its color
                # e.g. assume friendly king eats opponent piece, and this square is attacked by sliding piece,
                # then the king shouldn't be allowed to move there (square should be part of attacked_squares)
                # therefore we mask both friendly and opponent pieces as opponent pieces (such that the slider can reach the square in both cases)
                else:
                    destination_squares &= ~mask_opponent_pieces(piece_square, direction, moving_pieces, mask_upwards)
                    destination_squares &= ~mask_opponent_pieces(piece_square, direction, opponent_pieces, mask_upwards)

            if not compute_slide_attacks and self.is_pinned(piece_bb):
                # only allow piece to move along pin ray
                pin_ray = self.pin_ray_map[piece_bb]
                destination_squares &= pin_ray

            # only append to move list if we are computing moves for friendly pieces
            if not compute_slide_attacks:
                self.moves += Action.generate_actions(destination_squares & ~self.opponent_occupied, piece, piece_square, ActionType.MOVE)
                self.moves += Action.generate_actions(destination_squares & self.opponent_occupied & ~self.opponent_king, piece, piece_square, ActionType.ATTACK)
                self.moves += Action.generate_actions(destination_squares & self.opponent_occupied & self.opponent_king, piece, piece_square, ActionType.ATTACK, is_check=True)

            # otherwise append destination squares to attacked_squares
            else:
                self.attacked_squares |= destination_squares


    def compute_slider_attacks(self):
        opponent_bishops = self.opponent_board["BISHOP"]
        directions = [
            (["UP_RIGHT", "UP_LEFT"], True),
            (["DOWN_RIGHT", "DOWN_LEFT"], False)
        ]
        self._get_range_moves(opponent_bishops, directions, compute_slide_attacks=True)

        opponent_queen = self.opponent_board["QUEEN"]
        directions = [
            (["UP_RIGHT", "RIGHT", "UP", "UP_LEFT"], True),
            (["DOWN_RIGHT", "DOWN", "LEFT", "DOWN_LEFT"], False)
        ]
        self._get_range_moves(opponent_queen, directions, compute_slide_attacks=True)

        opponent_rooks = self.opponent_board["ROOK"]
        move_ranges = [
            (["UP", "RIGHT"], True),
            (["LEFT", "DOWN"], False)
        ]
        self._get_range_moves(opponent_rooks, move_ranges, compute_slide_attacks=True)


    def is_diagonal(self, direction: str):
        # TODO: make Enum/global variables with directions
        diag_directions = ["UP_RIGHT", "UP_LEFT", "DOWN_RIGHT", "DOWN_LEFT"]
        return direction in diag_directions

    def compute_attack_map(self):
        # sliders attacks
        self.compute_slider_attacks()

        # check for pinned pieces, walking in every direction from friendly king
        opponent_diag_sliders = self.opponent_board["QUEEN"].bb | self.opponent_board["BISHOP"].bb
        opponent_ortho_sliders = self.opponent_board["QUEEN"].bb | self.opponent_board["ROOK"].bb

        directions = ["RIGHT", "UP", "DOWN", "LEFT", "UP_RIGHT", "UP_LEFT", "DOWN_RIGHT", "DOWN_LEFT"]

        king = self.player_board["KING"]
        king_square = get_square_int_from_bb(king.bb)

        for direction in directions:
            attackers = opponent_diag_sliders if self.is_diagonal(direction) else opponent_ortho_sliders

            # only walk through x-ray if there is an opponent sliding piece on it
            if SQUARE_XRAYS[king_square][direction] & attackers != 0:

                # get function to move one square in a given direction
                move = MOVE_FUNCTION[direction]

                friendly_piece_count = 0
                opponent_piece_count = 0
                possible_pin_square = 0
                pin_ray = 0
                
                square_bb = king.bb
                while (square_bb := move(square_bb)) != 0 :
                    pin_ray |= square_bb

                    if square_bb & self.player_occupied != 0:
                        friendly_piece_count += 1
                        # found a friendly piece between king and attacker, saving as possible pin
                        possible_pin_square = square_bb

                    # attackers are not counted when checking for pieces between king - attacker
                    if square_bb & self.opponent_occupied & ~attackers != 0:
                        opponent_piece_count += 1

                    if square_bb & attackers != 0:
                        # finding attacking opponent piece and no friendly piece in between means we have a check
                        if friendly_piece_count == 0:
                            self.in_double_check = self.in_check # if we were already in check, now we are in double check
                            self.in_check = True

                        # one friendly piece found between king and attacker -> the friendly piece found previously is pinned
                        elif friendly_piece_count == 1 and opponent_piece_count == 0:
                            self.pin_squares |= possible_pin_square
                            self.pin_ray_map[possible_pin_square] = pin_ray

                        # exit loop as soon as attacker is found when walking from friendly king
                        break

            # exit loop, as only the king can move in a double check
            if self.in_double_check:
                break

        # knight attacks
        opponent_knights = self.opponent_board["KNIGHT"]
        for knight_bb in get_individual_ones_in_bb(opponent_knights.bb):
            square_int = get_square_int_from_bb(knight_bb)
            knight_attack_squares = opponent_knights.moves_lookup[square_int]
            self.attacked_squares |= knight_attack_squares
            if knight_attack_squares & king.bb != 0:
                self.in_double_check = self.in_check
                self.in_check = True

        # pawn attacks
        opponent_pawns = self.opponent_board["PAWN"]
        for pawn_bb in get_individual_ones_in_bb(opponent_pawns.bb):
            pawn_attack_squares = pawn_diag_moves(pawn_bb, not self.color)
            self.attacked_squares |=  pawn_attack_squares
            if pawn_attack_squares & king.bb != 0:
                self.in_double_check = self.in_check
                self.in_check = True





