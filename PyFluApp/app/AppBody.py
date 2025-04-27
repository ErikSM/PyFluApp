from tkinter import Frame, OptionMenu, Listbox, Entry, Text, StringVar, Scrollbar, E, W, N, S, END, ANCHOR

from app.executions import configuring_buts
from data.all_errors import log_error
from data.content_configs import colr, letter, width, height
from data.content_summary import python_books
from data.content_welcome import attention_string
from structure.Book import Book


class AppBody:

    def __init__(self, main_window):

        self.__book = None
        self.__opt_str = StringVar()
        self.__opt_list = python_books.keys()
        self.__opt_menu_books: OptionMenu
        self.__list_summary: Listbox
        self.__buts_actions = None
        self.__path_str = StringVar()
        self.__entry_path: Entry
        self.__text_screen: Text


        body = Frame(main_window, bg=colr['purple'], width=100, height=100, bd=3)

        self.__left = self._create_left(body)
        self.__left.grid(row=0, column=0)

        self.__center = self._create_center(body)
        self.__center.grid(row=0, column=1)

        self.__right = self._create_right(body)
        self.__right.grid(row=0, column=2)

        body.pack()


    def _create_left(self, body):
        left = Frame(body, bg=colr['purple'], width=30)

        self.__opt_str.set(value ='Selecione o Livro')

        self.__opt_menu_books= OptionMenu(left,
                                          self.__opt_str, *self.__opt_list,
                                          command=lambda selected=self.__opt_str: self.click_opt_book(selected))

        self.__opt_menu_books.config(font=letter['opt'], bg =colr['white grey'],
                                     width=width['opt'], bd=3, anchor='center', state='normal')
        self.__opt_menu_books.grid(row=2, column=1)

        self.__list_summary = Listbox(left, font=letter['list'],
                                      bg=colr['grey'], fg=colr['white'], bd=15,
                                      width=width['lis'], height=height['lis'])

        scr_list_x = Scrollbar(left, orient='horizontal', command=self.__list_summary.xview)
        scr_list_x.grid(row=4, column=1, columnspan=5, sticky=W + E)
        scr_list_y = Scrollbar(left, orient='vertical', command=self.__list_summary.yview)
        scr_list_y.grid(row=3, rowspan=4, column=0, sticky=N + S)

        self.__list_summary.config(yscrollcommand=scr_list_y.set, xscrollcommand=scr_list_x.set)
        self.__list_summary.grid(row=3, column=1, columnspan=4)

        return left

    def _create_center(self, body):
        center = Frame(body, bg=colr['purple'], width=30)

        self.__buts_actions = configuring_buts(center, 'action', self.click_but_play)

        for i in self.__buts_actions[0]:
            i.pack()
        self.__buts_actions[1].pack()

        return center

    def _create_right(self, body):
        right = Frame(body, bg=colr['purple'], width=30)

        self.__entry_path = Entry(right, textvariable=self.__path_str, state='disabled', bd=5,
                                  font=letter['search'], bg=colr['white'], fg=colr['purple'], width=width['ent'])
        self.__entry_path.grid(row=2, column=3, columnspan=4)


        self.__text_screen = Text(right, font=letter['screen'],
                                  bg=colr['grey'], fg=colr['white'], bd=10,
                                  height=height['tex'], width=width['tex'])

        scr_text_x = Scrollbar(right, orient='horizontal', command=self.__text_screen.xview)
        scr_text_x.grid(row=4, column=3, sticky=W + E)
        scr_text_y = Scrollbar(right, orient='vertical', command=self.__text_screen.yview)
        scr_text_y.grid(row=3, rowspan=4, column=4, sticky=N + S)

        self.__text_screen.config(yscrollcommand=scr_text_y.set, xscrollcommand=scr_text_x.set)
        self.__text_screen.grid(row=3, column=3)

        self.__text_screen.insert(1.0, attention_string)

        return right

    def click_opt_book(self, selected):
        self.__list_summary.delete(0, END)

        self.__book = Book(selected)
        self.__list_summary.insert(END, *self.__book.summary())

    def click_but_play(self):
        self.__text_screen.delete(1.0, END)

        selected = self.__list_summary.get(ANCHOR)
        try:
            file_content = self.__book[selected]
        except TypeError as te:
            file_content = log_error('AppMain _click_but_play', te, 'book not found')

        self.__text_screen.insert(END, file_content)

    def default(self):
        self.__text_screen.delete(0.0, END)
        self.__list_summary.delete(0, END)
        self.__entry_path.delete(0, END)

        self.__opt_str.set(value ='Selecione o Livro')
        self.__text_screen.insert(1.0, attention_string)

    def update_size(self, new_w: dict, new_h: dict, new_l: dict):
        self.__list_summary.config(width=new_w['lis'], height=new_h['lis'], font=new_l['list'])
        self.__text_screen.config(width=new_w['tex'], height=new_h['tex'], font=new_l['screen'])

    def update_font(self, new_letters: dict):
        self.__list_summary.config(font=new_letters['list'])
        self.__text_screen.config(font=new_letters['screen'])

