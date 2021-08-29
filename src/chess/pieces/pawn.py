from typing import Dict, Tuple
from chess.pieces.piece import Piece
from chess.moves import Moves
from chess.utils import get_individual_ones_in_bb, get_square_int_from_bb
from chess.action import Action
import chess

class Pawn(Piece):
    def __init__(self, bb, color, piece_type):
        super().__init__(bb, color, piece_type)

    def generate_move_lookup() -> Dict[Tuple[chess.Square, chess.Color], chess.Bitboard]:
        '''
        Pawns are color dependent as white moves up the board and black moves down the board
        Never to be needed
        '''
        moves_lookup = {}

        for color in chess.COLORS:
            for square, bb_square in zip(chess.SQUARES, chess.BB_SQUARES):

                if color == chess.WHITE:
                    if chess.BB_SQUARES[square] & chess.BB_RANK_1 != 0:
                        moves_lookup[square, color] = chess.BB_EMPTY
                    elif chess.BB_SQUARES[square] & chess.BB_RANK_2 != 0:
                        moves_lookup[square, color] = Moves.move_up(bb_square) | Moves.move_2_up(bb_square) | Moves.move_up_left(bb_square) | Moves.move_up_right(bb_square)
                    else:
                        moves_lookup[square, color] = Moves.move_up(bb_square) | Moves.move_up_left(bb_square) | Moves.move_up_right(bb_square)
                
                else:
                    if chess.BB_SQUARES[square] & chess.BB_RANK_8 != 0:
                        moves_lookup[square, color] = chess.BB_EMPTY
                    elif chess.BB_SQUARES[square] & chess.BB_RANK_7 != 0:
                        moves_lookup[square, color] = Moves.move_down(bb_square) | Moves.move_2_down(bb_square) | Moves.move_down_left(bb_square) | Moves.move_down_right(bb_square)
                    else:
                        moves_lookup[square, color] = Moves.move_down(bb_square) | Moves.move_down_left(bb_square) | Moves.move_down_right(bb_square)
        
        return moves_lookup

    move_lookup = generate_move_lookup()

    def get_moves(self, color: bool, opponent_occupied: chess.Bitboard, player_occupied: chess.Bitboard, en_passant_bb: chess.Bitboard):
        for current_piece_position in get_individual_ones_in_bb(self.bb):
            attack_mask = self.diag_moves(current_piece_position, color) & (opponent_occupied | en_passant_bb)
            target_squares = attack_mask
            move_up = self.forward_move(current_piece_position, color) & ~(opponent_occupied | player_occupied)
            if move_up:
                target_squares |= move_up
                if current_piece_position & self.pawn_starting_rank(color):
                    move_2_up = self.two_forward_move(current_piece_position, color) & ~(opponent_occupied | player_occupied)
                    if move_2_up:
                        target_squares |= move_2_up

            pawn_actions = Action.generate_actions(target_squares, chess.PAWN, current_piece_position)
            attack_actions = Action.generate_actions(attack_mask, chess.PAWN, current_piece_position)

        return pawn_actions, attack_actions

    @staticmethod
    def pawn_starting_rank(color):
        if color == chess.WHITE:
            return chess.BB_RANK_2
        else:
            return chess.BB_RANK_7
    
    @staticmethod
    def diag_moves(bb, color):
        if color == chess.WHITE:
            return Moves.move_up_left(bb) | Moves.move_up_right(bb)
        else:
            return Moves.move_down_left(bb) | Moves.move_down_right(bb)

            # masks

    @staticmethod
    def forward_move(bb, color):
        if color == chess.WHITE:
            return Moves.move_up(bb)
        else:
            return Moves.move_down(bb)

    @staticmethod
    def two_forward_move(bb, color):
        if color == chess.WHITE:
            return Moves.move_2_up(bb)
        else:
            return Moves.move_2_down(bb)