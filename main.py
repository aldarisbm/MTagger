import mutagen


def main():
    mut = mutagen.File('./test_files/Carmín.m4a', easy=True)
    print(mut.get('title'))

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
