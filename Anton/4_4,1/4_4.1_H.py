def is_palindrome(obj) -> bool:
    if type(obj) is int:
        obj = str(obj)
    obj = tuple(obj)
    if obj[:(len(obj) + 1) // 2:] == obj[-1:len(obj) // 2 - 1:-1]:
        return True
    return False
