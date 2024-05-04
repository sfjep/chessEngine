# chessEnginePython

For future self:

- L << 1 moves the bitboard 0001 to 0010. Since the least significant square is A1, this would be equivalent to moving from A1 to B1 (Meaning one square right)

# Clone stockfix repo and build

`make -j profile-build ARCH=x86-64-sse41-popcnt`

# After build you can run stockfish locally

`./stockfish`

# Now you can test possible moves as positions:

```
position fen rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1
go perft 3
```

!! Beware that newer Stockfish models are containing a print in the network.cpp that will mess up your interaction with perftree. Make sure to remove the info prints.

# To compare again own moves gen, use perftree:

# Install cargo

`curl https://sh.rustup.rs -sSf | sh`

# Install perftree

`cargo install perftree-cli`

# Now you can test your the local moves generation by:

```
./src/perft.sh 3 "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
a2a3 380
b2b3 420
c2c3 420
d2d3 539
e2e3 599
f2f3 380
g2g3 420
h2h3 380
a2a4 420
b2b4 421
c2c4 441
d2d4 560
e2e4 600
f2f4 401
g2g4 421
h2h4 420
b1c3 440
g1h3 400
b1a3 400
g1f3 440

8902
```

# To compare against stockfish you can execute

```
~/code/chessEngine$ perftree ./src/perft.sh
> diff
a2a3  1  1
a2a4  1  1
b1a3  1  1
b1c3  1  1
b2b3  1  1
b2b4  1  1
c2c3  1  1
c2c4  1  1
d2d3  1  1
d2d4  1  1
e2e3  1  1
e2e4  1  1
f2f3  1  1
f2f4  1  1
g1f3  1  1
g1h3  1  1
g2g3  1  1
g2g4  1  1
h2h3  1  1
h2h4  1  1

total  20  20
```
