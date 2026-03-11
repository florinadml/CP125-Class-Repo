def manage_playlist(current_playlist, add_songs, import_playlist, banned_songs):
    for song in add_songs :
        current_playlist.add(song)

    current_playlist.update(import_playlist)
    current_playlist.difference_update(banned_songs)

    while len(current_playlist) > 6 : 
        current_playlist.pop()

    return len(current_playlist)




