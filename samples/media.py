

class Artist:
    def __init__(self, name, albuns = []):
        self.name = name
        self.albuns = albuns

        for album in self.albuns:
            album.artist = self

    def release_album(self, album):
        self.albuns.append(album)
        album.artist = self

    def __str__(self):
        representation = "{}\nAlbuns:\n".format(self.name)
        for album in self.albuns:
            representation += "{}\n".format(album)
        return representation

    def __repr__(self):
        return self.name

class Album:
    def __init__(self, title, year, artist = None, musics = []):
        self.title = title
        self.year = year
        self.musics = musics
        self.artist = artist

        for music in self.musics:
            music.album = self

    def add_music(self, music):
        self.musics.append(music)
        music.album = self

    def insert_music(self, index, music):
        self.musics.insert(index, music)
        music.album = self

    def __str__(self):
        representation = "{} ({})\nFaixas:\n".format(self.title, self.year)
        n = 1
        for music in self.musics:
            representation += "{}. {}\n".format(n, music.title)
            n += 1
        return representation

    def __repr__(self):
        return "{} ({})".format(self.title, self.year)

class Music:
    def __init__(self, title, duration = 0, album = None):
        self.title = title
        self.duration = duration
        self.album = album

    def __str__(self):
        return "{} ({}) — {}".format(self.title, self.album.title, self.album.artist.name)

    def __repr__(self):
        return "{}".format(self.title)


if __name__ == '__main__':
    joao = Artist("Joao das Coves")
    novo_album = Album("Meus covers", 2016)
    joao.release_album(novo_album)
