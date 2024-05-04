from collections import deque
from chess.state import State
from chess.state import Fen
import sys

def perft(depth: int, state: State):
    if depth == 1:
        return len(state.get_legal_moves())
    elif depth > 1:
        count = 0

        moves = state.get_legal_moves()
        for action in moves:
            state.apply_action(action)
            parent = state.parent
            count += perft(depth - 1, state)
            state = parent

        return count

    else:
        return 1

def perfTest(depth: int, state: State):
    total_leaf_nodes = 0

    moves = state.get_legal_moves()
    for action in moves:
        leaf_nodes = 0
        state.apply_action(action)
        parent = state.parent

        leaf_nodes = perft(depth-1, state)
        total_leaf_nodes += leaf_nodes

        print(f"{action} {leaf_nodes}")
        state = parent

    print(f"\n{total_leaf_nodes}", end="")

if __name__ == "__main__":
    depth = int(sys.argv[1])
    fen = sys.argv[2]

    state = State(fen)
    perfTest(depth, state)

# state = State()

# perfTest(3, state)

# file1 = open('/Users/victorianunezr/repos/chessEngine/src/output.txt', 'r')
# Lines = file1.readlines()

# count = 0
# # Strips the newline character
# for line in Lines[0:len(Lines)-1]:
#     count += 1
#     print(line.strip())

# print(Lines[len(Lines)-1], end="")