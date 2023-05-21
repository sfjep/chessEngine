import chess

class FenUtils:
    def __init__(self, fen: str):
        self.fen = fen
        self.fen_fields = self.fen.split()

    def get_board(self, Board):
        return Board(self.fen_fields[0])

    def get_player(self):
        return self.fen_fields[1] == "w"

    def get_can_castle_kingside(self):
        return ("k" in self.fen_fields[2], "K" in self.fen_fields[2])

    def get_can_castle_queenside(self):
        return ("q" in self.fen_fields[2], "Q" in self.fen_fields[2])

    def get_en_passant_capture_square(self):
        if self.fen_fields[3] != "-":
            return (chess.BB_SQUARES[chess.SQUARE_NAMES.index(self.fen_fields[3])])
        else:
            return chess.BB_EMPTY

    def get_halfmove_count(self):
        return int(self.fen_fields[4])

    def get_move_count(self):
        return int(self.fen_fields[5])