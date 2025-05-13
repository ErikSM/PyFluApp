from data.content_configs import colr, letter, width, height, main_geometry


class Config:

    def __init__(self):
        self.__config = colr, letter, width, height, main_geometry

        self.__current_reference_size = 0
        self.__calculation_values = {'plus': (5, 9, 3), 'less': (-5, -9, -3)}
        self.__widget_not_edit = ['title', 'opt', 'bt_act', 'bt_oth'], ['title', 'note']


    def __getitem__(self, item):
        return self.__config[int(item)]

    def set_some_type_letter(self, witch: str, font='Arial', size=8, shape='bold'):
        self.__config[1][witch] = (font, size, shape)

    def set_size_in_proportion(self, plus_or_less: str, width_or_height='both'):
        not_edit_key = self.__widget_not_edit[0]

        how_much_change = self.__calculation_values[plus_or_less]
        self.__current_reference_size += how_much_change[0]

        if  0 <= self.__current_reference_size <= 10:
            if width_or_height == 'width' or width_or_height == 'both':
                for i in self.__config[2]:
                    if i not in not_edit_key:
                        self.__config[2][i] += how_much_change[1]

            if width_or_height == 'height' or width_or_height == 'both':
                for i in self.__config[3]:
                    if i not in not_edit_key:
                        self.__config[3][i] += how_much_change[2]


        if not 0 <= self.__current_reference_size <= 10:
            if self.__current_reference_size < 0:
                self.__current_reference_size = 0
            elif self.__current_reference_size > 10:
                self.__current_reference_size = 10


        self._auto_letter_size_set()

    def _auto_letter_size_set(self):
        not_edit_key = self.__widget_not_edit[1]

        if self.__current_reference_size < 5:
            for i in self.__config[1]:
                if i not in not_edit_key:
                    if i == 'list':
                        size = 7
                    else:
                        size = 8
                    self.__config[1][i][1] = size

        if  self.__current_reference_size == 5:
            for i in self.__config[1]:
                if i not in not_edit_key:
                    if i == 'list':
                        size = 8
                    else:
                        size = 10
                    self.__config[1][i][1] = size

        if self.__current_reference_size > 5:
            for i in self.__config[1]:
                if i not in not_edit_key:
                    if i == 'list':
                        size = 9
                    else:
                        size = 11
                    self.__config[1][i][1] = size
