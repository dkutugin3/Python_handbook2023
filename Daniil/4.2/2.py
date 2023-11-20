def make_matrix(size, value: int = 0):
    if type(size) is tuple:
        return [[value for i in range(size[0])] for j in range(size[1])]
    return [[value for i in range(size)] for j in range(size)]
