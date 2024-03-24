# Это класс для объектов сетки
import numpy as np

class Grid:

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
            grid[i][0] |= 1
        else:
            grid[i][j+1] |= 1

    def up(self, i, j, grid):
        if(i==0):
            grid[self.size-1][j] |= 2
        else:
            grid[i-1][j] |= 2 

    def left(self, i, j, grid):
        if(j==0):
            grid[i][self.size-1] |= 4
        else:
            grid[i][j-1] |= 4

    def down(self, i, j, grid):
        if(i==self.size-1):
            grid[0][j] |= 8
        else:
            grid[i+1][j] |= 8


    def move(self):
        newgrid = np.zeros((self.size, self.size), int)
        for i, row in enumerate(self.grid):
            for j, val in enumerate(row):
                if(val==1):
                    self.right(i, j, newgrid)
                elif(val==2):
                    self.up(i, j, newgrid)
                elif(val==4):
                    self.left(i, j, newgrid)
                elif(val==8):
                    self.down(i, j, newgrid)
                elif(val==3):
                    self.up(i, j, newgrid)
                    self.right(i, j, newgrid)
                elif(val==9):
                    self.right(i, j, newgrid)
                    self.down(i, j, newgrid)
                elif(val==6):
                    self.left(i, j, newgrid)
                    self.up(i, j, newgrid)
                elif(val==12):
                    self.left(i, j, newgrid)
                    self.down(i, j, newgrid)
                elif(val==5):
                    self.up(i, j, newgrid)
                    self.down(i, j, newgrid)
                elif(val==10):
                    self.left(i, j, newgrid)
                    self.right(i, j, newgrid)
                elif(val==7):
                    self.left(i, j, newgrid)
                    self.up(i, j, newgrid)
                    self.right(i, j, newgrid)
                elif(val==11):
                    self.up(i, j, newgrid)
                    self.down(i, j, newgrid)
                    self.right(i, j, newgrid)
                elif(val==13):
                    self.down(i, j, newgrid)
                    self.left(i, j, newgrid)
                    self.right(i, j, newgrid)
                elif(val==14):
                    self.left(i, j, newgrid)
                    self.up(i, j, newgrid)
                    self.down(i, j, newgrid)
                elif(val==15):
                    self.right(i, j, newgrid)
                    self.up(i, j, newgrid)
                    self.left(i, j, newgrid)
                    self.down(i, j, newgrid)
        self.grid = newgrid
        return self             
