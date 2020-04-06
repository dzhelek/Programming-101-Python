class Song:
    def __init__(self, title, artist, album, length):
        self.title = title
        self.artist = artist
        self.album = album
        self.length = length


    def __str__(self):
        return f"{self.artist} - {self.title} from {self.album} - {self.length}"


    def __eq__(self, other):
        return self.title = other.title


    def __hash__(self):
        return self.title


    def length(self, seconds=False, minutes=False, hours=False):
        return self.length

