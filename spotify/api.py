from dataclasses import dataclass
from typing import List

import spotipy

from config import settings


@dataclass(kw_only=True)
class SpotifyTrack:
    artists: List[str]
    album: str
    name: str


class SpotifyPlaylist:
    name: str
    tracks: List[SpotifyTrack] = []


@dataclass
class Spotify:
    client_id: str
    client_secret: str

    _spotify_client: spotipy.Spotify

    def __post_init__(self):
        if self.client_secret is None and self.client_id is None:
            self.client_id = settings.spotipy_client_id
            self.client_secret = settings.spotipy_client_secret
        creds = spotipy.SpotifyClientCredentials(client_id=self.client_id, client_secret=self.client_secret)
        self._spotify_client = spotipy.Spotify(client_credentials_manager=creds)

    def _get_all_tracks(self, playlist_id: str) -> []:
        all_tracks = []

        offset = 0
        limit = 100
        while True:
            items = self._spotify_client.playlist_items(playlist_id=playlist_id, limit=limit, offset=offset)['items']
            if len(items) == 0:
                break
            offset += limit
            all_tracks.extend(items)

        return all_tracks

    def get_playlist(self, playlist_id: str) -> SpotifyPlaylist:
        playlist = self._spotify_client.playlist(playlist_id=playlist_id)
        playlist_tracks = self._get_all_tracks(playlist_id=playlist_id)

        spotify_playlist = SpotifyPlaylist()
        spotify_playlist.name = playlist["name"]

        for track in playlist_tracks:
            artists = track['track']['artists']
            spotify_playlist.tracks.append(
                SpotifyTrack(
                    name=track['track']['name'],
                    album=track['track']['album']['name'] if track['track']['album'] else None,
                    artists=[artist['name'] for artist in artists],
                )
            )

        return spotify_playlist
