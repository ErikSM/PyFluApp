from tkinter import Tk, Frame, END, W, E, N, S

from app.CustomButton import CustomButton
from app.Screen import Screen
from data.content_configs import colr
from data.content_welcome import hello_string


class AppFoot:

    def __init__(self, main_window: Tk):
        self.__foot = self._foot_frame(main_window)
        self.__center = self._config_center()


    def _foot_frame(self, main_window):
        self.__foot = Frame(main_window, bg=colr['purple'], width=100, height=100, bd=3)
        self.__foot.pack()

        return self.__foot

    def _config_center(self):
        center = Frame(self.__foot, bg=colr['purple'])

        self.__oth_buts = CustomButton(center, 'others', self.click_any_but_others)
        self.__oth_buts.layout('grid', row=2, rowspan=3, column=1)

        self.__terminal = Screen('terminal', center)
        self.__terminal.grid_config('screen', row=3, column=4)
        self.__terminal.grid_config('scroll_x', row=4, column=4, sticky=W + E)
        self.__terminal.grid_config('scroll_y', row=3, rowspan=4, column=3, sticky=N + S)
        self.__terminal.write(1.0, hello_string)

        center.grid(row=1, column=1)

        return center

    def click_any_but_others(self, selected: str):
        self.__terminal.delete_text(0.0, END)

        processed = self.__oth_buts.processing_but('others', selected)
        self.__terminal.write(END, processed[0])
        if processed[1]:
            processed[2]()

    def default(self):
        self.__terminal.delete_text(0.0, END)
        self.__terminal.write(1.0, hello_string)

    def update_size(self, new_w: dict, new_h: dict, new_l: dict):
        self.__terminal.configure_widget('screen', width=new_w['not'], height=new_h['not'], font=new_l['note'])

    def update_font(self, new_letters: dict):
        self.__terminal.configure_widget('screen', font=new_letters['not'])

    def update_color(self, theme: list):
        self.__foot.config(bg=theme[0])
        self.__center.config(bg=theme[0])

        self.__terminal.configure_widget('screen', bg=theme[0], fg=theme[1])

        self.__oth_buts.update_color(theme[0], theme[1])
