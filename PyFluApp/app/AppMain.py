from tkinter import *

from app.config import letter, colr, width, height
from app.executions import processing_but_other, configuring_buts
from data.content_summary import python_books
from structure.Book import Book


class AppMain:


    def __init__(self):
        self.__window = Tk()

        self.__book = None
        self.__img_banner = PhotoImage(file=r'assets\banner.PNG')

        self.__head = Frame(self.__window, bg=colr['purple'], width=100, height=100, bd=3)

        self.__container_u = Frame(self.__head, bg=colr['purple'])
        self.__label_img_banner = Label(self.__container_u)

        self.__body = Frame(self.__window, bg=colr['purple'], width=100, height=100, bd=3)

        self.__container_l = Frame(self.__body, bg=colr['purple'], width=30)
        self.__str_opt_book = StringVar(value='Click to Select Python Book')
        self.__tuple_opt_books = python_books.keys()
        self.__opt_menu_books = OptionMenu(self.__container_l, self.__str_opt_book, *self.__tuple_opt_books,
                                           command=lambda opt_str=self.__str_opt_book: self._active_opt_menu(opt_str))
        self.__list_summary = Listbox(self.__container_l)

        self.__container_c = Frame(self.__body, bg=colr['purple'], width=30)
        self.__buts_actions = self._set_buts(self.__container_c, 'action')

        self.__container_r = Frame(self.__body, bg=colr['purple'], width=30)
        self.__entry_text_str = StringVar()
        self.__entry_local = Entry(self.__container_r)
        self.__text_screen = Text(self.__container_r)

        self.__foot = Frame(self.__window, bg=colr['purple'], width=100, height=100, bd=3)

        self.__container_d = Frame(self.__foot, bg=colr['purple'])
        self.__buts_others = self._set_buts(self.__container_d, 'others')
        self.__text_note = Text(self.__container_d)

        self._enable_config()


    def _set_buts(self, container, type_buts):
        command = None

        if type_buts == 'action':
            command = self._click_but_play
        elif type_buts == 'others':
            command = self._click_any_but_others

        buts, buts_container = configuring_buts(container, type_buts, command)

        return buts, buts_container


    def _config_container_u(self):
        self.__label_img_banner.configure(image=self.__img_banner)
        self.__label_img_banner.pack(side=LEFT)

        self.__container_u.pack()

    def _config_container_l(self):
        self.__opt_menu_books.config(bg=colr['white grey'], width=width['opt'], bd=3, anchor='center', state=NORMAL)
        self.__opt_menu_books.grid(row=2, column=1)

        self.__list_summary.config(font=letter['list'], bg=colr['grey'], fg=colr['white'], bd=15)
        self.__list_summary.config(width=width['lis'], height=height['lis'])
        self.__list_summary.grid(row=3, column=1, columnspan=4)

        scr_list_x = Scrollbar(self.__container_l, orient=HORIZONTAL, command=self.__list_summary.xview)
        scr_list_x.grid(row=4, column=1, columnspan=5, sticky=W + E)
        self.__list_summary.config(xscrollcommand=scr_list_x.set)

        scr_list_y = Scrollbar(self.__container_l, orient=VERTICAL, command=self.__list_summary.yview)
        scr_list_y.grid(row=3, rowspan=4, column=0, sticky=N + S)
        self.__list_summary.config(yscrollcommand=scr_list_y.set)

        self.__container_l.grid(row=0, column=0)

    def _active_opt_menu(self, selected):
        self.__list_summary.delete(0, END)
        self.__book = Book(selected)

        self.__list_summary.insert(END, *self.__book.summary())

    def _config_container_c(self):
        for i in self.__buts_actions[0]:
            i.pack()
        self.__buts_actions[1].pack()

        self.__container_c.grid(row=0, column=1)

    def _click_but_play(self):
        self.__text_screen.delete(1.0, END)

        selected = self.__list_summary.get(ANCHOR)

        try:
            file_content = self.__book[selected]
        except TypeError:
            file_content = (f'    [ book not found ]\n\n\n'
                        f'Acesse:\n'
                        f'          https://pythonfluente.com/')

        self.__text_screen.insert(END, file_content)

    def _config_container_r(self):
        self.__entry_local.config(font=letter['search'], textvariable=self.__entry_text_str)
        self.__entry_local.config(width=width['ent'], bd=5, bg=colr['white'], fg=colr['purple'], state=DISABLED)
        self.__entry_local.grid(row=2, column=3, columnspan=4)

        self.__text_screen = Text(self.__container_r, font=letter['principal'],
                                  bg=colr['grey'], fg=colr['white'], bd=3, height=height['tex'], width=width['tex'])
        self.__text_screen.grid(row=3, column=3)

        scr_text_x = Scrollbar(self.__container_r, orient=HORIZONTAL, command=self.__text_screen.xview)
        scr_text_x.grid(row=4, column=3, sticky=W + E)
        self.__text_screen.config(xscrollcommand=scr_text_x.set)

        scr_text_y = Scrollbar(self.__container_r, orient=VERTICAL, command=self.__text_screen.yview)
        scr_text_y.grid(row=3, rowspan=4, column=4, sticky=N + S)
        self.__text_screen.config(yscrollcommand=scr_text_y.set)

        self.__container_r.grid(row=0, column=2)

    def _config_container_d(self):
        for i in self.__buts_others[0]:
            i.pack()
        self.__buts_others[1].grid(row=2, rowspan=3, column=1)

        self.__text_note.config(font=letter['principal'],
                                selectforeground='black', selectbackground='white', insertbackground='white',
                                bg=colr['purple'], fg=colr['white'], bd=10, height=height['not'], width=width['not'])
        self.__text_note.grid(row=3, column=4)

        scr_note_x = Scrollbar(self.__container_d, orient=HORIZONTAL, command=self.__text_note.xview)
        scr_note_x.grid(row=4, column=4, sticky=W + E)
        self.__text_note.config(xscrollcommand=scr_note_x.set)

        scr_note_y = Scrollbar(self.__container_d, orient=VERTICAL, command=self.__text_note.yview)
        scr_note_y.grid(row=3, rowspan=4, column=3, sticky=N + S)
        self.__text_note.config(yscrollcommand=scr_note_y.set)

        self.__container_d.grid(row=1, column=1)

    def _click_any_but_others(self, selected):
        self.__text_note.delete(0.0, END)

        processed = processing_but_other(selected)
        text_str, more_action, action = processed

        self.__text_note.insert(END, text_str)
        if more_action:
            action()

    def _enable_config(self):
        self._config_container_u()
        self._config_container_l()
        self._config_container_c()
        self._config_container_r()
        self._config_container_d()

    def _config_window(self):
        self.__window.config(bg=colr['purple'])
        self.__window.resizable(True, True)
        self.__window.geometry('+1+1')
        self.__window.title('Fluent Python App Study')

    def start_app(self):
        self.__head.pack()
        self.__body.pack()
        self.__foot.pack()

        self._config_window()
        self.__window.mainloop()
