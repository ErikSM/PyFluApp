from tkinter import *

from app.config import font, colr, width, height
from data.summary import python_books
from structure.Book import Book


class AppMain:

    def __init__(self):

        self.__window = Tk()

        self.__pybook_selected = None

        self.__head = Frame(self.__window, bg=colr['purple'], width=100, height=100)
        self.__container_u = Frame(self.__head, bg=colr['purple'])

        self.__body = Frame(self.__window, bg=colr['purple'], width=100, height=100)

        self.__container_l = Frame(self.__body, bg=colr['purple'], width=30)
        self.__opt_menu_str = StringVar()
        self.__opt_menu_tuple = python_books.keys()
        self.__opt_menu = OptionMenu(self.__container_l, self.__opt_menu_str, *self.__opt_menu_tuple,
                                     command=lambda opt_str=self.__opt_menu_str: self._active_opt_menu(opt_str))
        self.__listbox = Listbox(self.__container_l)

        self.__container_c = Frame(self.__body, bg=colr['purple'], width=30)
        self.__buts = self._set_buts(self.__container_c)

        self.__container_r = Frame(self.__body, bg=colr['purple'], width=30)
        self.__entry_text_str = StringVar()
        self.__entry_local = Entry(self.__container_r)
        self.__text = Text(self.__container_r)

        self.__foot = Frame(self.__window, bg=colr['purple'], width=100, height=100)
        self.__container_d = Frame(self.__foot, bg=colr['purple'])
        self.__note = Text(self.__container_d)

        self._enable_config()

    def _enable_config(self):
        self._config_container_l()
        self._config_container_c()
        self._config_container_r()
        self._config_container_d()

    def _config_container_u(self):
        pass

    def _config_container_l(self):
        self.__opt_menu.config(bg=colr['white grey'], width=width['opt'], bd=3, anchor='center', state=NORMAL)
        self.__opt_menu.grid(row=0, column=1)

        self.__listbox.config(font=font['list'], bg=colr['grey'], fg=colr['white'], bd=15)
        self.__listbox.config(width=width['lis'], height=height['lis'])
        self.__listbox.grid(row=1, column=1)

        scr_list_x = Scrollbar(self.__container_l, orient=HORIZONTAL, command=self.__listbox.xview)
        scr_list_x.grid(row=2, column=1, sticky=W + E)
        self.__listbox.config(xscrollcommand=scr_list_x.set)

        scr_list_y = Scrollbar(self.__container_l, orient=VERTICAL, command=self.__listbox.yview)
        scr_list_y.grid(row=1, column=0, sticky=N + S)
        self.__listbox.config(yscrollcommand=scr_list_y.set)

        self.__container_l.grid(row=0, column=0)

    def _active_opt_menu(self, selected):
        self.__listbox.delete(0, END)

        self.__pybook_selected = Book(selected)

        self.__listbox.insert(END, *self.__pybook_selected.summary())

    def _config_container_c(self):
        for i in self.__buts:
            i.pack()

        self.__container_c.grid(row=0, column=1)

    def _set_buts(self, container):
        buts = list()

        how_many = 11
        cont = 1
        while cont <= how_many:
            buts.append(Button(container, width=5, height=-5, bd=3, state=DISABLED,
                               bg=colr['grey'], fg=colr['purple']))
            cont += 1

        buts[0].config(bg=colr['purple'], bd=0)
        buts[2].config(text='play =>', command=self._click_but_play, state=NORMAL)

        return buts

    def _click_but_play(self):
        self.__text.delete(1.0, END)

        selected = self.__listbox.get(ANCHOR)

        parentheses = selected.find(')')
        file_name = selected[:parentheses]
        file_name = file_name.replace(' ', '')
        file_name = file_name.replace('.', '')

        file = self.__pybook_selected[file_name]

        self.__text.insert(END, file)

    def _config_container_r(self):
        self.__entry_local.config(font=font['search'], textvariable=self.__entry_text_str)
        self.__entry_local.config(width=width['ent'], bd=3, bg=colr['white'], fg=colr['purple'], state=DISABLED)
        self.__entry_local.grid(row=0, column=2)

        self.__text = Text(self.__container_r, font=font['Principal'],
                           bg=colr['grey'], fg=colr['white'], bd=3, height=height['tex'], width=width['tex'])
        self.__text.grid(row=1, column=2)

        scr_text_x = Scrollbar(self.__container_r, orient=HORIZONTAL, command=self.__text.xview)
        scr_text_x.grid(row=2, column=2, sticky=W + E)
        self.__text.config(xscrollcommand=scr_text_x.set)

        scr_text_y = Scrollbar(self.__container_r, orient=VERTICAL, command=self.__text.yview)
        scr_text_y.grid(row=1, column=3, sticky=N + S)
        self.__text.config(yscrollcommand=scr_text_y.set)

        self.__container_r.grid(row=0, column=2)

    def _config_container_d(self):
        self.__note.config(font=font['Principal'],
                           selectforeground='black', selectbackground='white', insertbackground='white',
                           bg=colr['purple'], fg=colr['white'], bd=2, height=height['not'], width=width['not'])
        self.__note.grid(row=0, column=1)

        scr_note_x = Scrollbar(self.__container_d, orient=HORIZONTAL, command=self.__note.xview)
        scr_note_x.grid(row=1, column=1, sticky=W + E)
        self.__note.config(xscrollcommand=scr_note_x.set)

        scr_note_y = Scrollbar(self.__container_d, orient=VERTICAL, command=self.__note.yview)
        scr_note_y.grid(row=0, column=0, sticky=N + S)
        self.__note.config(yscrollcommand=scr_note_y.set)

        self.__container_d.grid(row=1, column=1)

    def _config_window(self):
        self.__window.config(bg=colr['purple'])
        self.__window.resizable(True, True)
        self.__window.geometry('+100+10')
        self.__window.title('Fluent Python App Study')

    def start_app(self):
        self.__head.pack()
        self.__body.pack()
        self.__foot.pack()

        self._config_window()
        self.__window.mainloop()
