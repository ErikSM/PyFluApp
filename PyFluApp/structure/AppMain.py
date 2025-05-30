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

        self.__app = AppHead(self.__window), AppBody(self.__window), AppFoot(self.__window)
        self.__central_control = CentralControl(self.__app)
        self.__app_menu = AppMenu(self.__window, self.__central_control)


    def _config_window(self):
        self.__window.config(bg=colr['purple'])

        self.__window.resizable(False, False)
        self.__window.geometry('+188+47')

        self.__window.title('Fluent Python App Study (Não oficial)')

    def config_app_interaction(self):
        self.__app[0].add_command_to_max_min_but(self.__app_menu.click_maximize, self.__app_menu.click_minimize)

    def start_app(self):
        self.config_app_interaction()

        self._config_window()
        self.__window.mainloop()

