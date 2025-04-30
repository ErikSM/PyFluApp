from tkinter import Menu, Tk

from app.CentralControl import CentralControl
from data.content_configs import colr, themes


class AppMenu:

    def __init__(self, window: Tk, central: CentralControl):
        self.__window = window
        self.__central = central

        self.__menu = self._config_menu()

        self.__menu_file = self._config_menu_arquivo()
        self.__menu_edit= self._config_menu_edit()

        self.__window.config(menu=self.__menu)


    def _config_menu(self):
        menu = Menu(self.__window, selectcolor=colr['purple'], type="menubar")

        return menu

    def _config_menu_arquivo(self):
        file = Menu(self.__menu, tearoff=0)

        file.add_command(label='inicio', command=self.click_start)
        file.add_command(label='sair', command=self.click_sair)

        self.__menu.add_cascade(label='Arquivo', menu=file)

        return file

    def _config_menu_edit(self):
        edit = Menu(self.__menu, tearoff=0)

        resize = Menu(edit, tearoff=0)
        resize.add_command(label='maximizar', command=self.click_maximize)
        resize.add_command(label='minimizar', command=self.click_minimize)
        edit.add_cascade(label='Redimensionar', menu=resize)

        appearance = Menu(edit, tearoff=0)
        all_theme = themes.keys()
        for i in all_theme:
            appearance.add_command(label=f'{i}', command=lambda choice=i: self.click_themes(choice))

        edit.add_cascade(label='Aparência', menu=appearance)
        self.__menu.add_cascade(label='Editar', menu=edit, compound='right')

        return edit

    def click_start(self):
        self.__central[1].default()
        self.__central[2].default()

    def click_sair(self):
        self.__window.destroy()

    def click_maximize(self):
        geometry = self.__window.wm_geometry()

        self.__central[3].set_size_in_proportion('plus', geometry=geometry)

        self.__central[1].update_size(self.__central[3]['2'], self.__central[3]['3'], self.__central[3][1])
        self.__central[2].update_size(self.__central[3]['2'], self.__central[3]['3'], self.__central[3][1])

    def click_minimize(self):
        geometry = self.__window.wm_geometry()

        self.__central[3].set_size_in_proportion('less', geometry=geometry)

        self.__central[1].update_size(self.__central[3]['2'], self.__central[3]['3'], self.__central[3][1])
        self.__central[2].update_size(self.__central[3]['2'], self.__central[3]['3'], self.__central[3][1])

    def click_themes(self, choice):
        theme = themes[choice]

        self.__central[0].update_color(theme)
        self.__central[1].update_color(theme)
        self.__central[2].update_color(theme)

        self.__window.config(bg=theme[0])