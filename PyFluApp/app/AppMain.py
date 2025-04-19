from tkinter import *

from app.config import letter, colr, width, height
from app.executions import processing_but_other, configuring_buts
from data.content_summary import python_books
from structure.Book import Book


class AppMain:

    def __init__(self):

        self.__window = Tk()
        self.__book = None
        self.__img_banner = PhotoImage()
        self.__path_str = StringVar()
        self.__opt_books_str = StringVar()
        self.__obt_books_tuple = python_books.keys()


        head = Frame(self.__window, bg=colr['purple'], width=100, height=100, bd=3)

        self.__head_up = Frame(head)
        self.__label_img_banner = Label(self.__head_up)

        head.pack()

        body = Frame(self.__window, bg=colr['purple'], width=100, height=100, bd=3)

        self._body_left = Frame(body)
        self.__opt_books = OptionMenu(self._body_left, self.__opt_books_str, *self.__obt_books_tuple,
                                      command=lambda opt_str=self.__opt_books_str: self._click_opt_book(opt_str))
        self.__list_summary = Listbox(self._body_left)

        self.__body_center = Frame(body)
        self.__buts_actions = self._set_buts(self.__body_center, 'action')

        self.__body_right = Frame(body)
        self.__entry_path = Entry(self.__body_right)
        self.__text_screen = Text(self.__body_right)

        body.pack()

        foot = Frame(self.__window, bg=colr['purple'], width=100, height=100, bd=3)

        self.__foot_down = Frame(foot)
        self.__buts_others = self._set_buts(self.__foot_down, 'others')
        self.__text_note = Text(self.__foot_down)

        foot.pack()


    def _click_opt_book(self, selected):
        self.__list_summary.delete(0, END)
        self.__book = Book(selected)

        self.__list_summary.insert(END, *self.__book.summary())

    def _set_buts(self, container, type_buts):
        command = None

        if type_buts == 'action':
            command = self._click_but_play
        elif type_buts == 'others':
            command = self._click_any_but_others

        buts, buts_container = configuring_buts(container, type_buts, command)

        return buts, buts_container

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

    def _click_any_but_others(self, selected):
        self.__text_note.delete(0.0, END)

        processed = processing_but_other(selected)
        text_str, more_action, action = processed

        self.__text_note.insert(END, text_str)
        if more_action:
            action()

    def _config_head_up(self):
        self.__img_banner.config(file=r'assets\banner.PNG')
        self.__label_img_banner.configure(image=self.__img_banner)
        self.__label_img_banner.pack(side=LEFT)

        self.__head_up.config(bg=colr['purple'])
        self.__head_up.pack()

    def _config_body_left(self):
        self.__opt_books_str.set(value='Click to Select Python Book')

        self.__opt_books.config(bg=colr['white grey'], width=width['opt'], bd=3, anchor='center', state=NORMAL)
        self.__opt_books.grid(row=2, column=1)

        self.__list_summary.config(font=letter['list'], bg=colr['grey'], fg=colr['white'], bd=15)
        self.__list_summary.config(width=width['lis'], height=height['lis'])
        self.__list_summary.grid(row=3, column=1, columnspan=4)

        scr_list_x = Scrollbar(self._body_left, orient=HORIZONTAL, command=self.__list_summary.xview)
        scr_list_x.grid(row=4, column=1, columnspan=5, sticky=W + E)
        self.__list_summary.config(xscrollcommand=scr_list_x.set)

        scr_list_y = Scrollbar(self._body_left, orient=VERTICAL, command=self.__list_summary.yview)
        scr_list_y.grid(row=3, rowspan=4, column=0, sticky=N + S)
        self.__list_summary.config(yscrollcommand=scr_list_y.set)

        self._body_left.config(bg=colr['purple'], width=30)
        self._body_left.grid(row=0, column=0)

    def _config_body_center(self):
        for i in self.__buts_actions[0]:
            i.pack()
        self.__buts_actions[1].pack()

        self.__body_center.config(bg=colr['purple'], width=30)
        self.__body_center.grid(row=0, column=1)

    def _config_body_right(self):
        self.__entry_path.config(font=letter['search'], textvariable=self.__path_str)
        self.__entry_path.config(width=width['ent'], bd=5, bg=colr['white'], fg=colr['purple'], state=DISABLED)
        self.__entry_path.grid(row=2, column=3, columnspan=4)

        self.__text_screen = Text(self.__body_right, font=letter['principal'],
                                  bg=colr['grey'], fg=colr['white'], bd=3, height=height['tex'], width=width['tex'])
        self.__text_screen.grid(row=3, column=3)

        scr_text_x = Scrollbar(self.__body_right, orient=HORIZONTAL, command=self.__text_screen.xview)
        scr_text_x.grid(row=4, column=3, sticky=W + E)
        self.__text_screen.config(xscrollcommand=scr_text_x.set)

        scr_text_y = Scrollbar(self.__body_right, orient=VERTICAL, command=self.__text_screen.yview)
        scr_text_y.grid(row=3, rowspan=4, column=4, sticky=N + S)
        self.__text_screen.config(yscrollcommand=scr_text_y.set)

        self.__body_right.config(bg=colr['purple'], width=30)
        self.__body_right.grid(row=0, column=2)

    def _config_foot_down(self):
        for i in self.__buts_others[0]:
            i.pack()
        self.__buts_others[1].grid(row=2, rowspan=3, column=1)

        self.__text_note.config(font=letter['principal'],
                                selectforeground='black', selectbackground='white', insertbackground='white',
                                bg=colr['purple'], fg=colr['white'], bd=10, height=height['not'], width=width['not'])
        self.__text_note.grid(row=3, column=4)

        scr_note_x = Scrollbar(self.__foot_down, orient=HORIZONTAL, command=self.__text_note.xview)
        scr_note_x.grid(row=4, column=4, sticky=W + E)
        self.__text_note.config(xscrollcommand=scr_note_x.set)

        scr_note_y = Scrollbar(self.__foot_down, orient=VERTICAL, command=self.__text_note.yview)
        scr_note_y.grid(row=3, rowspan=4, column=3, sticky=N + S)
        self.__text_note.config(yscrollcommand=scr_note_y.set)

        self.__foot_down.config(bg=colr['purple'])
        self.__foot_down.grid(row=1, column=1)

    def _config_window(self):
        self.__window.config(bg=colr['purple'])
        self.__window.resizable(True, True)
        self.__window.geometry('+1+1')
        self.__window.title('Fluent Python App Study')

    def _enable_all_config(self):
        self._config_head_up()
        self._config_body_left()
        self._config_body_center()
        self._config_body_right()
        self._config_foot_down()

        self._config_window()

    def start_app(self):
        self._enable_all_config()
        self.__window.mainloop()
