import logging
from dataclasses import dataclass, field
from typing import Dict

import mutagen

from config import logger


@dataclass
class SeratoMetadata:
    filename: str = field(init=True)
    title: str = field(init=True)
    album: str = field(init=True)
    artist: str = field(init=True)
    genre: str = field(init=True)


@dataclass
class Metadata:
    filename: str
    logger: logging.Logger = field(init=False)

    def set_metadata(self, metadata: SeratoMetadata) -> Dict:
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
