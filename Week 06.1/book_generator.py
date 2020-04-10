from random import randrange, sample
from zipfile import ZipFile

word_characters = 'a*b*c*d*e*f*g*h*i*j*k*\
l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*\
-* - *, *! *. *? *\n'.split('*')


def generate_words():
    while True:
        word = sample(word_characters, randrange(3, 7))
        yield ''.join(word) + ' '


def generate_filenames():
    i = 0
    while True:
        i += 1
        yield f"{i:03}" + ".txt"


def generate_chapters(length):
    word = generate_words()

    while True:
        chapter = ''

        for i in range(length):
            chapter += next(word)

        yield chapter


def write_chapters(chapter_length_range):
    chapter = generate_chapters(chapter_length_range)
    filename = generate_filenames()
    chapter_number = 0

    while True:
        for i in range(5):
            with open(next(filename), 'w') as f:
                chapter_number += 1
                f.write(f'# chapter {chapter_number}\n')
                f.write(next(chapter))
                yield


def main(chapters_count):
    write = write_chapters(69)

    with ZipFile('book.zip', 'w') as z:
        for i in range(chapters_count):
            next(write)


if __name__ == '__main__':
    main(3)
