from tkinter import Listbox, Scrollbar, END, ANCHOR
from data.content_configs import letter, colr, height, width


class Summary:

    def __init__(self, frame):
        self.__summary = Listbox(frame, font=letter['list'], bg=colr['grey'], fg=colr['white'],
                                 width=width['lis'], height=height['lis'], bd=15)

        self.__scroll_x = Scrollbar(frame, orient='horizontal', command=self.__summary.xview)
        self.__scroll_y = Scrollbar(frame, orient='vertical', command=self.__summary.yview)

        self.__widgets = {'summary': self.__summary, 'scroll_x': self.__scroll_x, 'scroll_y':self.__scroll_y}

    def grid_config(self, widget, **kwargs):
        self.__widgets[widget].grid(kwargs)
        self.__summary.config(yscrollcommand=self.__scroll_y.set, xscrollcommand=self.__scroll_x.set)

    def configure_widget(self, widget='summary', **kwargs):
        self.__widgets[widget].config(kwargs)

    def write(self, param=END, *args):
        self.__summary.insert(param, *args)

    def delete_option(self, param=0, end_param=END):
        self.__summary.delete(param, end_param)

    def update_content(self, *summary_content):
        self.__summary.delete(0, END)
        self.__summary.insert(1, *summary_content)

    def get_selected(self):
        return self.__summary.get(ANCHOR)
