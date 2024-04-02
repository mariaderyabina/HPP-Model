# Это класс для объектов сетки
import numpy as np

class Grid:

    # Направления скоростей частиц
    global r_speed
    global u_speed
    global l_speed
    global d_speed

    r_speed = 1
    u_speed = 2
    l_speed = 4
    d_speed = 8    


    # Создание сетки
    def __init__(self, N):
        self.size = N
        self.grid = np.zeros((N, N), int)

    # Ввести координаты и направление частицы
    def set_particles(self, i, j, direction):
        self.grid[i][j] |= direction

    # Вернуть матрицу с координатами и направлениями частиц
    def get_particles(self):
        return self.grid

    # Функции для передвижения частиц
    def right(self, i, j, grid):
        if(j==self.size-1):
            grid[i][0] |= r_speed
        else:
            grid[i][j+1] |= r_speed

    def up(self, i, j, grid):
        if(i==0):
            grid[self.size-1][j] |= u_speed
        else:
            grid[i-1][j] |= u_speed 

    def left(self, i, j, grid):
        if(j==0):
            grid[i][self.size-1] |= l_speed
        else:
            grid[i][j-1] |= l_speed

    def down(self, i, j, grid):
        if(i==self.size-1):
            grid[0][j] |= d_speed
        else:
            grid[i+1][j] |= d_speed


    def move(self):
        newgrid = np.zeros((self.size, self.size), int)
        for i, row in enumerate(self.grid):
            for j, val in enumerate(row):
                # Проверка наличия частиц в ячейке
                r = val & r_speed
                u = val & u_speed
                l = val & l_speed
                d = val & d_speed

                # 1 этап - обработка коллизий - обрабатываются случаи, когда в ячейке 2 частицы с противоположными скоростями
                # у таких частиц направления скоростей меняются на 90 градусов
                if r and l and not(u or d):
                    r, l = 0, 0
                    u, d = u_speed, d_speed
                elif u and d and not(r or l):
                    u, d = 0, 0
                    r, l = r_speed, l_speed

                # 2 этап - распространение
                # двигаем частицы
                if r:
                    self.right(i, j, newgrid)
                if u:
                    self.up(i, j, newgrid)
                if l:
                    self.left(i, j, newgrid)
                if d:
                    self.down(i, j, newgrid)

        self.grid = newgrid
        return self             
