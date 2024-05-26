# MTagger

**MTagger** is a library designed to load MP3 files downloaded from YouTube and retrieve and update their metadata,
including title, artist, album, and genre. This ensures your music files have complete metadata, making them compatible
with applications like Serato.

### **THIS LIBRARY IS OFFERED AS-IS, NO GUARANTEES**

## Features

- **Load MP3 Files or Folders**: Load individual MP3 files or entire folders of MP3s downloaded from YouTube.
- **Retrieve Metadata**: Use the LLM, YouTube API, and Google Search to find and retrieve metadata for the MP3 files.
    - Title
    - Artist
    - Album
    - Genre
- **Update Metadata**: Automatically update the MP3 files with the retrieved metadata for compatibility with
  applications like Serato.

## Installation

TODO

## Usage

### Load and Update a Single MP3 File

```python
from mtagger import MetadataExtractor

# Initialize the metadata extractor
extractor = MetadataExtractor(
    yt_api_key='YOUR_YOUTUBE_API_KEY',
    spotify_client_id='YOUR_SPOTIFY_CLIENT_ID',
    spotify_client_secret='YOUR_SPOTIFY_CLIENT_SECRET'
)

# Load an MP3 file
mp3_file = 'path/to/your/downloaded/mp3file.mp3'

# Retrieve and update metadata
metadata = extractor.get_metadata(mp3_file)
extractor.update_metadata(mp3_file, metadata)

# Print the updated metadata
print("Title:", metadata.title)
print("Artist:", metadata.artist)
print("Album:", metadata.album)
print("Genre:", metadata.genre)
```

### Load and Update All MP3 Files in a Folder

```python
from mtagger import MetadataExtractor

# Initialize the metadata extractor
extractor = MetadataExtractor(
    yt_api_key='YOUR_YOUTUBE_API_KEY',
    spotify_client_id='YOUR_SPOTIFY_CLIENT_ID',
    spotify_client_secret='YOUR_SPOTIFY_CLIENT_SECRET'
)

# Load a folder containing MP3 files
folder_path = 'path/to/your/downloaded/mp3files/'

# Some extra metadata for LLM to infer metadata
extra_metadata = 'possible genres: bachata, salsa, zouk'

# Retrieve and update metadata for all files in the folder
extractor.update_metadata_for_folder(folder_path=folder_path, extra_metadata=extra_metadata)
```

## Configuration

Provide your YouTube API key to use the YouTube API features when initializing the `MetadataExtractor` class.

## API Reference

### `MetadataExtractor`

#### `__init__(self, api_key: str)`

- Initializes the metadata extractor with the necessary API key for YouTube.

#### `get_metadata(self, mp3_file: str) -> dict`

- Retrieves metadata for the given MP3 file.
- **Parameters**:
    - `mp3_file`: The path to the MP3 file.
- **Returns**: A SeratoMetadata object containing the metadata (`title`, `artist`, `album`, `genre`).

#### `update_metadata(self, mp3_file: str, metadata: dict)`

- Updates the given MP3 file with the provided metadata.
- **Parameters**:
    - `mp3_file`: The path to the MP3 file.
    - `SeratoMetadata`: An object containing the metadata (`title`, `artist`, `album`, `genre`).

#### `update_metadata_for_folder(self, folder_path: str)`

- Retrieves and updates metadata for all MP3 files in the specified folder.
- **Parameters**:
    - `folder_path`: The path to the folder containing MP3 files.
    - `extra_metadata`: Extra metadata that you think might help the LLM infer metadata

## License

This project is licensed under the MIT License.