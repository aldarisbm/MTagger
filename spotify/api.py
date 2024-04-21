from pydantic import BaseModel
from pydantic.dataclasses import dataclass


class SpotifyPlaylist(BaseModel):
    name: str


@dataclass
class SpotifyAPI:
    access_token: str
    client_id: str
    client_secret: str
