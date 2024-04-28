from spotify.api import Spotify


def main():
    # playlist = sys.argv[1]
    client = Spotify()
    playlist_id = "74H5Eh6UiM63N7wgfFV6qh"

    playlist = client.get_playlist(playlist_id)

    for track in playlist.tracks:
        print(track)
    print(len(playlist.tracks))
    # mut = mutagen.File('./test_files/Carmín.m4a', easy=True)
    # print(mut.get('title'))


if __name__ == '__main__':
    main()
