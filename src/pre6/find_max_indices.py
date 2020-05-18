def find_max_indices(M):
    max_value_list = [max(row) for row in M]
    max_value = max(max_value_list)
    index = max_value_list.index(max_value)
    column = M[index].index(max_value)
    return (index, (column, max_value))
