def replace_kutoten(filename, code):
    with open(filename, mode="r", encoding=code) as f:
        text = f.read()

    text_replaced = "".join(map(select_char, list(text)))

    paths = filename.split("/")
    paths[-1] = "new-{}".format(paths[-1])
    new_filename = "/".join(paths)
    with open(new_filename, mode="w", encoding=code) as f:
        f.write(text_replaced)


def select_char(char):
    if char == "、":
        return "，"
    elif char == "。":
        return "．"
    else:
        return char
