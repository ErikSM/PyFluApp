from tkinter import *

from app.AppBody import AppBody
from app.AppFoot import AppFoot
from app.AppHead import AppHead
from app.AppMenu import AppMenu
from app.CentralControl import CentralControl
from data.content_configs import colr


class AppMain:

    def __init__(self):

        self.__window = Tk()

        self.__app_head = AppHead(self.__window)
        self.__app_body = AppBody(self.__window)
        self.__app_foot = AppFoot(self.__window)

        self.__central_control = CentralControl(self.__app_head, self.__app_body, self.__app_foot)

        self.__app_menu = AppMenu(self.__window, self.__central_control)

    def _config_window(self):
        self.__window.config(bg=colr['purple'])

        self.__window.resizable(False, False)
        self.__window.geometry('+188+47')

        self.__window.title('Fluent Python App Study (Não oficial)')

    def start_app(self):
        self._config_window()
        self.__window.mainloop()
