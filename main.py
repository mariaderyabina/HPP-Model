from Grid import *
from animation import *

# Словарь для направлений частиц
directions = {'вверх': 2, 'вниз': 8, 'вправо': 1, 'влево': 4}

# Ввод сетки с консоли
# Размер сетки
N = int(input("Введите длину стороны сетки: "))

# Создание сетки
grid = Grid(N)

# Ввод координат и направлений частиц
print()
print("Вводите координаты и направление частицы через пробел")
print(f"Координатами могут быть целые числа от 1 до {N}")
print("Направления частиц задаются словами: вверх, вниз, вправо, влево")
print("В одной клетке может быть от 1 до 4 частиц (по одной на каждое направление)")
print("Пример ввода: 1 4 вверх")
print('Для завершения ввода введите "-1"')


# рисуем пустую сетку для ввода
fig = input_particles()
update(0, grid, grid.size, is_anim=False, first_round=True)

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


# Сохранение в гифку
save_gif(fig, grid, is_anim=True)
# Прорисовка
draw(fig, grid, is_anim=True)
