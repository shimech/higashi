def split_iterable(xs, y):
    answer, part = [], []
    for element in xs:
        if element == y:
            answer.append(part)
            part = []
        else:
            part.append(element)
    answer.append(part)
    return answer
