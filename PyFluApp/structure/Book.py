from data.summary import python_books


class Book:

    def __init__(self, book: str):
        self.__name = book

        self.__chapters = python_books[self.__name]

    def __str__(self):
        return f'Book({self.__name})'

    def __len__(self):
        return len(self.__chapters)

    def __getitem__(self, item):
        return self.__chapters[item]

    def all_chapters(self):
        all_chapters = [i for i in self.__chapters]
        return all_chapters

    def summary(self):
        summary = list()

        for i in self.__chapters:
            for j in self.__chapters[i]:

                number = j[0]
                name = j[1]
                between = ') '
                paragraph = ''

                if type(j[0]) is not int:
                    paragraph = ' ' * 2

                string = f'{paragraph}{number}{between}{name}'
                summary.append(string)

        return summary
