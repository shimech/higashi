def inc_digits(s, n):
    return "".join(map(lambda x: str((int(x) + n) % 10), list(s)))
