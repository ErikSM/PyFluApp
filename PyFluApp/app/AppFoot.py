from tkinter import Tk, Text, Frame, END, Scrollbar, W, E, N, S

from app.executions import processing_but_other, configuring_buts
from data.content_configs import colr, letter, width, height
from data.content_welcome import hello_string


class AppFoot:

    def __init__(self, main_window: Tk):

        self.__buts_others: None
        self.__text_note: Text

        foot = Frame(main_window, bg=colr['purple'], width=100, height=100, bd=3)

        self.__center = self._config_center(foot)
        self.__center.grid(row=1, column=1)

        foot.pack()


    def _config_center(self, foot):
        center = Frame(foot, bg=colr['purple'])

        self.__buts_others = configuring_buts(center, 'others', self.click_any_but_others)
        for i in self.__buts_others[0]:
            i.pack()
        self.__buts_others[1].grid(row=2, rowspan=3, column=1)


        self.__text_note = Text(center, font=letter['note'],
                                selectforeground='black', selectbackground='white', insertbackground='white',
                                bg=colr['purple'], fg=colr['white'], bd=10, height=height['not'], width=width['not'])


        scr_note_x = Scrollbar(center, orient='horizontal', command=self.__text_note.xview)
        scr_note_x.grid(row=4, column=4, sticky=W + E)
        scr_note_y = Scrollbar(center, orient='vertical', command=self.__text_note.yview)
        scr_note_y.grid(row=3, rowspan=4, column=3, sticky=N + S)

        self.__text_note.config(yscrollcommand=scr_note_y.set, xscrollcommand=scr_note_x.set)
        self.__text_note.grid(row=3, column=4)

        self.__text_note.insert(1.0, hello_string)

        return center

    def click_any_but_others(self, selected: str):
        self.__text_note.delete(0.0, END)

        processed = processing_but_other(selected)
        text_str, more_action, action = processed

        self.__text_note.insert(END, text_str)
        if more_action:
            action()

    def default(self):
        self.__text_note.delete(0.0, END)
        self.__text_note.insert(1.0, hello_string)

    def update_size(self, new_w: dict, new_h: dict, new_l: dict):
        self.__text_note.config(width=new_w['not'], height=new_h['not'], font=new_l['note'])

    def update_font(self, new_letters: dict):
        self.__text_note.config(font=new_letters['not'])
