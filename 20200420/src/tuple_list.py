def tuple_list(lp, x):
    return [x for x in list(map(lambda value: value[1] if value[0] == x else None, lp)) if x is not None]
