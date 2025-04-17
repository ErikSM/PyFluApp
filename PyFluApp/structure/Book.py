from data.content_summary import python_books, open_file


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

    def __getitem__(self, selected: str):
        parentheses = selected.find(')')

        file_name = selected[:parentheses]

        file_name = file_name.replace(' ', '')
        file_name = file_name.replace('.', '')

        try:
            return self.__contents[file_name]
        except KeyError:
            return (f'    [ Chapter not found ]\n\n\n'
                        f'Acesse:\n'
                        f'          https://pythonfluente.com/')


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
            except FileNotFoundError:
                text = (f'    [ file not found ]\n\n\n'
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

        for i in self.__titles.items():
            number = i[0]
            name = i[1]

            try:
                int(number)
            except ValueError:
                paragraph = ' ' * 2
            else:
                paragraph = ''
            finally:
                between = ') '

            string = f'{paragraph}{number}{between}{name}'

            yield string
