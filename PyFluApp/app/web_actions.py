import webbrowser
from tkinter import Button, Label, LEFT, Frame, Toplevel


def access_website(url):
    tk = Toplevel()
    tk.title("Acessar o Site no Browser")
    tk.geometry("400x65+350+500")
    tk.config(bd=5)

    Label(tk, text=f'Deseja acessar: {url} \nem seu Browser Padrao???').pack()

    buts = Frame(tk)
    Button(buts, text='Sim    ', command=lambda: _but_access_website(url, tk, True)).pack(side=LEFT)
    Button(buts, text='    Nao', command=lambda: _but_access_website(url, tk, False)).pack(side=LEFT)
    buts.pack()

    tk.mainloop()


def _but_access_website(url: str, tk: Toplevel, yes_or_not: bool):
    if yes_or_not:
        webbrowser.open(url)
    else:
        pass
    tk.destroy()
