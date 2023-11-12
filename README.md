# chessEnginePython

For future self:
- L << 1 moves the bitboard 0001 to 0010. Since the least significant square is A1, this would be equivalent to moving from A1 to B1 (Meaning one square right)

Game setup missing:
- Castling through check
- Checkmate
- Limit scope when in check 
- 3-fold repition (FEN list of previous positions count unique - remember same castling rights check)
- 50-move rule (Move counter since captures or pawn push)
- Stalemate
- Draw on dead positions
  -- No pushes or progrss possible
  -- King vs king and bishop, etc.
