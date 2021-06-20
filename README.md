# chessEnginePython

For future self:
L << 1 moves the bitboard 0001 to 0010. Since the least significant square is A1, this would be equivalent to moving from A1 to B1 (Meaning one square right)

Game
[x] White/Black piece separation
State class

- 3-fold repition (FEN list of previous positions count unique - remember same castling rights check)
- 50-move rule (Move counter since captures or pawn push)
- stalemate
- Dead positions
  -- No pushes or progrss possible
  -- King vs king and bishop, etc.

All possible moves for each piece in each location
Convert bitboard to FEN
Convert FEN to bitboards
FEN to pretty board

Agent
