from spoopify.song import Song
from spoopify.album import Album

class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name):
        filtered_albums = [a for a in self.albums if a.name == album_name]
        if filtered_albums:
            f_album = filtered_albums[0]
            if f_album.published:
                return f"Album has been published. It cannot be removed."
            else:
                self.albums.remove(f_album)
                return f"Album {album_name} has been removed."
        return f"Album {album_name} is not found."

    def details(self):
        res = f"Band {self.name}\n"
        for a in self.albums:
            res += f"Album {a.name}\n"
            for s in a.songs:
                res += f"{s.get_info()}\n"
        return res
