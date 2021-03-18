class custom_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.num = self.start

    def __iter__(self):
        return self

    def __next__(self):
        if self.num > self.end:
            raise StopIteration
        value = self.num
        self.num += 1
        return value
