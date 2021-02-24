from spoopify.song import Song

class Album:
    def __init__(self, name, *songs, published=False):
        self.name = name
        self.songs = list(songs)
        self.published = published

    def add_song(self, song_n: Song):
        if song_n.single:
            return f"Cannot add {song_n.name}. It's a single"
        if self.published:
            return f"Cannot add songs. Album is published."
        if song_n in self.songs:
            return f"Song is already in the album."
        # filtered_songs = [s for s in self.songs if s == song_n.get_info()]
        # if filtered_songs:
        #     return f"Song is already in the album."
        self.songs.append(song_n)
        return f"Song {song_n.name} has been added to the album {self.name}."

    def remove_song(self, song_name):
        if self.published:
            return f"Cannot remove songs. Album is published."
        filtered_song = [s for s in self.songs if s.name == song_name]
        if filtered_song:
            f_song = filtered_song[0]
            if f_song in self.songs:
                self.songs.remove(f_song)
                return f"Removed song {song_name} from album {self.name}."
        return f"Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        result = f"Album {self.name}\n"
        for s in self.songs:
            result += f"== {s.get_info()}\n"
        return result
