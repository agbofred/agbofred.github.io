class songs:
    def __init__(self, title, artist, duration_sec, genre):
        self.title = title
        self.artist = artist
        self.duration_sec = duration_sec
        self.genre = genre
    
playlist = []
playlist.append(songs("title 1", "Artist1", 128, "clasic"))
playlist.append(songs("title 2", "Artist2", 250, "Afrobit"))
playlist.append(songs("title 3", "Artist3", 150, "None"))
playlist.append(songs("title 4", "Artist4", 100, "None"))


def printlist(plist):
    total = 0
    for i in plist:
        total+= i.duration_sec
    print(f"Total music in sectond {total/60}")

printlist(playlist)


