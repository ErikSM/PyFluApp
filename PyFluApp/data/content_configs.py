import random


colr = dict()
colr['purple'] = '#03030E'
colr['white'] = '#E5E4EA'
colr['grey'] = '#1F2021'
colr['white grey'] = '#494C51'
colr['yellow'] = '#928339'

tema_base = [colr[i] for i in colr]

themes = dict()
themes['tema 1'] = tema_base
themes['tema 2'] = tema_base[1], tema_base[0], tema_base[3], tema_base[4], tema_base[2]
themes['tema 3'] = tema_base[2], tema_base[1], tema_base[0], tema_base[3], tema_base[4]
print(themes)



letter = dict()
letter['title'] = ['Arial', 10, 'bold']
letter['opt'] = ['Consolas', 9, 'bold']
letter['list'] = ['Consolas', 8, 'bold']
letter['search'] = ['Consolas', 9, 'bold']
letter['screen'] = ['Ariel', 8, 'bold']
letter['note'] = ['Consolas', 8, 'bold']
letter['bt_act'] = ['Impact', 9, '']
letter['bt_oth'] = ['Arial', 10, 'bold']


width = dict()
width['opt'] = 28
width['lis'] = 65
width['ent'] = 33
width['tex'] = 110
width['not'] = 140
width['bt_act'] = 7
width['bt_oth'] = 0


height = dict()
height['lis'] = 11
height['tex'] = 12
height['not'] = 10
height['bt_act'] = 0
height['bt_oth'] = 0
