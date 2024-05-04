from collections import deque
from chess.state import State
from chess.state import Fen



def search(s0: State, depth_cutoff: int):
    queue: deque[State] = deque()
    queue.append(s0)
    result = {i: 0 for i in range(depth_cutoff + 1)}
    node_count_per_level = {i: 0 for i in range(depth_cutoff + 1)}

    depth = 0
    parent = None

    while queue and depth <= depth_cutoff:
        s = queue.popleft()

        if parent != s.parent:
            depth += 1
            if depth > depth_cutoff:
                break
            parent = s.parent

        result[depth] += len(s.possible_actions)
        node_count_per_level[depth] += 1

        # only expand tree if depth < depth_cutoff
        if depth < depth_cutoff:
            for action in s.possible_actions:
                new_state = s.apply_action(action)
                s.children.append(new_state)
                queue.append(new_state)

    return result



def perfTest(depth: int, state: State):
    total_leaf_nodes = 0

    for action in state.possible_actions:
        leaf_nodes = 0
        state.apply_action(action)

        leaf_nodes = perft(depth-1, state)
        total_leaf_nodes += leaf_nodes

        print(f"Move: {action}, Leaf nodes: {leaf_nodes}")

        state = state.undo_action()

    print(f"Test complete. Total number of leaves: {total_leaf_nodes}")


def perft(depth: int, state: State):
    if depth == 1:
        return len(state.possible_actions)
    elif depth > 1:
        count = 0

        for action in state.possible_actions:
            state.apply_action(action)
            parent = state.undo_action()
            count += perft(depth - 1, state)
            state = parent

        return count

    else:
        return 1
