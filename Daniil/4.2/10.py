def secret_replace(data: str, **kwargs):
    for char in data:
        if char in kwargs:
            data = data.replace(char, kwargs[char][0], 1)
            kwargs[char] = (*kwargs[char][1:], kwargs[char][0])
    return data
