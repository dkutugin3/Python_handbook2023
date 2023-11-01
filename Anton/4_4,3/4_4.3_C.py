def make_equation(*koeffs) -> str:
    if len(koeffs) < 2:
        return str(koeffs[-1])
    return f'({(make_equation(*koeffs[:-1:]))}) * x + {koeffs[-1]}'
