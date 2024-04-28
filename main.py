from spotify.api import Spotify


def main():
    # playlist = sys.argv[1]
    client = Spotify()
    playlist_id = "63YBONu8oFaV0IzdJz3Xzn"

    client.get_playlist(playlist_id)

    # print(playlist)
    # mut = mutagen.File('./test_files/Carmín.m4a', easy=True)
    # print(mut.get('title'))


if __name__ == '__main__':
    main()
