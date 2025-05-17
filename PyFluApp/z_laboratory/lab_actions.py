from tkinter import Tk, Button, Toplevel

import webview
import webbrowser
import urllib.request


class Access:

    def __init__(self, url):

        self.__tk = Toplevel()
        self.__webview = webview
        self.__url = url

        self.__url_search = urllib.request.urlopen(self.__url)



    def page_url_open_in_tkinter_window(self):
        self.__webview.create_window('Image Open in tkinter (webview)', self.__url)
        self.__webview.start()

    def url_open_on_browser(self):
        self.__tk.title("Abrir no navegador??")
        self.__tk.geometry("400x50")
        self.__tk.config(bd=5)
        Button(self.__tk, text='open browser', command=lambda: webbrowser.open(self.__url)). pack()
        self.__tk.mainloop()

    def save_image_from_url_selected(self, file_name_and_ext, size):
        with open(f"{file_name_and_ext}", "wb") as file:
            chunk_size = size
            while True:
                chunk = self.__url_search.read(chunk_size)
                if not chunk:
                    break
                file.write(chunk)
