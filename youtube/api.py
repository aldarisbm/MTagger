from dataclasses import dataclass

import pyyoutube
from pyyoutube import Api

from config import settings


@dataclass
class Youtube:
    api_key = str
    _youtube_client = pyyoutube.Api

    def __post_init__(self):
        if self.api_key is None:
            self.api_key = settings.yt_api_key
        self._youtube_client = Api(api_key=self.api_key)

    def search(self, query: str):
        ts = self._youtube_client.search(q=query, limit=10, return_json=True)
        # print(ts)
        for item in ts['items']:
            print(item)
        #     snippet = item_dict.get("snippet")
        #     print(snippet)
#
