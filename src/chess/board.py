import numpy as np
from typing import Dict

import chess
import chess.pieces as Pieces
from chess.action import Action, ActionType
from chess.pieces.piece import Piece
from chess.utils import get_individual_ones_in_bb, get_square_int_from_bb, get_bb_from_square_int, get_square_name_from_bb, typename, print_bitboard
from chess.moves.move_utils import move_down, move_up

class Board:
    WP: Piece
    WR: Piece
    WN: Piece
    WB: Piece
    WQ: Piece
    WK: Piece
    BP: Piece
    BR: Piece
    BN: Piece
    BB: Piece
    BQ: Piece
    BK: Piece

    white_occupied: chess.Bitboard
    black_occupied: chess.Bitboard
    all_occupied: chess.Bitboard
    white_pieces: list
    black_pieces: list
    pieces: list

    char_to_piece: Dict[str, Piece]

    def __init__(self, fen_board: str = None):
        self.fen_board = fen_board
        self._create_pieces()

        self.char_to_piece = {
            "P": self.WP,
            "R": self.WR,
            "N": self.WN,
            "B": self.WB,
            "Q": self.WQ,
            "K": self.WK,
            "p": self.BP,
            "r": self.BR,
            "n": self.BN,
            "b": self.BB,
            "q": self.BQ,
            "k": self.BK,
        }

        if not fen_board:
            self._set_board_to_start_position()
        else:
            self._set_board_from_fen(fen_board)

        self._set_helper_bitboards()
        self._set_board_chararray()

    def __repr__(self):
        return f"{typename(self)}(fen_board={self.fen_board})"

    def _create_pieces(self):
        self.WP = Pieces.Pawn(chess.BB_EMPTY, chess.WHITE)
        self.WR = Pieces.Rook(chess.BB_EMPTY, chess.WHITE)
        self.WN = Pieces.Knight(chess.BB_EMPTY, chess.WHITE)
        self.WB = Pieces.Bishop(chess.BB_EMPTY, chess.WHITE)
        self.WQ = Pieces.Queen(chess.BB_EMPTY, chess.WHITE)
        self.WK = Pieces.King(chess.BB_EMPTY, chess.WHITE)
        self.BP = Pieces.Pawn(chess.BB_EMPTY, chess.BLACK)
        self.BR = Pieces.Rook(chess.BB_EMPTY, chess.BLACK)
        self.BN = Pieces.Knight(chess.BB_EMPTY, chess.BLACK)
        self.BB = Pieces.Bishop(chess.BB_EMPTY, chess.BLACK)
        self.BQ = Pieces.Queen(chess.BB_EMPTY, chess.BLACK)
        self.BK = Pieces.King(chess.BB_EMPTY, chess.BLACK)

    def _set_board_to_start_position(self):
        self.WP.bb = chess.BB_RANK_2
        self.WR.bb = chess.BB_A1 | chess.BB_H1
        self.WN.bb = chess.BB_B1 | chess.BB_G1
        self.WB.bb = chess.BB_C1 | chess.BB_F1
        self.WQ.bb = chess.BB_D1
        self.WK.bb = chess.BB_E1

        self.BP.bb = chess.BB_RANK_7
        self.BN.bb = chess.BB_B8 | chess.BB_G8
        self.BR.bb = chess.BB_A8 | chess.BB_H8
        self.BB.bb = chess.BB_C8 | chess.BB_F8
        self.BQ.bb = chess.BB_D8
        self.BK.bb = chess.BB_E8


    def _set_board_from_fen(self, fen_board: str):
        fen = fen_board.split("/")
        if len(fen) != 8:
            raise InvalidFenException
        blank_spaces = "1234567"
        # enumerating ranks from 7 to 0, as fen starts from black to white
        for rank, rank_content in zip(range(7, -1, -1), fen):
            if rank_content != "8":
                file_count = 0
                for char in rank_content:
                    if char in blank_spaces:
                        file_count += int(char)
                    else:
                        self.char_to_piece[char].bb |= chess.BB_SQUARES[
                            rank * 8 + file_count
                        ]
                        file_count += 1
                    if file_count > 8:
                        raise InvalidFenException

    def _set_helper_bitboards(self):
        self.white_occupied = (
            self.WP.bb | self.WR.bb | self.WB.bb | self.WN.bb | self.WQ.bb | self.WK.bb
        )
        self.black_occupied = (
            self.BP.bb | self.BR.bb | self.BB.bb | self.BN.bb | self.BQ.bb | self.BK.bb
        )
        self.all_occupied = self.white_occupied | self.black_occupied
        self.white_pieces = [self.WP, self.WN, self.WB, self.WR, self.WQ, self.WK]
        self.black_pieces = [self.BP, self.BN, self.BB, self.BR, self.BQ, self.BK]
        self.all_pieces = self.white_pieces + self.black_pieces

        self.pieces = {
            chess.WHITE : {
                "PLAYER_OCCUPIED": self.white_occupied,
                "OPPONENT_OCCUPIED": self.black_occupied,
                "PLAYER_PIECES": self.white_pieces,
                "OPPONENT_PIECES": self.black_pieces,
                "PAWN" : self.WP,
                "ROOK" : self.WR,
                "BISHOP" : self.WB,
                "KNIGHT" : self.WN,
                "QUEEN" : self.WQ,
                "KING" : self.WK
            },
            chess.BLACK : {
                "PLAYER_OCCUPIED": self.black_occupied,
                "OPPONENT_OCCUPIED": self.white_occupied,
                "PLAYER_PIECES": self.black_pieces,
                "OPPONENT_PIECES": self.white_pieces,
                "PAWN" : self.BP,
                "ROOK" : self.BR,
                "BISHOP" : self.BB,
                "KNIGHT" : self.BN,
                "QUEEN" : self.BQ,
                "KING" : self.BK
            }
        }


    @staticmethod
    def get_individual_piece_bb(bb_pieces: chess.Bitboard):
        """
        Generates 1 bit bitboards from the decomposition of a bitboard
        """
        while bb_pieces != 0:
            most_sig_bit = 2 ** (bb_pieces.bit_length() - 1)
            yield most_sig_bit
            bb_pieces ^= most_sig_bit

    def _set_board_chararray(self):
        self.board_arr = np.full([8, 8], " ", dtype=object)
        for piece in self.all_pieces:
            for bb in get_individual_ones_in_bb(piece.bb):
                idx = get_square_int_from_bb(bb)
                if piece.color == chess.WHITE:
                    self.board_arr[idx // 8, idx % 8] = f"W{chess.PIECE_SYMBOLS[piece.type].upper()}"
                else:
                    self.board_arr[idx // 8, idx % 8] = f"B{chess.PIECE_SYMBOLS[piece.type].upper()}"
        self.board_arr = np.flip(self.board_arr, axis=0)

    def get_piece_name_from_board_dim(self, row: int, column: int) -> str:
        return self.board_arr[7-row][column]

    def square_has_piece(self, row: int, column: int):
        return self.board_arr[row][column] != " "

    def apply_action(self, action: Action):
        # board_piece = piece for piece in self.white_pieces if piece.type == action.piece.type
        board_piece = self.white_pieces[action.piece.type-1] if action.piece.color else self.black_pieces[action.piece.type-1]
        assert board_piece.type == action.piece.type

        # remove piece from current square
        board_piece.bb &= ~get_bb_from_square_int(action.origin_square)

        # move piece to new square
        board_piece.bb |= get_bb_from_square_int(action.destination_square)

        match action.type:
            case ActionType.ATTACK:
               self.apply_attack_action(action)

        # if action is EN_PASSANT, remove opponent pawn
            case ActionType.EN_PASSANT:
                self.apply_enpassant_action(action)

        # if action is CASTLING, move rook
            case ActionType.CASTLING:
                self.apply_castling_action(action)

        # if action is PROMOTION, add promote_to piece to destination square
            case ActionType.PROMOTION:
                self.apply_promotion_action(board_piece, action)

        # update helper bitboards and chararray
        self._set_helper_bitboards()
        self._set_board_chararray()


    def apply_attack_action(self, action):
        opponent_pieces = self.black_pieces if action.piece.color else self.white_pieces
        for attacked_piece in opponent_pieces:
            if attacked_piece.bb & get_bb_from_square_int(action.destination_square) != 0:
                attacked_piece.bb &= ~get_bb_from_square_int(action.destination_square)
                break

    def apply_enpassant_action(self, action):
        # find square of attacked piece
        if action.piece.color == chess.WHITE:
            opponent_pawns = self.BP
            attacked_pawn_sq_bb = move_down(get_bb_from_square_int(action.destination_square))
        else:
            opponent_pawns = self.WP
            attacked_pawn_sq_bb = move_up(get_bb_from_square_int(action.destination_square))
        # remove attacked pawn
        opponent_pawns.bb &= ~attacked_pawn_sq_bb


    def apply_castling_action(self, action):
        if action.is_long_castles:
            rook_destination_bb = get_bb_from_square_int(chess.D1) if action.piece.color else get_bb_from_square_int(chess.D8)
            rook_origin_square = get_bb_from_square_int(chess.A1) if action.piece.color else get_bb_from_square_int(chess.A8)
        else:
            rook_destination_bb = get_bb_from_square_int(chess.F1) if action.piece.color else get_bb_from_square_int(chess.F8)
            rook_origin_square = get_bb_from_square_int(chess.H1) if action.piece.color else get_bb_from_square_int(chess.H8)
        rook_to_move = self.WR if action.piece.color else self.BR
        assert rook_destination_bb & self.all_occupied == 0, f"Rook is trying to move to a square occupied by another piece. Origin: {get_square_name_from_bb(rook_origin_square)} Dest: {get_square_name_from_bb(rook_destination_bb)}"
        assert rook_to_move.bb & rook_origin_square != 0, f"Rook is not in the expected origin square. Origin:{get_square_name_from_bb(rook_origin_square)} BB: {print_bitboard(rook_to_move.bb)}"
        rook_to_move.bb &= ~rook_origin_square
        rook_to_move.bb |= rook_destination_bb


    def apply_promotion_action(self, board_piece, action):
        if action.promotion_to is None:
            raise Exception("Attribute 'promotion_to' of action of type PROMOTION should have a value.")
        match action.promotion_to:
            case chess.QUEEN:
                promote_to_piece = self.WQ if action.piece.color else self. BQ

            case chess.KNIGHT:
                promote_to_piece = self.WN if action.piece.color else self. BN

            case chess.BISHOP:
                promote_to_piece = self.WB if action.piece.color else self. BB

            case chess.ROOK:
                promote_to_piece = self.WR if action.piece.color else self. BR

        # check if action is an attack, i.e. there is an opponent piece in destination square
        destination_bb = get_bb_from_square_int(action.destination_square)
        opponent_occupied = self.black_occupied if action.piece.color else self.white_occupied
        if opponent_occupied & destination_bb != 0:
            self.apply_attack_action(action)

        promote_to_piece.bb |= destination_bb
        # remove pawn from destination, as it was added by caller of this function
        board_piece.bb &= ~destination_bb


    def validate_action(self, piece: Piece, action: Action):
        # check piece to move is in expected location
        if piece.bb & get_bb_from_square_int(action.origin_square) == 0:
            raise Exception(f"{chess.COLOR_NAMES[piece.color]} {piece.type} is not in origin square specified in {action}.")

        # if action type is MOVE, check destination square is not occupied
        if action.type == ActionType.MOVE and self.all_occupied & get_bb_from_square_int(action.destination_square) != 0:
            raise Exception(f"Destination square of {action} is already occupied.")

        # if action type is ATTACK, check destination square is occupied by opponent
        opponent_pieces = self.black_occupied if action.piece.color == chess.WHITE else self.white_occupied
        if action.type == ActionType.ATTACK and opponent_pieces & get_bb_from_square_int(action.destination_square) == 0:
            raise Exception(f"Destination square of attack {action} is not occupied by an opponent piece.")


class InvalidFenException(Exception):
    pass
