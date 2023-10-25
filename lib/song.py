class Song:
    
    count = 0
    genres = set()
    artists = set()
    genre_count = dict(Rap=0, Rock=0, Country=0, Pop=0)
    artist_count = {}
    
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)
        
    @classmethod
    def add_song_to_count(cls, increment=1):
        cls.count += increment
        
    @classmethod
    def add_to_genres(cls, genre):
        cls.genres.add(genre)
        
    @classmethod
    def add_to_artists(cls, artist):
        cls.artists.add(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        cls.genre_count[genre] += 1
        
    @classmethod
    def add_to_artist_count(cls, artist):
        if cls.artist_count.get(artist):
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1