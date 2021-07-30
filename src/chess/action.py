from chess.state import State
import chess
from chess.utils import (
    get_individual_ones_in_bb,
    get_square_int_from_bb
)

class Action:

    def __init__(self, piece_type: int, origin_square: int, new_square: int):
        self.piece_type = piece_type
        self.origin_square = origin_square
        self.new_square = new_square

    @staticmethod
    def get_possible_actions(state: State):
        '''
        Generate list of actions possible in state
            Check which color is playing
            Iterate through all pieces of color
            Take index of piece and get moves lookup
            Convert possible moves to list of       
        '''     
        possible_actions = []   
        if state.turn == chess.WHITE:
            possible_actions.append(Action._get_white_possible_actions(state))
        else:
            possible_actions.append(Action._get_black_possible_actions(state))

    @staticmethod
    def _get_white_possible_actions(state: State) -> list:
        possible_actions = []   
        for piece in state.board.white_pieces:

            new_square = piece.get_moves(piece.bb)
            
            if new_square & state.BLACK_OCCUPIED != 0:
                Action(square, new_square, piece.piece_type)
                
                # quit in direction
            else:
                Action(square, new_square, piece.piece_type)


            for piece_bb in get_individual_ones_in_bb(piece.bb):
                possible_moves = piece.MOVES_LOOKUP[get_square_int_from_bb(piece_bb)]
                for possible_move in get_individual_ones_in_bb(possible_moves):
                    possible_move 

    
    @staticmethod
    def _get_black_possible_actions(state: State) -> list:
        pass


                    