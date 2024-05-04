from collections import deque
from chess.state import State
from chess.state import Fen
import sys

# def search(s0: State, depth_cutoff: int):
#     queue: deque[State] = deque()
#     queue.append(s0)
#     result = {i: 0 for i in range(depth_cutoff + 1)}
#     node_count_per_level = {i: 0 for i in range(depth_cutoff + 1)}

#     depth = 0
#     parent = None

#     while queue and depth <= depth_cutoff:
#         s = queue.popleft()

#         if parent != s.parent:
#             depth += 1
#             if depth > depth_cutoff:
#                 break
#             parent = s.parent

#         result[depth] += len(s.possible_actions)
#         node_count_per_level[depth] += 1

#         # only expand tree if depth < depth_cutoff
#         if depth < depth_cutoff:
#             for action in s.possible_actions:
#                 new_state = s.apply_action(action)
#                 s.children.append(new_state)
#                 queue.append(new_state)

#     return result


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
        # if str(action) == "h2h3":
        #     pass
        
        leaf_nodes = 0
        state.apply_action(action)
        parent = state.parent

        leaf_nodes = perft(depth-1, state)
        total_leaf_nodes += leaf_nodes

        print(f"{action} {leaf_nodes}")

        state = parent

    print(f"\n{total_leaf_nodes}")

# if __name__ == "__main__":
#     depth = int(sys.argv[1])
#     fen = sys.argv[2]
#     moves = sys.argv[3].split() if len(sys.argv) > 3 else []

#     state = State(fen)

#     perfTest(depth, state)

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