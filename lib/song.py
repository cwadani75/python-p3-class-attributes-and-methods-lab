class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Track total songs
        Song.count += 1

        # Track unique genres
        if genre not in Song.genres:
            Song.genres.append(genre)

        # Track unique artists
        if artist not in Song.artists:
            Song.artists.append(artist)

        # Track count per genre
        if genre in Song.genre_count:
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1

        # Track count per artist
        if artist in Song.artist_count:
            Song.artist_count[artist] += 1
        else:
            Song.artist_count[artist] = 1
