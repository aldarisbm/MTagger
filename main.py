from mtagger.spotify.api import Spotify
from mtagger.youtube.api import Youtube


def main():
    client = Spotify()
    playlist_id = "74H5Eh6UiM63N7wgfFV6qh"

    playlist = client.get_playlist(playlist_id)
    first_track = playlist.tracks[0]

    yt_client = Youtube()
    yt_client.search(f"{first_track.name} {first_track.album} {first_track.artists}")
    # for root, dirs, files in os.walk(f"{os.getcwd()}/test_files"):
    #     for file in files[:1]:
    #         file_name = f'{root}/{file}'
    #         print(file_name)
    #         mut = mutagen.File(file_name, easy=True)
    #         mut.delete()
    #         print(mut.setdefault('title', 'the title'))
    #         print(mut.setdefault('album', 'the album'))
    #         print(mut.setdefault('artist', 'the artist'))
    #         mut.tags['album'] = 'test'
    #         print("tags", mut.tags)
    #         print(mut.get('title'))
    #         print(mut.get('artist'))
    #         print(mut.get('album'))
    #         mut.save()


if __name__ == '__main__':
    main()
