from tkinter import Frame, OptionMenu, Listbox, Entry, Text, StringVar, Scrollbar, E, W, N, S, END, ANCHOR, Toplevel, \
    Button

from structure.buttons import configuring_buts
from data.all_errors import log_error
from data.content_configs import colr, letter, width, height
from data.content_summary import python_books
from data.content_welcome import attention_string
from structure.Book import Book


class AppBody:

    def __init__(self, main_window):
        self.__body = self._body_frame(main_window)
        self.__left = self._create_left()
        self.__center = self._create_center()
        self.__right = self._create_right()


    def _body_frame(self, main_window):
        self.__body = Frame(main_window, bg=colr['purple'], width=100, height=100, bd=3)

        self.__body.pack()

        return self.__body

    def _create_left(self):
        self.__opt_str = StringVar(value ='Selecione o Livro')
        self.__opt_list = python_books.keys()
        self.__opt_menu_books: OptionMenu
        self.__list_summary: Listbox


        left = Frame(self.__body, bg=colr['purple'], width=30)


        self.__opt_menu_books= OptionMenu(left,
                                          self.__opt_str, *self.__opt_list,
                                          command=lambda selected=self.__opt_str: self._click_opt_book(selected))

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

        left.grid(row=0, column=0)

        return left

    def _create_center(self):
        self.__buts_actions = None

        center = Frame(self.__body, bg=colr['purple'], width=30)

        self.__buts_actions = configuring_buts(center, 'action', self._click_but_play)

        for i in self.__buts_actions[0]:
            i.pack()
        self.__buts_actions[1].pack()

        center.grid(row=0, column=1)

        return center

    def _create_right(self):
        self.__path_str = StringVar(value='..//')
        self.__entry_path: Entry
        self.__text_screen: Text
        self.__but_notebook: Button

        right = Frame(self.__body, bg=colr['purple'], width=30)

        self.__entry_path = Entry(right, textvariable=self.__path_str, font=letter['search'],
                                  disabledbackground=colr['grey'], disabledforeground=colr['purple'],
                                  width=width['ent'], bd=5, state='disabled')
        self.__entry_path.grid(row=2, column=2)

        self.__but_notebook = Button(right, text=' < Expandir >', command=self.screen_top_level)
        self.__but_notebook.grid(row=2, column=4, columnspan=5)

        #  grid base [ column=2 ~ columnspan=4 ]
        self.__text_screen = Text(right, font=letter['screen'], insertunfocussed='hollow',
                                  bg=colr['grey'], fg=colr['yellow'], selectbackground=colr['yellow'] ,
                                  height=height['tex'], width=width['tex'], bd=10)

        scr_text_x = Scrollbar(right, orient='horizontal', command=self.__text_screen.xview)
        scr_text_x.grid(row=4, column=2, columnspan=3, sticky=W + E)
        scr_text_y = Scrollbar(right, orient='vertical', command=self.__text_screen.yview)
        scr_text_y.grid(row=3, rowspan=4, column=5, sticky=N + S)

        self.__text_screen.config(yscrollcommand=scr_text_y.set, xscrollcommand=scr_text_x.set)
        self.__text_screen.grid(row=3, column=2, columnspan=3)  # grid base

        self.__text_screen.insert(1.0, attention_string)

        right.grid(row=0, column=2)

        return right

    def _click_opt_book(self, selected):
        self.__book = Book(selected)

        self.__list_summary.delete(0, END)
        self.__list_summary.insert(END, *self.__book.summary())

    def _click_but_play(self):
        self.__text_screen.delete(1.0, END)

        selected = self.__list_summary.get(ANCHOR)
        try:
            file_content = self.__book[selected]
        except TypeError as type_error:
            file_content = log_error('AppMain _click_but_play', type_error, 'book not found')

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

    def update_color(self, theme: list):
        self.__body.config(bg=theme[0])

        self.__left.config(bg=theme[0])
        self.__center.config(bg=theme[0])
        self.__right.config(bg=theme[0])

        self.__list_summary.config(bg=theme[2], fg=theme[1])
        self.__entry_path.config(disabledbackground=theme[2], disabledforeground=theme[0])
        self.__text_screen.config(bg=theme[2], fg=theme[4], selectbackground=theme[4])

    def del_text(self, where='screen'):
        if where == 'screen':
            self.__text_screen.delete(1.0, END)
        elif where == 'list':
            self.__list_summary.delete(0, END)

    def insert_text(self, *args, where='screen'):
        if where == 'screen':
            self.__text_screen.insert(END, *args)
        elif where == 'list':
            self.__list_summary.insert(END, *args)

    def screen_top_level(self):
        tl = Toplevel()
        tl.geometry('+300+47')

        temporary_screen = Text(tl, width=130, height=40, bd=20)
        temporary_screen.insert(1.0, self.__text_screen.get(1.0, END))
        temporary_screen.pack(fill='both')

        tl.mainloop()
