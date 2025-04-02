from data.summary import python_books, open_file
import io
import os


class Book:

    def __init__(self, book: python_books):
        self.__name = book
        self.__chapters = python_books[self.__name]

        self.__titles = {i[0]: i[1] for i in self._generating_titles()}
        self.__contents = self._dict_contents()

    def __str__(self):
        return f'Book({self.__name})'

    def __len__(self):
        return len(self.__chapters)

    def __getitem__(self, item):
        return self.__contents[item]

    def _generating_titles(self):
        for i in self.__chapters:
            for j in self.__chapters[i]:
                yield j

    def _dict_contents(self):
        titles = dict()

        for i in self.__titles:
            key = str(i).replace('.', '')

            try:
                text = open_file(key)
            except FileNotFoundError:
                text = (f'    [ File not found ]\n\n\n'
                        f'Acesse:\n'
                        f'          https://pythonfluente.com/')

            titles[key] = text

        return titles

    def all_chapters(self):
        return [i for i in self.__chapters.keys()]

    def all_titles(self):
        for i in self.__titles:
            yield i, self.__titles[i]

    def summary(self):
        summary = list()

        for i in self.__titles.items():
            number = i[0]
            name = i[1]

            if len(i[0]) != 1:
                paragraph = ' ' * 2
            else:
                paragraph = ''

            between = ') '

            string = f'{paragraph}{number}{between}{name}'
            summary.append(string)

        return summary


