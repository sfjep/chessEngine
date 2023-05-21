from state import State

def start_game():
    s = State().get_initial_state()

    while not s.is_checkmate():
        s.get_possible_actions()
        a = s.choose_action()
        s = s.apply_action(a)
