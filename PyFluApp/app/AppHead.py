from tkinter import Tk, Frame, Label, PhotoImage

from structure.Config import colr


class AppHead:

    def __init__(self, main_window: Tk):
        self.__img_banner: PhotoImage

        self.__head = self._head_frame(main_window)

        self.__center = self._config_head()
        self.__center.grid(row=1, column=1)

        self.__head.pack()


    def _head_frame(self, main_window):
        self.__head = Frame(main_window, bg=colr['purple'], width=100, height=100, bd=3)

        return self.__head

    def _config_head(self):
        center = Frame(self.__head, bg=colr['purple'])

        self.__img_banner = PhotoImage(file=r'assets\banner.PNG')
        Label(center, image=self.__img_banner).pack(side='left')

        return center

    def update_color(self, theme: list):
        self.__head.config(bg=theme[0])
        self.__center.config(bg=theme[0])
