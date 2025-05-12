from tkinter import StringVar, OptionMenu, END

from app.Summary import Summary
from data.content_configs import letter, colr, width
from data.content_summary import python_books
from structure.Book import Book

class SummaryOption:

    def __init__(self, frame, list_summary: Summary):
        self.__book = None
        self.__listbox_summary = list_summary

        self.__selected = StringVar(value='Selecione o Livro')
        self.__options = python_books.keys()

        self.__summary_menu = OptionMenu(frame, self.__selected, *self.__options,
                                         command=lambda str_var=self.__selected: self._click_menu(str_var))

    def __str__(self):
        return self.__selected.get()

    def __getitem__(self, item):
        return self.__book[item]

    def _click_menu(self, str_var):
        self.__book = Book(str_var)
        self.__listbox_summary.update_content(*self.__book.summary())

    def grid_config(self, **kwargs):
        self.__summary_menu.grid(**kwargs)

    def config_widget(self, **kwargs):
        self.__summary_menu.config(**kwargs)

    def default(self):
        self.__selected.set(value='Selecione o Livro')

