def words2vec(words, frequent_words):
    counter = dict([[fw, 0] for fw in frequent_words])
    for word in words:
        if counter.get(word) is not None:
            counter[word] += 1
    return [counter[fw] for fw in frequent_words]
