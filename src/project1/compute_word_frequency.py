def compute_word_frequency(dw):
    import itertools
    from collections import Counter
    important_word_list = list(itertools.chain.from_iterable(dw.values()))
    return dict(Counter(important_word_list))
