from data.content_configs import colr, letter, width, height


class Config:

    def __init__(self):

        self.__color = colr
        self.__letter = letter
        self.__width = width
        self.__height = height

        self.__size_reference = 0
        self.all = self.__color, self.__letter, self.__width, self.__height

    def __getitem__(self, item):
        return self.all[item]

    def get_all(self):
        return self.all

    def set_some_type_letter(self, witch, font: str='Arial', size: int=8, shape: str='bold'):
        self.__letter[witch] = (font, size, shape)


    def set_size_in_proportion(self, width_or_height, how_much):
        approved = True
        not_edit = 'opt', 'ent', 'bt_act', 'bt_oth'

        if self.__size_reference < -2:
            approved = False
            self.__size_reference = -2

        elif self.__size_reference > 10:
            approved = False
            self.__size_reference = 10

        else:
            approved = True


        if approved:
            self.__size_reference += how_much

            if width_or_height == 'width' or width_or_height == 'both':
                if not -2 <= self.__size_reference <= 10:
                    pass

                else:
                    for i in self.__width:
                        if i in not_edit:
                            pass
                        else:
                            self.__width[i] += how_much


            if width_or_height == 'height' or width_or_height == 'both':
                if not -2 <= self.__size_reference <= 6:
                    pass

                else:
                    for i in self.__height:
                        if i in not_edit:
                            pass
                        else:
                            self.__height[i] += how_much

        return self.__width, self.__height
