from tkinter import Tk, Menu

from app.AppBody import AppBody
from app.AppFoot import AppFoot
from app.Config import Config

#  in progress

class MenuBar:

    def __init__(self, main_window: Tk, body: AppBody, foot: AppFoot):

        self.__window = main_window
        self.__config = Config()

        self.__default = body.default, foot.default
        self.__size_update = body.update_size, foot.update_size

        self.__menu = self._config_bar()

        self.__menu_file = self._config_menu_arquivo()
        self.__menu_edit= self._config_menu_edit()

    def _config_menu_arquivo(self):
        file = Menu(self.__menu, tearoff=0)

        file.add_command(label='inicio', command=self.click_start)
        file.add_command(label='sair', command=self.click_sair)

        self.__menu.add_cascade(label='Arquivo', menu=file)

        return file

    def _config_menu_edit(self):
        file = Menu(self.__menu, tearoff=0, relief='sunken')

        file.add_command(label='maximizar', command=self.click_maximize)
        file.add_command(label='minimizar', command=self.click_minimize)

        self.__menu.add_cascade(label='Editar', menu=file)

        return file

    def _config_bar(self):
        bar = Menu(self.__window, tearoff=0)
        self.__window.config(menu=bar)

        return bar

    def click_start(self):
        for i in self.__default:
            i()

    def click_sair(self):
        self.__window.destroy()


#  in progress
    def click_maximize(self):
        sizes = self.__config.set_size_in_proportion('both', 2)

        for i in self.__size_update:
            i(sizes)

    def click_minimize(self):
        sizes  = self.__config.set_size_in_proportion('both', -2)

        for i in self.__size_update:
            i(sizes)

