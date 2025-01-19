

colr = dict()
colr['purple'] = '#03030E'
colr['white'] = '#E5E4EA'
colr['grey'] = '#1F2021'
colr['white grey'] = '#494C51'

font = dict()
font['title'] = ('Arial', 10, 'bold')
font['search'] = ('Consolas', 14, 'bold')
font['Principal'] = ('Ariel', 9, 'bold')
font['list'] = ('Consolas', 8, 'bold')
font['foot'] = ('Consolas', 7, 'bold')

width = dict()
width['opt'] = 28
width['lis'] = 60
width['ent'] = 48
width['tex'] = 100
width['not'] = 100

height = dict()
height['lis'] = 20
height['tex'] = 20
height['not'] = 5


def set_size(witch, addition):
    if witch == 'width':
        for i in width:
            if i == 'ent':
                pass
            else:
                width[i] += addition

    elif witch == 'height':
        if addition >= 7:
            addition = 7
        for i in height:
            height[i] += addition


set_size('width', 17)
set_size('height', 7)
