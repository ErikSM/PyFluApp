from data.content_configs import colr, letter, width, height


class Config:

    def __init__(self):

        self.__color = colr
        self.__letter = letter
        self.__width = width
        self.__height = height

        self.__size_reference = 0
        self.__not_edit_key = None

    def __getitem__(self, item):
        items = self.__color, self.__letter, self.__width, self.__height
        return items[int(item)]

    def get_all(self):
        return self.__color, self.__letter, self.__width, self.__height

    def set_some_type_letter(self, witch, font: str='Arial', size: int=8, shape: str='bold'):
        self.__letter[witch] = (font, size, shape)


    def set_size_in_proportion(self, width_or_height, how_much, geometry):
        print(geometry)

        self.__not_edit_key = ['title', 'opt', 'ent', 'bt_act', 'bt_oth']

        if self.__size_reference < -4:
            approved = False
            self.__size_reference = -4


        elif self.__size_reference > 14:
            approved = False
            self.__size_reference = 14

        else:
            approved = True
            self.__size_reference += how_much
            self._auto_letter_size_set()

        if approved:

            if width_or_height == 'width' or width_or_height == 'both':

                if  -4 < self.__size_reference < 14:

                    for i in self.__width:
                        if i in self.__not_edit_key:
                            pass
                        else:
                            self.__width[i] += how_much



            if width_or_height == 'height' or width_or_height == 'both':
                if  -4 < self.__size_reference < 6:

                    for i in self.__height:
                        if i in self.__not_edit_key:
                            pass
                        else:
                            self.__height[i] += how_much



    # in progress
    def _auto_letter_size_set(self):
        self.__not_edit_key = ['title', 'list']


        if self.__size_reference <= 2:
            self.__letter = letter

        if  2 <self.__size_reference > 3:
            for i in self.__letter:
                if i not in self.__not_edit_key:
                    self.__letter[i][1] = 9

        if 3 < self.__size_reference > 8:
            for i in self.__letter:
                if i not in self.__not_edit_key:
                    self.__letter[i][1] = 10

