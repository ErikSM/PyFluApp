from data.all_errors import log_error
from data.content_summary import python_books, open_file


def prepare_file_name(selected: str):
    file_name = selected[:selected.find(')')]

    file_name = file_name.replace(' ', '')
    file_name = file_name.replace('.', '')

    return file_name


class Book:

    def __init__(self, book: python_books):
        self.__name = book
        self.__chapters = python_books[self.__name]

        self.__titles = {i[0]: i[1] for i in self._generating_titles()}
        self.__contents = self._dict_contents()


    def __getitem__(self, selected: str):
        file_name = prepare_file_name(selected)
        try:
            return self.__contents[file_name]
        except KeyError as ke:
            return log_error('book __getitem__', ke, 'chapter not found')


    def _generating_titles(self):
        try:
            for i in self.__chapters:
                for j in self.__chapters[i]:
                    yield j
        except TypeError:
            pass

    def _dict_contents(self):
        titles = dict()

        for i in self.__titles:
            key = str(i).replace('.', '')
            try:
                text = open_file(key)
            except FileNotFoundError as ffe:
                text = log_error('Book _dict_contents', ffe, 'file not found')

            titles[key] = text

        return titles

    def summary(self):
        for i in self.__titles.items():
            try:
                int(i[0])
            except ValueError:
                space = ' ' * 2
            else:
                space = ''

            yield f'{space} {i[0]}) {i[1]}'
