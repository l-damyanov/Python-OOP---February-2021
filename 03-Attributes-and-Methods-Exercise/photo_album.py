import math

class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(math.floor(photos_count * 0.25))

    def add_photo(self, label):
        for page_i in range(self.pages):
            if len(self.photos[page_i]) == 4:
                continue
            else:
                self.photos[page_i].append(label)
                return f"{label} photo added successfully on page {page_i + 1} slot {len(self.photos[page_i])}"
        return "No more free spots"

    def display(self):
        result = ""
        for page in self.photos:
            result += f"-----------\n"
            if len(page) > 0:
                result += f"{' '.join('[]' for el in page)}\n"
            else:
                result += "\n"
        result += f"-----------\n"
        return result
