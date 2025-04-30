from tkinter import Tk, Menu

from app.AppBody import AppBody
from app.AppFoot import AppFoot
from app.AppHead import AppHead
from data.content_configs import themes, colr
from structure.Config import Config


class AppMenu:

    def __init__(self, main_window: Tk, head: AppHead, body: AppBody, foot: AppFoot):

        self.__window = main_window
        self.__head = head
        self.__body = body
        self.__foot = foot
        self.__config = Config()

        self.__menu = self._config_menu()

        self.__menu_file = self._config_menu_arquivo()
        self.__menu_edit= self._config_menu_edit()

        self.__window.config(menu=self.__menu)


    def _config_menu_arquivo(self):
        file = Menu(self.__menu, tearoff=0)

        file.add_command(label='inicio', command=self.click_start)
        file.add_command(label='sair', command=self.click_sair)

        self.__menu.add_cascade(label='Arquivo', menu=file)

        return file

    def _config_menu_edit(self):
        edit = Menu(self.__menu, tearoff=0, relief='sunken')

        resize = Menu(edit, tearoff=0)
        resize.add_command(label='maximizar', command=self.click_maximize)
        resize.add_command(label='minimizar', command=self.click_minimize)
        edit.add_cascade(label='Redimensionar', menu=resize)

        appearance = Menu(edit, tearoff=0)
        all_theme = 'tema 1', 'tema 2', 'tema 3'
        for i in all_theme:
            appearance.add_command(label=f'{i}', command=lambda choice=i: self.click_themes(choice))

        edit.add_cascade(label='Aparência', menu=appearance)
        self.__menu.add_cascade(label='Editar', menu=edit)

        return edit

    def _config_menu(self):
        menu = Menu(self.__window, selectcolor=colr['purple'], type="normal")

        return menu

    def click_start(self):
        self.__body.default()
        self.__foot.default()

    def click_sair(self):
        self.__window.destroy()

    def click_maximize(self):
        geometry = self.__window.wm_geometry()

        self.__config.set_size_in_proportion('plus', geometry=geometry)

        self.__body.update_size(self.__config['2'], self.__config['3'], self.__config[1])
        self.__foot.update_size(self.__config['2'], self.__config['3'], self.__config[1])

    def click_minimize(self):
        geometry = self.__window.wm_geometry()

        self.__config.set_size_in_proportion('less', geometry=geometry)

        self.__body.update_size(self.__config['2'], self.__config['3'], self.__config[1])
        self.__foot.update_size(self.__config['2'], self.__config['3'], self.__config[1])



    def click_themes(self, choice):
        theme = themes[choice]

        self.__head.update_color(theme)
        self.__body.update_color(theme)
        self.__foot.update_color(theme)

        self.__window.config(bg=theme[0])

