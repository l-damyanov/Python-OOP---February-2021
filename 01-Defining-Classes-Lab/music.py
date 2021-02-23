class Music:
    def __init__(self, title, artis, lyrics):
        self.title = title
        self.artist = artis
        self.lyrics = lyrics
    def print_info(self):
        return f'This is "{self.title}" from "{self.artist}"'

    def play(self):
        return self.lyrics
