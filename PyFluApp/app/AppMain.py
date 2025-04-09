from tkinter import *

from app.config import font, colr, width, height
from data.summary import python_books
from structure.Book import Book
from app.web_actions import access_website


class AppMain:

    def __init__(self):

        self.__window = Tk()

        self.__pybook_selected = None
        self.__img_banner = PhotoImage(file=r'assets\banner.PNG')

        self.__head = Frame(self.__window, bg=colr['purple'], width=100, height=100, bd=3)

        self.__container_u = Frame(self.__head, bg=colr['purple'])
        self.__label_img_banner = Label(self.__container_u)

        self.__body = Frame(self.__window, bg=colr['purple'], width=100, height=100, bd=3)

        self.__container_l = Frame(self.__body, bg=colr['purple'], width=30)
        self.__str_opt_book = StringVar(value='Click to Select Python Book')
        self.__tuple_opt_books = python_books.keys()
        self.__opt_menu_books = OptionMenu(self.__container_l, self.__str_opt_book, *self.__tuple_opt_books,
                                           command=lambda opt_str=self.__str_opt_book: self._active_opt_menu(opt_str))
        self.__list_summary = Listbox(self.__container_l)

        self.__container_c = Frame(self.__body, bg=colr['purple'], width=30)
        self.__buts_actions = self._set_buts(self.__container_c, 'act_buts')

        self.__container_r = Frame(self.__body, bg=colr['purple'], width=30)
        self.__entry_text_str = StringVar()
        self.__entry_local = Entry(self.__container_r)
        self.__text_screen = Text(self.__container_r)

        self.__foot = Frame(self.__window, bg=colr['purple'], width=100, height=100, bd=3)

        self.__container_d = Frame(self.__foot, bg=colr['purple'])
        self.__buts_others = self._set_buts(self.__container_d, 'others')
        self.__text_note = Text(self.__container_d)

        self._enable_config()

    def _set_buts(self, container, type_buts, font=font):

        buts = list()
        values = tuple()
        temporaty_container = None

        if type_buts == 'act_buts':
            values = 11, font['but_act'], 10, 5, 3, DISABLED, colr['grey'], colr['purple'], container
        elif type_buts == 'others':
            temporaty_container = Frame(container)
            values = 7, font['but_other'], 40, 0, 0, NORMAL, colr['purple'], colr['white'], temporaty_container

        how_many, font = values[0], values[1]
        width, height, bd = values[2], values[3], values[4]
        state, bg, fg =  values[5], values[6] ,values[7]
        local = values[8]

        cont = 1
        while cont <= how_many:
            buts.append(Button(local, font=font,
                               width=width, height=-height, bd=bd,
                               state=state, bg=bg, fg=fg))
            cont += 1

        if type_buts == 'act_buts':
            buts[0].config(bg=colr['purple'], bd=0)
            buts[2].config(text='play      >', command=self._click_but_play,
                           font=font, width=width, height=-height, bd=bd, state=NORMAL, bg=bg, fg=fg)
            return buts

        elif type_buts == 'others':
            all_names = ('Acesse o Site Oficial', 'Sobre o Autor do Livro', 'Sobre o Aplicativo',
                            '* Outras fontes de estudo', '* Dicas adicionais', '* Sugestoes', '* Contato comigo',  ' ')
            cont = 0
            for i in buts:
                name = all_names[cont]
                i.config(text=f'{name}', command=lambda selected=(name, all_names): self._click_ohters_but(selected))
                cont += 1

            return buts, temporaty_container

    def _config_container_u(self):
        self.__label_img_banner.configure(image=self.__img_banner)
        self.__label_img_banner.pack(side=LEFT)

        self.__container_u.pack()

    def _config_container_l(self):
        self.__opt_menu_books.config(bg=colr['white grey'], width=width['opt'], bd=3, anchor='center', state=NORMAL)
        self.__opt_menu_books.grid(row=2, column=1)

        self.__list_summary.config(font=font['list'], bg=colr['grey'], fg=colr['white'], bd=15)
        self.__list_summary.config(width=width['lis'], height=height['lis'])
        self.__list_summary.grid(row=3, column=1, columnspan=4)

        scr_list_x = Scrollbar(self.__container_l, orient=HORIZONTAL, command=self.__list_summary.xview)
        scr_list_x.grid(row=4, column=1, columnspan=5, sticky=W + E)
        self.__list_summary.config(xscrollcommand=scr_list_x.set)

        scr_list_y = Scrollbar(self.__container_l, orient=VERTICAL, command=self.__list_summary.yview)
        scr_list_y.grid(row=3, rowspan=4, column=0, sticky=N + S)
        self.__list_summary.config(yscrollcommand=scr_list_y.set)

        self.__container_l.grid(row=0, column=0)

    def _active_opt_menu(self, selected):
        self.__list_summary.delete(0, END)
        self.__pybook_selected = Book(selected)

        self.__list_summary.insert(END, *self.__pybook_selected.summary())

    def _config_container_c(self):
        for i in self.__buts_actions:
            i.pack()

        self.__container_c.grid(row=0, column=1)

    def _click_but_play(self):
        self.__text_screen.delete(1.0, END)

        selected = self.__list_summary.get(ANCHOR)

        parentheses = selected.find(')')
        file_name = selected[:parentheses]
        file_name = file_name.replace(' ', '')
        file_name = file_name.replace('.', '')

        try:
            file = self.__pybook_selected[file_name]
        except TypeError:
            file = (f'    [ book not found ]\n\n\n'
                        f'Acesse:\n'
                        f'          https://pythonfluente.com/')

        self.__text_screen.insert(END, file)

    def _config_container_r(self):
        self.__entry_local.config(font=font['search'], textvariable=self.__entry_text_str)
        self.__entry_local.config(width=width['ent'], bd=5, bg=colr['white'], fg=colr['purple'], state=DISABLED)
        self.__entry_local.grid(row=2, column=3, columnspan=4)

        self.__text_screen = Text(self.__container_r, font=font['principal'],
                                  bg=colr['grey'], fg=colr['white'], bd=3, height=height['tex'], width=width['tex'])
        self.__text_screen.grid(row=3, column=3)

        scr_text_x = Scrollbar(self.__container_r, orient=HORIZONTAL, command=self.__text_screen.xview)
        scr_text_x.grid(row=4, column=3, sticky=W + E)
        self.__text_screen.config(xscrollcommand=scr_text_x.set)

        scr_text_y = Scrollbar(self.__container_r, orient=VERTICAL, command=self.__text_screen.yview)
        scr_text_y.grid(row=3, rowspan=4, column=4, sticky=N + S)
        self.__text_screen.config(yscrollcommand=scr_text_y.set)

        self.__container_r.grid(row=0, column=2)

    def _config_container_d(self):
        for i in self.__buts_others[0]:
            i.pack()
        self.__buts_others[1].grid(row=3, rowspan=1, column=1)

        self.__text_note.config(font=font['principal'],
                                selectforeground='black', selectbackground='white', insertbackground='white',
                                bg=colr['purple'], fg=colr['white'], bd=10, height=height['not'], width=width['not'])
        self.__text_note.grid(row=3, column=4, columnspan=5)

        scr_note_x = Scrollbar(self.__container_d, orient=HORIZONTAL, command=self.__text_note.xview)
        scr_note_x.grid(row=4, column=4, columnspan=5, sticky=W + E)
        self.__text_note.config(xscrollcommand=scr_note_x.set)

        scr_note_y = Scrollbar(self.__container_d, orient=VERTICAL, command=self.__text_note.yview)
        scr_note_y.grid(row=3, rowspan=2, column=3, sticky=N + S)
        self.__text_note.config(yscrollcommand=scr_note_y.set)

        self.__container_d.grid(row=1, column=1)

    def _click_ohters_but(self, but_selected_and_all_buts:tuple):
        self.__text_note.delete(1.0, END)
        string = ''

        selected, all_buts = but_selected_and_all_buts[0], but_selected_and_all_buts[1]

        if selected == all_buts[0]:
            oficial = 'https://pythonfluente.com/'

            string = f'Acesse o site oficial:  {oficial}'
            self.__text_note.insert(1.0, string)

            access_website(oficial)

        elif selected == all_buts[1]:
            string = ('     Luciano Ramalho é programador Python desde 1998, Parceiro da Python Software Foundation; \n'
                      'é sócio do Python.pro.br – uma empresa de treinamento – e cofundador do Garoa Hacker Clube, \n'
                      'o primeiro hackerspace do Brasil. Tem liderado equipes de desenvolvimento de software e \n'
                      'ministrado cursos sobre Python em empresas de mídia, bancos e para o governo federal.')

        elif selected == all_buts[2]:
            string =  (
                """    
                    Este aplicativo tem como principal objetivo o desenvolvimento pessoal do criador na linguagem
                Python e não tem fins lucrativos, procurando ao máximo não ferir direitos autorais.
    
                    Este aplicativo também busca, na medida do possível, ajudar na divulgação da fonte do conteúdo
                original e por isso, não apresenta o conteúdo na sua totalidade, mas sim, de forma resumida para
                incentivar outros possíveis usuários do aplicativo a irem até o local do conteúdo original e conhecer
                tanto o conteúdo na sua totalidade quanto o autor do livro.
    
                    Sendo assim, em caso de alguma queixa ou desagrado com o autor ou dono dos direitos do conteúdo,
                o criador do app esta disposto a modificar ou eliminar o conteúdo do aplicativo ou até mesmo remove-lo
                (remover o app) do github e por um fim ao acesso a este aplicativo.
                """
            )

        elif selected == all_buts[6]:
            string = ('Principal\n'
                      '    GitHub:     https://github.com/ErikSM \n\n'
                      'Outras formas\n'
                      '    Instagram:     https://www.instagram.com/erik_miyajima/#\n'
                      '    Linkedin:      https://www.linkedin.com/in/erik-miyajima-355a7223b/\n'
                      '    Facebook:      https://www.facebook.com/profile.php?id=100009124251611\n')

        else:
            string = f'{selected}:   Not defined yet, Sorry!'

        self.__text_note.insert(1.0, string)

    def _enable_config(self):
        self._config_container_u()
        self._config_container_l()
        self._config_container_c()
        self._config_container_r()
        self._config_container_d()

    def _config_window(self):
        self.__window.config(bg=colr['purple'])
        self.__window.resizable(True, True)
        self.__window.geometry('+15+10')
        self.__window.title('Fluent Python App Study')

    def start_app(self):
        self.__head.pack()
        self.__body.pack()
        self.__foot.pack()

        self._config_window()
        self.__window.mainloop()
