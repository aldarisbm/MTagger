from dataclasses import dataclass, field

from mtagger.llm import MetadataProducerLlm
from mtagger.metadata import SeratoMetadata
from mtagger.spotify import Spotify
from mtagger.youtube import Youtube


@dataclass
class MetadataExtractor:
    youtube_api_key: str = field(init=True)
    spotify_client_id: str = field(init=True)
    spotify_client_secret: str = field(init=True)

    model_path: str = field(init=False, default=None)
    __llm: MetadataProducerLlm = field(init=False)
    __spotify_client: Spotify = field(init=False)
    __youtube_client: Youtube = field(init=False)

    def __post_init__(self):
        self.__spotify_client = Spotify(
            client_id=self.spotify_client_id,
            client_secret=self.spotify_client_secret
        )
        self.__youtube_client = Youtube(
            api_key=self.youtube_api_key
        )
        self.__llm = MetadataProducerLlm(model_path=self.model_path)

    def get_metadata(self, filename: str) -> SeratoMetadata:
        pass

    def update_metadata(self, metadata: SeratoMetadata):
        pass
