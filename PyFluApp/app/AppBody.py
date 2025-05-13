from tkinter import Frame, Text, Scrollbar, E, W, N, S, END, Toplevel, Button
from app.Screen import Screen
from app.ContentPath import ContentPath
from app.Summary import Summary
from app.SummaryOption import SummaryOption
from data.all_errors import log_error
from data.content_configs import colr, letter, width
from data.content_welcome import attention_string
from structure.buttons import configuring_buts


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
        left = Frame(self.__body, bg=colr['purple'], width=30)

        self.__list_summary = Summary(left)
        self.__list_summary.grid_config('summary', row=3, column=1, columnspan=4)
        self.__list_summary.grid_config('scroll_x', row=4, column=1, columnspan=5, sticky=W + E)
        self.__list_summary.grid_config('scroll_y', row=3, rowspan=4, column=0, sticky=N + S)

        self.__opt_menu_books = SummaryOption(left, self.__list_summary)
        self.__opt_menu_books.config_widget(font=letter['opt'], bg=colr['white grey'], bd=3,
                                            width=width['opt'], anchor='center', state='normal')
        self.__opt_menu_books.grid_config(row=2, column=1)

        left.grid(row=0, column=0)

        return left

    def _create_center(self):
        center = Frame(self.__body, bg=colr['purple'], width=30)

        self.__buts_actions = configuring_buts(center, 'action', self._click_but_play)
        for i in self.__buts_actions[0]:
            i.pack()
        self.__buts_actions[1].pack()

        center.grid(row=0, column=1)

        return center

    def _create_right(self):
        right = Frame(self.__body, bg=colr['purple'], width=30)

        self.__entry_path = ContentPath(right)
        self.__entry_path.grid_config(row=2, column=2)

        self.__but_notebook = Button(right, text=' < Expandir >', command=self.screen_top_level)
        self.__but_notebook.grid(row=2, column=4, columnspan=5)

        self.__text_screen = Screen('notes', right)
        self.__text_screen.grid_config('screen', row=3, column=2, columnspan=3)
        self.__text_screen.grid_config('scroll_x', row=4, column=2, columnspan=3, sticky=W + E)
        self.__text_screen.grid_config('scroll_y', row=3, rowspan=4, column=5, sticky=N + S)
        self.__text_screen.write(1.0, attention_string)

        right.grid(row=0, column=2)

        return right

    def _click_but_play(self):
        self.__text_screen.delete_text(1.0, END)

        selected = self.__list_summary.get_selected()
        try:
            file_content = self.__opt_menu_books[selected]
        except TypeError as type_error:
            file_content = log_error('AppMain _click_but_play', type_error, 'book not found')

        self.__text_screen.write(END, file_content)

    def default(self):
        self.__text_screen.delete_text(0.0, END)
        self.__list_summary.delete_option(0, END)
        self.__entry_path.delete_text(0, END)

        self.__opt_menu_books.default()
        self.__text_screen.write(1.0, attention_string)

    def update_size(self, new_w: dict, new_h: dict, new_l: dict):
        self.__list_summary.configure_widget(width=new_w['lis'], height=new_h['lis'], font=new_l['list'])
        self.__text_screen.configure_widget('screen', width=new_w['tex'], height=new_h['tex'], font=new_l['screen'])

    def update_font(self, new_letters: dict):
        self.__list_summary.configure_widget(font=new_letters['list'])
        self.__text_screen.configure_widget(font=new_letters['screen'])

    def update_color(self, theme: list):
        self.__body.config(bg=theme[0])

        self.__left.config(bg=theme[0])
        self.__center.config(bg=theme[0])
        self.__right.config(bg=theme[0])

        self.__list_summary.configure_widget(bg=theme[2], fg=theme[1])

        self.__entry_path.configure_widget(disabledbackground=theme[2], disabledforeground=theme[0])
        self.__text_screen.configure_widget(bg=theme[2], fg=theme[4], selectbackground=theme[4])

    def del_text(self, where='screen'):
        if where == 'screen':
            self.__text_screen.delete_text(1.0, END)
        elif where == 'list':
            self.__list_summary.delete_option(0, END)

    def insert_text(self, *args, where='screen'):
        if where == 'screen':
            self.__text_screen.write(END, *args)
        elif where == 'list':
            self.__list_summary.write(END, *args)

    def screen_top_level(self):
        tl = Toplevel()
        tl.geometry('+200+37')

        frame = Frame(tl)

        temporary_screen = Text(frame, width=100, height=30, bd=20, font='12')
        temporary_screen.insert(1.0, self.__text_screen.get_text(1.0, END))
        temporary_screen.config(state='disabled', insertunfocussed='hollow')
        temporary_screen.configure(tabstyle='wordprocessor', wrap='word')

        scr_text_x = Scrollbar(frame, orient='horizontal', command=temporary_screen.xview)
        scr_text_x.grid(row=2, column=1, sticky=W + E)
        scr_text_y = Scrollbar(frame, orient='vertical', command=temporary_screen.yview)
        scr_text_y.grid(row=1, column=2, sticky=N + S)

        temporary_screen.config(yscrollcommand=scr_text_y.set, xscrollcommand=scr_text_x.set)
        temporary_screen.grid(row=1, column=1)

        frame.pack(fill='both')

        tl.mainloop()
