from janome.tokenizer import Tokenizer


T = Tokenizer()


def str2words(doc):
    def is_important_word(part_of_speech):
        important_word_list = ["形容詞,自立", "動詞,自立", "名詞"]
        for important_word in important_word_list:
            if important_word in part_of_speech:
                return True
        return False

    return [token.base_form for token in T.tokenize(doc) if is_important_word(token.part_of_speech)]
