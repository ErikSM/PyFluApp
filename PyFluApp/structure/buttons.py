from tkinter import NORMAL, Frame, Button, COMMAND

from structure.web_actions import access_website_on_browser
from data.content_but_other import other_buts_dict
from data.content_configs import colr, width, height, letter


def processing_but_other(selected: str):
    action = None
    string = other_buts_dict[selected]

    if selected == 'Acesse o Site Oficial':
        more_action = True
        action = lambda: access_website_on_browser('https://pythonfluente.com/')
    else:
        more_action = False

    return string, more_action, action


def configuring_buts(container: Frame, type_buts: str, self_command: COMMAND):

    buts, buts_local = _create_but_list(container, type_buts)

    if type_buts == 'action':
        buts[1].config(text='play      >', bg=colr['purple'], bd=3, command=self_command)

    elif type_buts == 'others':
        all_buts = [i for i in other_buts_dict.keys()]
        cont = 0

        for i in buts:
            but_txt = all_buts[cont]
            i.config(text=f'{but_txt}',
                       command=lambda selected=but_txt: self_command(selected))
            cont += 1

    return buts, buts_local


def _create_but_list(container: Frame, type_buts: str):
    buts = []
    values = ()

    font = letter
    frame = Frame(container, bg=colr['purple'])

    if type_buts == 'action':
        values = (5, frame, font['bt_act'], width['bt_act'], height['bt_act'], 1, NORMAL, colr['grey'], colr['white'])

    elif type_buts == 'others':
        values = (6,frame, font['bt_oth'],width['bt_oth'], height['bt_oth'], 0, NORMAL, colr['purple'], colr['white'])

    how_many, local, font, x_size, y_size, bd, state, bg, fg = values

    cont = 1
    while cont <= how_many:
        buts.append(Button(local, font=font,width=x_size, height=y_size, bd=bd, state=state, bg=bg, fg=fg))
        cont += 1

    return buts, local
