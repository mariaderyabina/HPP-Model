import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from functools import partial
import copy

# Настройки для стрелок
arrows = { 1:(1,0), 4:(-1,0), 2:(0,1), 8:(0,-1)}
arrows_collision = {5:(1,4), 10:(2,8)}
arrows_comb = {3:(1,2), 6:(2,4), 9:(1,8), 12:(4,8), 7:(1,2,4), 11:(1,2,8), 13:(1,4,8), 14:(2,4,8), 15:(1,2,4,8)}
scale = 0.25


# Обновление сетки
def update(i, grid, N, is_anim, first_round):
    if is_anim and (i >= 1 or not first_round):
        grid.move()
    if first_round:
        first_round = False

    # Очистка графика
    plt.cla()
    plt.axis('off')
    
    for r, row in enumerate(grid.get_particles()):
        for c, cell in enumerate(row):

            if cell in arrows:
                plt.arrow(c+1, N-r-1+1, scale*arrows[cell][0], scale*arrows[cell][1], head_width=0.1, color='w')
            elif cell in arrows_comb:
                for arrw in arrows_comb[cell]:
                    plt.arrow(c+1, N-r-1+1, scale*arrows[arrw][0], scale*arrows[arrw][1], head_width=0.1, color='w')
            elif cell in arrows_collision:
                plt.scatter(c+1, N-r-1+1, s=150, c='r', marker='*')

    # Цифры на осях
    for i in range(N+2):
        for j in range(N+2):
            if i == 0 or j == 0 or i == N+1 or j == N+1:
                plt.plot(i, N+2-j-1, 'ko')
            if i == 0 and j != N+1 and j != 0:
                plt.text(i, N+2-j-1, str(j), color='w')
            if j == 0 and i != N+1 and i != 0:
                plt.text(i, N+2-j-1, str(i), color='w')
    
    # Нарисовать сетку
    for y in range(N+1):
        plt.plot([x+0.5 for x in range(N+1)], [y+0.5 for _ in range(N+1)], color='y')
    for x in range(N+1):
        plt.plot([x+0.5 for _ in range(N+1)], [y+0.5 for y in range(N+1)], color='y')


# Прорисовка графика
def draw(fig, grid, is_anim):
    plt.ioff() 
    new_grid = copy.deepcopy(grid) 
    anim = animation.FuncAnimation(fig, partial(update, grid=new_grid, N=new_grid.size, is_anim=is_anim, first_round=True), frames=100, interval=170)
    plt.show()


# Сохранение в гифку
def save_gif(fig, grid, is_anim):
    plt.ioff()
    new_grid = copy.deepcopy(grid)
    anim2 = animation.FuncAnimation(fig, partial(update, grid=new_grid, N=new_grid.size, is_anim=is_anim, first_round=True), frames=100, interval=170)
    writer = animation.PillowWriter(fps=2)
    anim2.save('hpp.gif', writer=writer)
    plt.cla()


# Создание фигуры
def input_particles():
    fig, ax = plt.subplots()
    fig.patch.set_facecolor('black')
    ax.set_facecolor("black")
    plt.ion()
    fig.show()
    return fig
