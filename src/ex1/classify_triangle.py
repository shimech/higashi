def classify_triangle(a, b, c):
    lens = sorted([a, b, c])

    if lens[0] + lens[1] <= lens[2]:
        return 0

    if lens[0] ** 2 + lens[1] ** 2 > lens[2] ** 2:
        return 1
    elif lens[0] ** 2 + lens[1] ** 2 == lens[2] ** 2:
        return 2
    else:
        return 3
