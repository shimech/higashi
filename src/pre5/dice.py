def dice(i):
    import random
    random.seed(i)
    return tuple([random.randint(1, 6) for _ in range(2)])
