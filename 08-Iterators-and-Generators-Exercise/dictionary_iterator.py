class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.index = 0
        self.keys = [key for key in self.dictionary.keys()]

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.dictionary):
            raise StopIteration
        value = self.dictionary[self.keys[self.index]]
        key = self.keys[self.index]
        self.index += 1
        return (key, value)
