from Grid import *
from animation import *
import random

err_flg = 0
# Словарь для направлений частиц
directions = {'u': 2, 'd': 8, 'r': 1, 'l': 4}

# Ввод сетки с консоли
# Размер сетки
N = int(input("Введите длину стороны сетки: "))

# Создание сетки
grid = Grid(N)

# рисуем пустую сетку для ввода
fig = input_particles()
update(0, grid, grid.size, is_anim=False, first_round=True)

# Выбор пользователя - задать частицы рандомно или ввести вручную
print()
print("Задать начальное расположение частиц рандомно или вручную?")
start_position = input("Введите random/manually: ")

# Ввод начального расположения частиц
if start_position == 'random' or start_position == 'r':
    qty = int(input(f"Введите количество частиц\nДля моделирования газа - от 1 до {N}. Для моделирования жидкости - от {N} до {N}^2: "))
    for i in range(qty): 
        grid.set_particles(random.randint(0, N-1), random.randint(0, N-1), random.choice([1, 2, 4, 8]))
        update(0, grid, grid.size, is_anim=False, first_round=True)
elif start_position == 'manually' or start_position == 'm':
    print()
    print("Вводите координаты и направление частицы через пробел")
    print(f"Координатами могут быть целые числа от 1 до {N}")
    print("Направления частиц задаются словами: u (вверх), d (вниз), r (вправо), l (влево)")
    print("В одной клетке может быть от 1 до 4 частиц (по одной на каждое направление)")
    print("Пример ввода: 1 4 u")
    print('Для завершения ввода введите "-1"')

    inputting = True
    while(inputting):
        user_input = input()
        if user_input == "-1":
            inputting = False
        else:
            i, j, direction = user_input.split()
            i = int(i) - 1
            j = int(j) - 1
            try:
                direction = directions[direction]
            except KeyError:
                print('Некорректное направление частицы')
                continue
            grid.set_particles(i, j, direction)

            update(0, grid, grid.size, is_anim=False, first_round=True)
else:
    err_flg = 1

if not err_flg:
    # Сохранение в гифку
    save_gif(fig, grid, is_anim=True)
    # Прорисовка
    draw(fig, grid, is_anim=True)
