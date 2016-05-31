from media import Artist, Album, Music

joao = Artist("Joao das Coves")
first_album = Album("Meu primeiro cover", 2007)

joao.release_album(first_album)


musicas = [Music("Primeira Faixa"),
            Music("Segunda Faixa"),
            Music("Terceira Faixa"),
            Music("Quarta Faixa") ]


second_musics = [Music("Ninja"), Music("Cabra louca")]

for m in musicas:
    first_album.add_music(m)


second_album = Album("Meu primeiro Autoral", 2009, musics = second_musics)

joao.release_album(second_album)

print(second_musics[0].title, second_musics[0].album.title)
#print(second_album.musics[0].title)#, second_album.musics[0].album)
exit()
print("Uma musica")
print(musicas[0])
print("Uma lista de musicas")
print(musicas)
print("-------------")
print(first_album)
print("-------------")
print(joao)
