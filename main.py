from config import settings
from spotify.api import Spotify
from youtube.api import Youtube


def main():
    # playlist = sys.argv[1]
    client = Spotify()
    playlist_id = "74H5Eh6UiM63N7wgfFV6qh"

    playlist = client.get_playlist(playlist_id)
    first_track = playlist.tracks[0]

    yt_client = Youtube(api_key=settings.yt_api_key)
    yt_client.search(f"{first_track.name} {first_track.album} {first_track.artists}")

    # mut = mutagen.File('./test_files/Carmín.m4a', easy=True)
    # print(mut.get('title'))


if __name__ == '__main__':
    main()
