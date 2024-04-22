import spotipy

from pydantic import BaseModel
from pydantic.dataclasses import dataclass


class SpotifyPlaylist(BaseModel):
    name: str


@dataclass
class SpotifyAPI:
    client_id: str
    client_secret: str

    _spotify_client: spotipy.Spotify

    def __init__(self):
        creds = spotipy.SpotifyClientCredentials(client_id=self.client_id, client_secret=self.client_secret)
        self._spotify_client = spotipy.Spotify(client_credentials_manager=creds)
