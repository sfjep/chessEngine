from collections import deque
from chess.state import State


def search(s0: State, depth_cutoff: int):
    queue: deque[State] = deque()
    queue.append(s0)
    result = {i: 0 for i in range(depth_cutoff)}
    
    depth = 0
    while queue and depth < depth_cutoff:
        s = queue.popleft()
        for action in s.get_possible_actions():
            new_state = s.apply_action(action)
            s.children.append(new_state)
            queue.append(new_state)
            result[depth] += len(s.possible_actions)
        depth += 1

    return result
