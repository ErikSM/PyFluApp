from tkinter import Tk, Button

import webview
import webbrowser
import urllib.request

url_test = 'https://pythonfluente.com/'


##  Classe para executar as funcoes ???????





def page_url_open_in_tkinter_window(url):
    webview.create_window('Image Open in tkinter (webview)', url)
    webview.start()


def url_open_on_browser(url):
    tk = Tk()
    tk.title("URL open on browser")
    tk.geometry("400x50")
    tk.config(bd=5)

    but = Button(tk, text='open browser', command=lambda: webbrowser.open(url))
    but.pack()

    tk.mainloop()


def save_image_from_url_selected(url, file_name_and_ext, size):
    url_search = urllib.request.urlopen(url)

    with open(f"{file_name_and_ext}", "wb") as file:
        chunk_size = size
        while True:
            chunk = url_search.read(chunk_size)
            if not chunk:
                break
            file.write(chunk)


face = "https://www.instagram.com/erik_miyajima/"

page_url_open_in_tkinter_window(face)

