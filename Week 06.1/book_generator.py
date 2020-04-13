from random import randrange, choices, choice
from zipfile import ZipFile

lowercase_letters = 'a b c d e f g h i j\
 k l m n o p q r s t u v w x y z'.split()

uppercase_letters = 'A B C D E F G H I J\
K L M N O P Q R S T U V W X Y Z'.split()

punctuation = '?\n\n !\n\n .'.split(' ')

lowercase_letters.append(', ')


def generate_words():
    is_first_word = True
    while True:
        word = choices(lowercase_letters, k=randrange(2, 9))
        if is_first_word:
            word.insert(0, choice(uppercase_letters))
        word = ''.join(word).strip() + ' '
        is_first_word = yield word


def generate_filenames():
    i = 0
    while True:
        i += 1
        yield f"{i:06}" + ".txt"


def generate_chapters(length):
    while True:
        word = generate_words()

        chapter = ''

        words = 0
        while words <= length:
            for i in range(randrange(15, 25)):
                chapter += next(word)
                words += 1
            chapter = chapter.rstrip()
            punct = choices(punctuation, [1, 1, 10], k=1)[0]
            chapter += punct
            if words <= length:
                if punct == '.':
                    chapter += ' '
                chapter += word.send(True)
                words += 1

        yield chapter


def generate_files(chapter_length_range):
    chapter = generate_chapters(chapter_length_range)
    filename = generate_filenames()
    chapter_number = 0

    while True:
        file = 'book/' + next(filename)
        for i in range(5):
            chapter_number += 1
            if i == 0:
                with open(file, 'w') as f:
                    f.write(f'# chapter {chapter_number}\n')
                    f.write(next(chapter))
            else:
                with open(file, 'a') as f:
                    f.write(f'\n\n# chapter {chapter_number}\n')
                    f.write(next(chapter))
        print(f'{file} is being written...')
        yield file


def main(chapters_count):
    file = generate_files(69)

    with ZipFile('book.zip', 'w') as z:
        for i in range(chapters_count):
            z.write(next(file))


if __name__ == '__main__':
    main(500000)
