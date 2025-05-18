from tkinter import Entry, StringVar
from data.content_configs import letter, colr, width


class ContentPath:

    def __init__(self, frame):
        self.__str_value = StringVar(value='..//')

        self.__path = Entry(frame, textvariable=self.__str_value, font=letter['search'],
                            disabledbackground=colr['grey'], disabledforeground=colr['purple'],
                            width=width['ent'], bd=5, state='disabled')


    def __getitem__(self, item: str):
        if item == 'path_value':
            self.__str_value.get()
        else:
            pass

    def __setitem__(self, key: str, value: str):
        if key == 'path_value':
            self.__str_value.set(value=value)
        else:
            pass

    def grid_config(self, **kwargs):
        self.__path.grid(kwargs)

    def configure_widget(self, **kwargs):
        self.__path.config(kwargs)

