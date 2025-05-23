from tkinter import Menu, Tk
from app.CentralControl import CentralControl
from data.all_errors import error_historic
from data.content_configs import colr, themes


class AppMenu:

    def __init__(self, main_window: Tk, central: CentralControl):
        self.__window = main_window

        self.__central = central  # [0]=Head, [1]=Body, [2]=Foot, [3]=Config

        self.__menu = self._config_menu()
        self.__bar = self._create_menu_bar()


    def _create_menu_bar(self):
        self.__menu_file = self._config_menu_arquivo()
        self.__menu_edit = self._config_menu_edit()
        self.__menu_info = self._config_menu_info()

        self.__window.config(menu=self.__menu)

        return self.__menu_file, self.__menu_edit, self.__menu_info

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

        appearance = Menu(edit, tearoff=0)
        all_theme = themes.keys()
        for i in all_theme:
            appearance.add_command(label=f'{i}', command=lambda choice=i: self.click_themes(choice))

        edit.add_cascade(label='Aparência', menu=appearance)
        self.__menu.add_cascade(label='Editar', menu=edit)

        return edit

    def _config_menu_info(self):
        info = Menu(self.__menu, tearoff=0)

        report = Menu(info, tearoff=0)
        report.add_command(label='relatorio de erros', command=self.click_errors_report)

        info.add_cascade(label='relatório', menu=report)
        self.__menu.add_cascade(label='Informações', menu=info)

        return info

    def _max_geometry(self):
        sizes = self.__central[3][4][0]
        ext = self.__central[3][4][1]

        geometry = self.__window.wm_geometry()

        try:
            position_found = sizes.index(f"{geometry[:geometry.find('+')]}")
        except Exception as ex:
            print(ex)
        else:

            result = position_found  + 1
            if result == 4:
                new_position = 3
            else:
                new_position = result

            try:
                self.__window.geometry(f'{sizes[new_position]}{ext[new_position]}')
            except IndexError:
                pass

    def _min_geometry(self):
        sizes = self.__central[3][4][0]
        ext = self.__central[3][4][1]

        geometry = self.__window.wm_geometry()

        try:
            position_found  = sizes.index(f"{geometry[:geometry.find('+')]}")
        except Exception as ex:
            print(ex)
        else:
            result = position_found - 1
            if result == -1:
                new_position = 0
            else:
                new_position = result

            try:
                self.__window.geometry(f'{sizes[new_position]}{ext[new_position]}')
            except IndexError:
                pass

    def click_start(self):
        self.__central[1].default()
        self.__central[2].default()

    def click_sair(self):
        self.__window.destroy()

    def click_maximize(self):

        self.__central[3].set_size_in_proportion('plus')

        self.__central[1].update_size(self.__central[3]['2'], self.__central[3]['3'], self.__central[3]['1'])
        self.__central[2].update_size(self.__central[3]['2'], self.__central[3]['3'], self.__central[3]['1'])

        self._max_geometry()

    def click_minimize(self):

        self.__central[3].set_size_in_proportion('less')

        self.__central[1].update_size(self.__central[3]['2'], self.__central[3]['3'], self.__central[3]['1'])
        self.__central[2].update_size(self.__central[3]['2'], self.__central[3]['3'], self.__central[3]['1'])

        self._min_geometry()

    def click_themes(self, choice):
        theme = themes[choice]

        self.__central[0].update_color(theme)
        self.__central[1].update_color(theme)
        self.__central[2].update_color(theme)

        self.__window.config(bg=theme[0])

    def click_errors_report(self):
        self.__central[1].del_text()

        if len(error_historic) == 0:
            self.__central[1].insert_text(f'\n\n{' ' * 13} [ Nothing found ]\n\n{' ' * 18} No errors yet\n')
        else:
            for i in error_historic:
                ex = f'\n\n{i}\n   {error_historic[i]}'
                self.__central[1].insert_text(ex)
