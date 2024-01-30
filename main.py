from Grid import *
from animation import *

# Создание сетки
grid = Grid(5)
# 8 - вниз
# 2 - вверх
# 1 - вправо
# 4 - влево
grid.set_particles(1, 2, 8)
grid.set_particles(3, 2, 2)
grid.set_particles(0, 1, 1)
#grid.set_particles(2, 3, 4)
grid.set_particles(1, 4, 2)
grid.set_particles(4, 3, 8)
#grid.set_particles(3, 1, 1)

draw(grid)