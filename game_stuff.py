#!/usr/bin/python3

#####=====----- Variables -----=====#####

FIELD_ROWS = 10
FIELD_COLS = 10


#####=====----- Classes -----=====#####

class GameCell:
    ''' Объект одной клетки игрового поля с атрибутами координаты
    (coords), контента пусто/крестик/нолик (xo), весом для алгоритма
    выбора следующего хода (weight).
    '''
    def __init__(self):
        self.coords = (0, 0)
        self.xo = '.'
        self.weight = 0

class GameField:
    ''' Весь массив клеток игрового поля, состоящий из экземпляров
    класса GameCell()
    '''
    def __init__(self):
        self.cell_arr = [[GameCell() for col in range(FIELD_COLS)]
                                     for row in range(FIELD_ROWS)]
        for row_ in range(FIELD_ROWS):
            for col_ in range(FIELD_COLS):
                self.cell_arr[row_][col_].coords = (row_, col_)

#####=====----- THE END -----=====#########################################