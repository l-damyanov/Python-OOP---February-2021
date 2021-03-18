class vowels:
    def __init__(self, text):
        self.text = [text[i] for i in range(len(text)) if text[i].lower() in ['a', 'e', 'i', 'o', 'y', 'u']]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.text):
            raise StopIteration
        letter = self.text[self.index]
        self.index += 1
        return letter
