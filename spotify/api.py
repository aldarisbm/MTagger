from dataclasses import dataclass
from typing import List

import spotipy


@dataclass(kw_only=True)
class SpotifyTrack:
    artists: List[str]
    album: str
    comment: str


class SpotifyPlaylist:
    name: str
    tracks: List[SpotifyTrack]


class Spotify:
    client_id: str
    client_secret: str

    _spotify_client: spotipy.Spotify

    def __init__(self, client_id: str = None, client_secret: str = None):
        if not client_id and not client_secret:
            from config import settings
            self.client_id = settings.spotipy_client_id
            self.client_secret = settings.spotipy_client_secret
        else:
            self.client_id = client_id
            self.client_secret = client_secret

        creds = spotipy.SpotifyClientCredentials(client_id=self.client_id, client_secret=self.client_secret)
        self._spotify_client = spotipy.Spotify(client_credentials_manager=creds)

    def get_playlist(self, name: str) -> SpotifyPlaylist:
        playlist = self._spotify_client.playlist(playlist_id=name)

        spotify_playlist = SpotifyPlaylist()
        spotify_playlist.name = playlist["name"]

        tracks = playlist['tracks']['items']
        for track in tracks[:1]:
            print(track)
