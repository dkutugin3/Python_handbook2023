def modern_print(state: str) -> None:
    global history

    try:
        history
    except NameError:
        history = []

    if state not in history:
        print(state)
        history.append(state)
