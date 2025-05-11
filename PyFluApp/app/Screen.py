from tkinter import Text, Scrollbar, END

from data.content_configs import letter, colr, width, height
from data.content_welcome import attention_string


class Screen:

    def __init__(self, frame):

        self.__screen = Text(frame, font=letter['screen'], height=height['tex'], width=width['tex'], bd=10,
                             bg=colr['grey'], fg=colr['yellow'], selectbackground=colr['yellow'],
                             tabstyle='wordprocessor', wrap='word', insertunfocussed='hollow')

        self.__scroll_x = Scrollbar(frame, orient='horizontal', command=self.__screen.xview)
        self.__scroll_y = Scrollbar(frame, orient='vertical', command=self.__screen.yview)

        self.__widgets = {'screen': self.__screen, 'scroll_x': self.__scroll_x, 'scroll_y':self.__scroll_y}


    def grid_config(self, widget, **kwargs):
        self.__widgets[widget].grid(**kwargs)
        self.__screen.config(yscrollcommand=self.__scroll_y.set, xscrollcommand=self.__scroll_x.set)

    def configure_widget(self, widget='screen',  **kwargs):
        self.__widgets[widget].config(kwargs)

    def write(self, param=END, text:str=''):
        self.__screen.insert(param, text)

    def delete_text(self, param=1.0, end_param=END):
        self.__screen.delete(param, end_param)

    def get_text(self, param=1.0, end_param=END):
        return self.__screen.get(param, end_param)

