from tkinter import NORMAL, Frame, Button, Text

from data.content_but_other import other_buts_dict
from data.content_configs import colr, width, height, letter
from structure.WebAccess import WebAccess


class CustomButton:

    def __init__(self, app_frame: Frame, type_buts:str, command):
        self.__app_frame = app_frame
        self.__type_buts = type_buts
        self.__app_click_command = command

        self.__oth_content = other_buts_dict

        self.__buts = self._configuring_buts()


    def _configuring_buts(self):
        buts, buts_local = self._create_buts_list(self.__type_buts)

        if self.__type_buts == 'action':
            buts[1].config(text='play      >', bg=colr['purple'], bd=3, command=self.__app_click_command)

        elif self.__type_buts == 'others':
            all_buts = [i for i in other_buts_dict.keys()]
            cont = 0

            for i in buts:
                but_txt = all_buts[cont]
                i.config(text=f'{but_txt}',
                         command=lambda selected=but_txt: self.__app_click_command(selected))
                cont += 1

        return buts, buts_local

    def _create_buts_list(self, type_buts: str):
        buts = []
        values = ()

        font = letter
        buts_frame = Frame(self.__app_frame, bg=colr['purple'])

        if type_buts == 'action':
            values = (5, buts_frame, font['bt_act'], width['bt_act'],
                      height['bt_act'], 1, NORMAL, colr['grey'], colr['white'])

        elif type_buts == 'others':
            values = (6,buts_frame, font['bt_oth'],width['bt_oth'],
                      height['bt_oth'], 0, NORMAL, colr['purple'], colr['white'])

        how_many, local, font, x_size, y_size, bd, state, bg, fg = values

        cont = 1
        while cont <= how_many:
            buts.append(Button(local, font=font,width=x_size, height=y_size, bd=bd, state=state, bg=bg, fg=fg))
            cont += 1

        return buts, local

    def layout(self, pack_or_grid, **kwargs):
        for i in self.__buts[0]:
            i.pack()

        if pack_or_grid == 'pack':
            self.__buts[1].pack()
        if pack_or_grid == 'grid':
            # row=2, rowspan=3, column=1
            self.__buts[1].grid(**kwargs)

    def update_color(self, bg_theme, fg_theme):
        self.__buts[1].config(bg=bg_theme)
        for i in self.__buts[0]:
            i.config(bg=bg_theme, fg=fg_theme)


    def processing_but_other(self, selected: str):
        string = self.__oth_content[selected]

        web_browser = WebAccess('https://pythonfluente.com/').url_open_on_browser

        if selected == 'Acesse o Site Oficial':
            return string, True, web_browser
        else:
            return string, False




