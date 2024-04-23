from mutagen.mp4 import MP4


def main():
    mut = MP4('./test_files/Carmín.m4a')
    print(mut['©alb'])

    # mut['Title']
    # print(mut.info.__dict__)


# print(mut.keys())
# print(mut.items())
# print(mut.get('©nam'))
# for i in mut.values():
#     print(i)
#     print('****************************')


if __name__ == '__main__':
    main()
