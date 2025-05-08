from data.content_configs import colr, letter, width, height, main_geometry


class Config:

    def __init__(self):
        self.__config = colr, letter, width, height, main_geometry

        self.__size_reference = 0
        self.__calculation_values = {'plus': (5, 9, 3), 'less': (-5, -9, -3)}
        self.__not_edit_key = ['title', 'opt', 'bt_act', 'bt_oth']

    def __getitem__(self, item):
        return self.__config[int(item)]


    def set_some_type_letter(self, witch: str, font='Arial', size=8, shape='bold'):
        self.__config[1][witch] = (font, size, shape)


    def set_size_in_proportion(self, plus_or_less: str, width_or_height='both', geometry=''):
            print(geometry)

            how_much = self.__calculation_values[plus_or_less]
            self.__not_edit_key = ['title', 'opt', 'bt_act', 'bt_oth']

            self.__size_reference += how_much[0]

            if not  0 <= self.__size_reference <= 10 :
                if self.__size_reference < 0:
                    self.__size_reference = 0
                elif self.__size_reference > 10:
                    self.__size_reference = 10
            else:
                self._auto_letter_size_set()

                if width_or_height == 'width' or width_or_height == 'both':
                        for i in self.__config[2]:
                                if i not in self.__not_edit_key:
                                    self.__config[2][i] += how_much[1]

                if width_or_height == 'height' or width_or_height == 'both':
                        for i in self.__config[3]:
                            if i not in self.__not_edit_key:
                                self.__config[3][i] += how_much[2]

                print(self.__size_reference)


    def _auto_letter_size_set(self):
        self.__not_edit_key = ['title', 'note']

        if self.__size_reference < 5:
            for i in self.__config[1]:
                if i not in self.__not_edit_key:
                    if i == 'list':
                        size = 7
                    else:
                        size = 8
                    self.__config[1][i][1] = size

        if  self.__size_reference == 5:
            for i in self.__config[1]:
                if i not in self.__not_edit_key:
                    if i == 'list':
                        size = 8
                    else:
                        size = 10
                    self.__config[1][i][1] = size

        if self.__size_reference > 5:
            for i in self.__config[1]:
                if i not in self.__not_edit_key:
                    if i == 'list':
                        size = 9
                    else:
                        size = 11
                    self.__config[1][i][1] = size
