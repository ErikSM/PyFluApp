from tkinter import Tk, Menu, Label


#  in progress
class MenuBar:

    def __init__(self, main_window: Tk):
        self.__window = main_window

        self.__menu = self._config_bar()

        self.__menu_file = self._config_menu_arquivo()
        self.__menu_edit= self._config_menu_edit()


    def click_new(self,  clear_all):
        pass


    def click_sair(self):
        self.__window.destroy()

    def _config_menu_arquivo(self):
        file = Menu(self.__menu, tearoff=0)

        file.add_command(label='Novo', command=self.click_new)
        file.add_command(label='sair', command=self.click_sair)

        self.__menu.add_cascade(label='Arquivo', menu=file)

        return file


    def click_maximeze(self):
        pass

    def click_minimize(self):
        pass


    def _config_menu_edit(self):
        file = Menu(self.__menu, tearoff=0)

        file.add_command(label='maximizar', command=self.click_maximeze)
        file.add_command(label='minimizar', command=self.click_minimize)

        self.__menu.add_cascade(label='Arquivo', menu=file)

        return file


    def _config_bar(self):
        bar = Menu(self.__window, tearoff=0)
        self.__window.config(menu=bar)

        return bar





