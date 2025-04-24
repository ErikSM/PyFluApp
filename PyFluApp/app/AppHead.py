from tkinter import Tk, Frame, Label, PhotoImage

from app.config import colr


class AppHead:

    def __init__(self, main_window: Tk):
        self.__img_banner: PhotoImage

        head = Frame(main_window, bg=colr['purple'], width=100, height=100, bd=3)

        self.__center = self._config_head(head)
        self.__center.grid(row=1, column=1)

        head.pack()

    def _config_head(self, head):
        center = Frame(head, bg=colr['purple'])

        self.__img_banner = PhotoImage(file=r'assets\banner.PNG')
        Label(center, image=self.__img_banner).pack(side='left')

        return center