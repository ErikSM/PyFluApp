from tkinter import Entry, StringVar, END

from data.content_configs import letter, colr, width


class PathScreen:

    def __init__(self, frame):
        self.__str_var = StringVar(value='..//')

        self.__path = Entry(frame, textvariable=self.__str_var, font=letter['search'],
                                  disabledbackground=colr['grey'], disabledforeground=colr['purple'],
                                  width=width['ent'], bd=5, state='disabled')


    def grid_config(self, **kwargs):
        self.__path.grid(kwargs)

    def configure_widget(self, **kwargs):
        self.__path.config(kwargs)

    def write(self, param, text):
        self.__path.insert(param, text)

    def delete_text(self, param=0, end_param=END):
        self.__path.delete(param, end_param)

