from dataclasses import dataclass, field

import pyyoutube
from pyyoutube import Api

from config import settings


@dataclass
class Youtube:
    api_key: str = field(init=True)
    __youtube_client: pyyoutube.Api = field(init=True)

    def __post_init__(self):
        self.api_key = self.api_key or settings.yt_api_key
        self.__youtube_client = Api(api_key=self.api_key)

    def search(self, query: str):
        ts = self.__youtube_client.search(q=query, limit=10, return_json=True)
        for item in ts['items']:
            print(item)
