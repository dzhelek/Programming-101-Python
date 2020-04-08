from zipfile import ZipFile

from help_library import get_character


def get_chapter(filename):
    with ZipFile(filename, 'r') as z:
        for file in z.namelist():
            with z.open(file, 'r') as f:
                print()
                for line in f.readlines():
                    line = line.decode('utf-8')
                    if line.startswith('#'):
                        print(line, end='')
                        yield
                    else:
                        print(line, end='')


def main():
    chapters = get_chapter('Book.zip')
    for chapter in chapters:

        pressed = None
        while True:
            if pressed == ' ':
                break
            if pressed is not None:
                print(str(pressed), end='\r')
            pressed = str(get_character())[2]


if __name__ == '__main__':
    main()
