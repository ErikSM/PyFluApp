
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

letter['title'] = [font_letter[0], 10, font_mode[3]]
letter['opt'] = [font_letter[1], 10, font_mode[1]]
letter['list'] = [font_letter[1], 7, font_mode[2]]
letter['search'] = [font_letter[1], 8, font_mode[0]]
letter['screen'] = [font_letter[0], 8, font_mode[1]]
letter['note'] = [font_letter[1], 8, font_mode[1]]
letter['bt_act'] = [font_letter[2], 8, font_mode[0]]
letter['bt_oth'] = [font_letter[0], 8, font_mode[1]]


width = {'opt': 38, 'ent': 80,
         'lis': 53,  'tex': 85, 'not': 120,
         'bt_act': 7, 'bt_oth': 0}

height = {'lis': 12, 'tex': 11, 'not': 10,
          'bt_act': 0, 'bt_oth': 0}
