from tkinter import Tk, Frame, Label, PhotoImage, Button
from structure.Config import colr


class AppHead:

    def __init__(self, main_window: Tk):

        self.__head = self._head_frame(main_window)
        self.__center = self._config_center()
        self.__right = self._config_right()


    def _head_frame(self, main_window):
        self.__head = Frame(main_window, bg=colr['purple'], width=100, height=100, bd=3)
        self.__head.pack(fill='both')

        return self.__head

    def _config_center(self):
        self.__img_banner = PhotoImage(file=r'assets\banner.PNG')
        self.__banner: Label

        center = Frame(self.__head, bg=colr['purple'])

        self.__banner = Label(center, image=self.__img_banner)
        self.__banner.pack(side='left')

        center.pack(side='bottom', anchor='center')

        return center

    def _config_right(self):
        self.__but_max: Button
        self.__but_min: Button

        right = Frame(self.__head, bg=colr['purple'])

        self.__but_max = Button(right, text=' [+] Max')
        self.__but_max.pack(side='right', anchor='nw')

        self.__but_min = Button(right, text='Min [-] ')
        self.__but_min.pack(side='right', anchor='nw')

        right.pack(side='right', anchor='nw')

        return right

    def add_command_to_max_min_but(self, max_comm, min_comm):
        self.__but_max.config(command=max_comm)
        self.__but_min.config(command=min_comm)

    def update_color(self, theme: list):
        self.__head.config(bg=theme[0])
        self.__center.config(bg=theme[0])
