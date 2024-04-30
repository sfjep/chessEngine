from collections import deque
from chess.state import State


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
