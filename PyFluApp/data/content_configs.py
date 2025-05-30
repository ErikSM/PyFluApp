
themes = dict()
colr = {'purple': '#03030E', 'white': '#E5E4EA', 'grey': '#1F2021',
        'white grey': '#494C51', 'yellow': '#928339', 'blue': '#2a4a6a'}

base_theme = [colr[i] for i in colr]

themes['Dark Purple'] = base_theme
themes['Light Yellow'] = base_theme[4], base_theme[0], base_theme[1], base_theme[4], base_theme[0]
themes['Medium Blue '] = base_theme[5], base_theme[1], base_theme[0], base_theme[3], base_theme[4]


letter = dict()
font_letter = 'Arial', 'Consolas', 'Impact'
font_mode = '', 'bold', 'italic', 'bold italic'
font_size = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10


letter['title'] = [font_letter[0], font_size[10], font_mode[3]]
letter['opt'] = [font_letter[1], font_size[10], font_mode[1]]
letter['list'] = [font_letter[1], font_size[7], font_mode[2]]
letter['search'] = [font_letter[1], font_size[8], font_mode[0]]
letter['screen'] = [font_letter[0], font_size[8], font_mode[1]]
letter['note'] = [font_letter[1], font_size[8], font_mode[1]]
letter['bt_act'] = [font_letter[2], font_size[8], font_mode[0]]
letter['bt_oth'] = [font_letter[0], font_size[8], font_mode[1]]


width = {'opt': 38, 'ent': 30,
         'lis': 53,  'tex': 85, 'not': 120,
         'bt_act': 7, 'bt_oth': 0}

height = {'lis': 12, 'tex': 11, 'not': 10,
          'bt_act': 0, 'bt_oth': 0}

main_geometry = ['932x518', '1171x631', '1494x765'], ['+188+47', '+187+23', '+2+2']
