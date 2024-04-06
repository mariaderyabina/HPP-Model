# HPP Model - модель решеточного газа

## Описание модели
В основе модели квадратная решетка, в клетках которой могут обитать частицы единичной массы. Каждая из частиц может иметь скорость, направленную в одну из соседних клеток, такой величины, что за один шаг по времени частицы могут перелететь как раз в соседнюю клетку. В клетке может быть не более одной частицы с данным направлением скорости. Такая схема называется моделю HPP по первым буквам фамилий ее авторов.

Эволюция частиц за каждый шаг по времени происходит в два этапа.

- На первом частицы перелетают в соседние клетки в соответствии со своими скоростями. 

- На втором происходят соударения частиц в клетках. При столкновениях должно сохраняться количество частиц и их полный импульс. При этом нетривиальными столкновениями в модели HPP являются только соударения "почти лоб в лоб", после которых скорости частиц поворачиваются на 90◦. Во всех остальных случаях можно считать, что столкновения не произошло (частицы пролетели мимо друг друга). То есть, частицы меняют направление при столкновении с частицей противоположной скорости (были частицы вверх и вниз, становятся вправо и влево и наоборот).

## Кодирование скоростей частиц
Наличие частицы, имеющей скорость по каждому направлению, закодировано одним битом (0 - нет частицы, 1 - есть). 
Так можно записать состояние каждой клетки в четырех битах. Всего различных состояний в клетке может быть 16, включая 0 (нет ни одной частицы). Все операции сводятся к целочисленной арифметике, что означает высокую скорость расчетов и отсутствие ошибок округления.

Возможные состояния клетки:

- 0000<sub>2</sub> = 0 - нет частиц
- 0001<sub>2</sub> = 1 - есть частица со скоростью "вправо"
- 0010<sub>2</sub> = 2 - есть частица со скоростью "вверх"
- 0100<sub>2</sub> = 4 - есть частица со скоростью "влево"
- 1000<sub>2</sub> = 8 - есть частица со скоростью "вниз"
- 0011<sub>2</sub> = 3 - есть частица со скоростью "вправо" и частица со скоростью "вверх"
- и т.д. до состояния 1111<sub>2</sub> - в клетке есть частицы со всеми скоростями

Если в клетке уже есть частица, то добавление второй частицы происходит с помощью операции ИЛИ.\
Например, в клетке находится частица со скоростью "вверх":\
S = 0010<sub>2</sub>\
Тогда добавление к этой клетке частицы со скоростью "влево" произойдет так:\
S1 = S | 0100<sub>2</sub> = 0110<sub>2</sub> 
Таким образом, в состоянии S1 находятся две частицы со скоростями "вверх" и "влево".\
Точно так же при проиходит добавление третьей и четвертой частицы.

Провека наличия частицы данной скорости в клетке осуществляется операцией И.
Например, состояние клетки такое: 
S = 1011<sub>2</sub>\
Тогда проверка, есть ли в клетке частица со скоростью "вниз", будет такой:\
S & 1000<sub>2</sub> = 1000<sub>2</sub>\
Если результат проверки не равен 0, то такая частица есть в клетке.

## Взаимодействие с программой
Для запуска понадобятся: интерпретатор python, библиотеки numpy и matplotlib
1. В консоли перейти в директорию с проектом, выпонить команду "python main\.py". Далее появятся подсказки по вводу.
2. Ввести размер решетки.
3. Есть два режима начального положения частиц: ручной ввод или автоматическое рандомное заполнение. 
    - При ручном вводе нужно поочередно вводить координаты и скорости частиц. Ввод интерактивный, частицы будут сразу же появляться на графике.
    - При рандомном заполнении нужно выбрать количество частиц, это задает плотность моделируемого вещества.
4. Анимация движения частиц автоматически появится на графике, также в текущую директорию сохранится гифка "hpp.gif". Направления частиц изображаются стрелками, а столкновения - красной звездочкой. 