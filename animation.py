import numpy as np
import matplotlib.pyplot as plt
# анимация
from matplotlib.animation import FuncAnimation
from functools import partial

# Настройки для стрелок
arrows = { 1:(1,0), 4:(-1,0), 2:(0,1), 8:(0,-1)}
arrows_collision = {5:(1,4), 10:(2,8)}
arrows_comb = {3:(1,2), 6:(2,4), 9:(1,8), 12:(4,8), 7:(1,2,4), 11:(1,2,8), 13:(1,4,8), 14:(2,4,8), 15:(1,2,4,8)}
scale = 0.25


# Обновление сетки
def update(i, grid, N):
    if i == 0:
        global gridv
        gridv = grid
    gridv = gridv.move()

    # очищаем график
    plt.cla()
    plt.axis('off')
    
    for r, row in enumerate(gridv.get_particles()):
        for c, cell in enumerate(row):

            if cell in arrows:
                plt.arrow(c+1, N-r-1+1, scale*arrows[cell][0], scale*arrows[cell][1], head_width=0.1)
            elif cell in arrows_comb:
                for arrw in arrows_comb[cell]:
                    plt.arrow(c+1, N-r-1+1, scale*arrows[arrw][0], scale*arrows[arrw][1], head_width=0.1)
            elif cell in arrows_collision:
                plt.plot(c+1, N-r-1+1, 'r*')
            # else:
            #     # если нет частицы, ставим точку
            #     plt.plot(c+1, N-r-1+1, 'ro')

    # ставим точки по краям, чтобы оси не двигались от стрелок
    # изменить этот алгоритм, n^2 это плохо
    for i in range(N+2):
        for j in range(N+2):
            if i == 0 or j == 0 or i == N+1 or j == N+1:
                plt.plot(i, N+2-j-1, 'wo')
    
    # Нарисовать сетку
    for y in range(N+1):
        plt.plot([x+0.5 for x in range(N+1)], [y+0.5 for _ in range(N+1)], color='k')
    for x in range(N+1):
        plt.plot([x+0.5 for _ in range(N+1)], [y+0.5 for y in range(N+1)], color='k')


# Прорисовка графика
def draw(grid):
    fig, ax = plt.subplots()
    anim = FuncAnimation(fig, partial(update, grid=grid, N=grid.size), frames=20, interval=500)
    plt.show()
