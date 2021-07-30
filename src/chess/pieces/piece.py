from abc import ABC, abstractmethod

class Piece(ABC):
    
    def __init__(self, bb, color, piece_type):
        self.bb = bb
        self.color = color
        self.piece_type = piece_type
    
    @abstractmethod
    def generate_move_lookup(self):
        pass
    