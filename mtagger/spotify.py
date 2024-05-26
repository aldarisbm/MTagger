from dataclasses import dataclass, field
from typing import List

import spotipy


@dataclass
class SpotifyTrack:
    artists: List[str] = field(init=True)
    album: str = field(init=True)
    name: str = field(init=True)


@dataclass
class SpotifyPlaylist:
    name: str = field(init=True)
    tracks: List[SpotifyTrack] = field(init=False)

    def __post_init__(self):
        self.tracks = []


@dataclass(kw_only=True)
class Spotify:
    client_id: str = field(init=True)
    client_secret: str = field(init=True)

    __spotify_client: spotipy.Spotify = field(init=False)

    def __post_init__(self):
        creds = spotipy.SpotifyClientCredentials(client_id=self.client_id, client_secret=self.client_secret)
        self.__spotify_client = spotipy.Spotify(client_credentials_manager=creds)

    def _get_all_tracks(self, playlist_id: str) -> []:
        all_tracks = []

        offset = 0
        limit = 100
        while True:
            items = self.__spotify_client.playlist_items(playlist_id=playlist_id, limit=limit, offset=offset)['items']
            if len(items) == 0:
                break
            offset += limit
            all_tracks.extend(items)

        return all_tracks

    def get_playlist(self, playlist_id: str) -> SpotifyPlaylist:
        playlist = self.__spotify_client.playlist(playlist_id=playlist_id)
        playlist_tracks = self._get_all_tracks(playlist_id=playlist_id)

        playlist_name = playlist.get('name')
        spotify_playlist = SpotifyPlaylist(name=playlist_name)

        for track in playlist_tracks:
            t = track.get('track')
            artists = t.get('artists')
            spotify_playlist.tracks.append(
                SpotifyTrack(
                    name=t.get('name'),
                    album=t.get('album').get('name'),
                    artists=[artist.get('name') for artist in artists],
                )
            )

        return spotify_playlist
