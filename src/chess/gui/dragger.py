import pygame as p
import chess

class Dragger:

    """ Dragger is a class that handles the dragging of pieces.
    The first event: Click the piece
    The second event: Drag the piece
    The third event: Drop the piece
    """
    def __init__(self):
        self.x_coor = 0
        self.y_coor = 0
        self.piece = None  # this attribute will store the image of the piece being dragged

    def update_position(self, position, piece=None):  # we add an optional parameter for the piece
        self.x_coor, self.y_coor = position
        if piece is not None:  # if a piece is provided, store it
            self.piece = piece

    def get_piece(self):  # method to get the current piece
        return self.piece

    def clear(self):  # method to clear the current piece
        self.piece = None
