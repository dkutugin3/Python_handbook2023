def number_length(num: int) -> int:
    num = str(num).lstrip('-')
    return len(num)