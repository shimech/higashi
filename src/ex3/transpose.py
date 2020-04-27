def transpose(M):
    M_transpose = [[value] for value in M[0]]

    if len(M) == 1:
        return M_transpose

    for row in M[1:]:
        for i, value in enumerate(row):
            M_transpose[i].append(value)

    return M_transpose
