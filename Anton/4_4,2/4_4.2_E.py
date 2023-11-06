def to_string(*data, sep=' ', end='\n') -> str:
    return sep.join(map(str, data)) + end
