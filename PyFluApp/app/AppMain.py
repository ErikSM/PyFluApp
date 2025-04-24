from tkinter import *

from app.AppBody import AppBody
from app.AppFoot import AppFoot
from app.AppHead import AppHead
from app.MenuBar import MenuBar
from app.config import colr


class AppMain:

    def __init__(self):

        self.__window = Tk()

        self.__menu_bar = MenuBar(self.__window)

        self.__app_head = AppHead(self.__window)
        self.__app_body = AppBody(self.__window)
        self.__app_foot = AppFoot(self.__window)

    def _config_window(self):
        self.__window.config(bg=colr['purple'])
        self.__window.resizable(True, True)
        self.__window.geometry('+1+1')
        self.__window.title('Fluent Python App Study (Não oficial)')

    def start_app(self):
        self._config_window()

        self.__window.mainloop()
