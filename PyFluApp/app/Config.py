from data.content_configs import colr, letter, width, height


class Config:

    def __init__(self):

        self.__color = colr
        self.__letter = letter
        self.__width = width
        self.__height = height

        self.__size_reference = 0
        self.__calculation_values = {'plus': +4, 'less': -4}
        self.__not_edit_key = None

    def __getitem__(self, item):
        items = self.__color, self.__letter, self.__width, self.__height
        return items[int(item)]

    def get_all(self):
        return self.__color, self.__letter, self.__width, self.__height

    def set_some_type_letter(self, witch, font: str='Arial', size: int=8, shape: str='bold'):
        self.__letter[witch] = (font, size, shape)

    def set_size_in_proportion(self, plus_or_less, width_or_height='both', geometry=''):
            print(geometry)

            how_much = self.__calculation_values[plus_or_less]
            self.__not_edit_key = ['title', 'opt', 'ent', 'bt_act', 'bt_oth']

            if self.__size_reference < -5:
                self.__size_reference = -5
            elif self.__size_reference > 10:
                self.__size_reference = 10

            self.__size_reference += how_much
            self._auto_letter_size_set()

            if width_or_height == 'width' or width_or_height == 'both':
                if  -5 < self.__size_reference < 10:

                    for i in self.__width:
                        if i not in self.__not_edit_key:
                            self.__width[i] += how_much

            if width_or_height == 'height' or width_or_height == 'both':
                if  -5 < self.__size_reference < 5:

                    for i in self.__height:
                        if i not in self.__not_edit_key:
                            self.__height[i] += how_much

    def _auto_letter_size_set(self):
        self.__not_edit_key = ['title', 'list']

        if self.__size_reference <= 0:
            self.__letter = letter

        if  0 <self.__size_reference > 5:
            for i in self.__letter:
                if i not in self.__not_edit_key:
                    self.__letter[i][1] = 9

        if 5 < self.__size_reference >= 10:
            for i in self.__letter:
                if i not in self.__not_edit_key:
                    self.__letter[i][1] = 10
