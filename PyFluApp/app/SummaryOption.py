from tkinter import StringVar, OptionMenu

from data.content_configs import letter, colr, width
from data.content_summary import python_books


#  //////////////   em desenvolvimento  /////////////////////////


class SummaryOption:

    def __init__(self, left):
        self.__opt_str = StringVar(value='Selecione o Livro')
        self.__opt_list = python_books.keys()


        self.__opt_menu_books = OptionMenu(left, self.__opt_str, *self.__opt_list,
                                           command=lambda selected=self.__opt_str: self._click_opt_book(selected))

        self.__opt_menu_books.config(font=letter['opt'], bg=colr['white grey'],
                                     width=width['opt'], bd=3, anchor='center', state='normal')
        self.__opt_menu_books.grid(row=2, column=1)

