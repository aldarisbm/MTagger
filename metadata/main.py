from dataclasses import dataclass

import mutagen

from config import logger


@dataclass
class SeratoMetadata:
    title: str
    album: str
    artist: str
    genre: str


@dataclass
class Metadata:
    filename: str

    def set_metadata(self, metadata: SeratoMetadata):
        try:
            f = mutagen.File(self.filename)
        except mutagen.MutagenError:
            logger.info(f'loading file {self.filename}')
            raise

        try:
            f.setdefault('title', metadata.title)
            f.setdefault('album', metadata.album)
            f.setdefault('artist', metadata.artist)
            f.setdefault('genre', metadata.genre)
        except Exception as e:
            logger.info(f'setting tags for {self.filename}: {e}')
            raise

        return f.tags()
