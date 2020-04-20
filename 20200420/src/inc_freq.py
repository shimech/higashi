def inc_freq(s, d):
    for c in s:
        if d.get(c) is not None:
            d[c] += 1
