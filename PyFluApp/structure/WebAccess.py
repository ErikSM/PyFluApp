from tkinter import Button, Label, Frame, Tk

import webbrowser
import urllib.request
import webview


class WebAccess:

    def __init__(self, url):
        self.__tk = None
        self.__webview = webview
        self.__url = url
        self.__webbrowser = webbrowser

        self.__url_search = urllib.request.urlopen(self.__url)

    def page_url_open_in_tkinter_window(self):
        self.__webview.create_window('Image Open in tkinter (webview)', self.__url)
        self.__webview.start()

    def url_open_on_browser(self):
        self.__tk = Tk()
        self.__tk.title("Acessar o Site no Browser")
        self.__tk.geometry("400x65+350+500")
        self.__tk.config(bd=5)

        Label(self.__tk, text=f'Deseja acessar: {self.__url} \nem seu Browser Padrao???').pack()

        buts = Frame(self.__tk)
        Button(buts, text='Sim    ',
               command=lambda: self._but_access_website(True)).pack(side='left')
        Button(buts, text='    Nao',
               command=lambda: self._but_access_website(False)).pack(side='left')
        buts.pack()

        self.__tk.mainloop()

    def _but_access_website(self, on_browser: bool):
        if on_browser:
            self.__webbrowser.open(self.__url)
        else:
            pass
        self.__tk.destroy()

    def save_image_from_url_selected(self, file_name_and_ext, size):
        with open(f"{file_name_and_ext}", "wb") as file:
            chunk_size = size
            while True:
                chunk = self.__url_search.read(chunk_size)
                if not chunk:
                    break
                file.write(chunk)

