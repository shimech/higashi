class drop_first:
    def __init__(self, iterable):
        self.iter = iter(iterable)
        next(self.iter)

    def __iter__(self):
        return self.iter
