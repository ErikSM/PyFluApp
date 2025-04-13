colr = dict()
colr['purple'] = '#03030E'
colr['white'] = '#E5E4EA'
colr['grey'] = '#1F2021'
colr['white grey'] = '#494C51'

letter = dict()
letter['title'] = ('Arial', 10, 'bold')
letter['search'] = ('Consolas', 14, 'bold')
letter['principal'] = ('Ariel', 9, 'bold')
letter['list'] = ('Consolas', 8, 'bold')
letter['foot'] = ('Consolas', 7, 'bold')
letter['but_act'] = ('Impact', 10)
letter['but_other'] = ('Arial', 11, 'bold')


def set_some_type_letter(witch, font: str = 'Arial', size: int = 9, shape: str = 'bold'):
    letter[witch] = (font, size, shape)


width = dict()
width['opt'] = 28
width['lis'] = 60
width['ent'] = 33
width['tex'] = 100
width['not'] = 130
width['but_act'] = 6
width['but_oth'] = 0

height = dict()
height['lis'] = 15
height['tex'] = 15
height['not'] = 10
height['but_act'] = 0
height['but_oth'] = 0

def set_size_in_proportion(width_or_height, how_much):
    approved = False
    not_edit = 'opt', 'ent', 'but_act', 'but_oth'

    if -30 <= how_much <= 20:
        approved = True

    if approved:
        if width_or_height == 'width':
            for i in width:
                if i in not_edit:
                    pass
                else:
                    width[i] += how_much

        elif width_or_height == 'height':
            if -10 <= how_much >= 7:
                how_much = 7
            for i in height:
                if i in not_edit:
                    pass
                else:
                    height[i] += how_much

    else:
        pass

set_size_in_proportion('width', 10)
set_size_in_proportion('height', 4)
