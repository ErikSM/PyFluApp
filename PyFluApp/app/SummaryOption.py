from tkinter import StringVar, OptionMenu
from app.Summary import Summary
from structure.Book import Book
from data.all_errors import log_error
from data.content_summary import python_books


class SummaryOption:

    def __init__(self, frame, summary: Summary):
        self.__book: Book
        self.__listbox_summary = summary

        self.__selected = StringVar(value='Selecione o Livro')
        self.__options = python_books.keys()

        self.__summary_menu = OptionMenu(frame, self.__selected, *self.__options,
                                         command=lambda str_var=self.__selected: self._click_menu(str_var))

    def __str__(self):
        return self.__selected.get()

    def __getitem__(self, item):
        try:
            return self.__book[item]
        except AttributeError as ae:
            return log_error('SummaryOption __getitem__', ae, 'book not found')

    def _click_menu(self, str_var):
        self.__book = Book(str_var)
        self.__listbox_summary.update_content(*self.__book.summary())

    def grid_config(self, **kwargs):
        self.__summary_menu.grid(**kwargs)

    def config_widget(self, **kwargs):
        self.__summary_menu.config(**kwargs)

    def default(self):
        self.__selected.set(value='Selecione o Livro')

