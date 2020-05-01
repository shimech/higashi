def text_file_len(filename, code):
    with open(filename, mode="r", encoding=code) as f:
        text = f.read()
    return len(text)
