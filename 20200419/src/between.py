def between(ln, x, y):
    x_index, y_index = ln.index(x), ln.index(y)
    start = min(x_index, y_index)
    end = max(x_index, y_index) + 1
    return ln[start:end]
