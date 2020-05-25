def extract_frequent_words(word_frequency, coverage):
    n_freq = 0
    answer = []
    for word, freq in sorted(word_frequency.items(), key=lambda x: -x[1]):
        if 1.0 * n_freq / sum(word_frequency.values()) < coverage:
            n_freq += freq
            answer.append(word)
        else:
            break
    return answer
