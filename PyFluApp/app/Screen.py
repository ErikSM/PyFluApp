from tkinter import Text, Scrollbar, END
from data.content_configs import letter, colr, width, height


def choice_text(screen, frame):
    if screen == 'notes':
        return Text(frame, bd=10,
                    font=letter['screen'], height=height['tex'], width=width['tex'],bg=colr['grey'], fg=colr['yellow'],
                    selectbackground=colr['yellow'], tabstyle='wordprocessor', wrap='word', insertunfocussed='hollow')
    elif screen == 'terminal':
        return Text(frame,
                    font=letter['note'], bg=colr['purple'], fg=colr['white'], height=height['not'], width=width['not'],
                    selectforeground='black', selectbackground='white', insertbackground='white', bd=10)
    else:
        return Text(frame)


class Screen:

    def __init__(self, screen ,frame):

        self.__txt_principal = choice_text(screen, frame)

        self.__scroll_x = Scrollbar(frame, orient='horizontal', command=self.__txt_principal.xview)
        self.__scroll_y = Scrollbar(frame, orient='vertical', command=self.__txt_principal.yview)

        self.__widgets = {'screen': self.__txt_principal, 'scroll_x': self.__scroll_x, 'scroll_y':self.__scroll_y}


    def grid_config(self, widget, **kwargs):
        self.__widgets[widget].grid(**kwargs)
        self.__txt_principal.config(yscrollcommand=self.__scroll_y.set, xscrollcommand=self.__scroll_x.set)

    def configure_widget(self, widget='screen',  **kwargs):
        self.__widgets[widget].config(kwargs)

    def write(self, param=END, text:str=''):
        self.__txt_principal.insert(param, text)

    def delete_text(self, param=1.0, end_param=END):
        self.__txt_principal.delete(param, end_param)

    def get_text(self, param=1.0, end_param=END):
        return self.__txt_principal.get(param, end_param)

