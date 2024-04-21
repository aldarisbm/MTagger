import spotipy

from config import settings


def main():
    creds = spotipy.SpotifyClientCredentials(
        client_id=settings.spotipy_client_id,
        client_secret=settings.spotipy_client_secret
    )
    spotify = spotipy.Spotify(client_credentials_manager=creds)
    playlist_id = '74H5Eh6UiM63N7wgfFV6qh'
    playlist = spotify.playlist(playlist_id=playlist_id)
    tracks = playlist['tracks']['items']
    for track in tracks[:1]:
        print(track)


if __name__ == '__main__':
    main()
