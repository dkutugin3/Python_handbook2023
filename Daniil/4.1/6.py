old_msg = set()


def modern_print(s: str):
    if s not in old_msg:
        print(s)
        old_msg.add(s)
