def mycsvread(csvfile, code):
    with open(csvfile, mode="r", encoding=code) as f:
        outlist = [l.replace("\n", "").split(",") for l in f.readlines()]
    return outlist
