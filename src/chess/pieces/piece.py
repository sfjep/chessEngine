from abc import ABC, abstractmethod

class Piece(ABC):
    
    def __init__(self, bb, color):
        self.bb = bb
        self.color = color
    
    @abstractmethod
    def generate_move_lookup(self):
        pass
    