# Дан многоугольник на плоскости, заданный  координатами своих вершин. Найти координаты вершин многоугольника,
# полученные поворотом каждой точки  на заданный угол вокруг начала координат. Вычислить средние значения
# координат по оси ОХ и ОУ повернутого многоугольника.
# 13_step.png
# Входные данные:
#
#  количество вершин многоугольника (целое число);
# список вершин многоугольника, каждая вершина на отдельной строке, строка состоит из двух чисел через пробел,
# определяющие координаты вершины по оси ОХ и OY (целые числа);
# угол поворота в градусах (целое число).
# Выходные данные:
#
# среднее значение абсцисс (координат x) и ординат(координат y) точек повернутого многоугольника, для вывода
# использовать шаблон:
# "avg_x = %6.2f, avg_y = %6.2f"
#
# Пояснение:
#
# Создать двухмерный массив из вершин многоугольника (количество строк - количество вершин, количество
# столбцов  2, для координат x и у точки).
# Составить матрицу поворота вокруг центра координат (\phiϕ - значение угла поворота в радианах):
# 13_step_1.png
# Умножить массив вершин на матрицу поворота. Полученная матрица - координаты вершин многоугольника после поворота.
# Найти среднее значение первого столбца (avg_x) и среднее значение второго (avg_y).
# Sample Input:
#
# 3
# -7 -8
# -11 4
# -9 5
# 45
# Sample Output:
#
# avg_x =  -6.60, avg_y =  -6.13
import math

import numpy as np

number_of_vertices = int(input())
list_vertices = []
for i in range(number_of_vertices):
    list_vertices.append([int(item) for item in input().split()])

angle_of_rotation = int(input())
angle_of_rotation_rad = math.radians(angle_of_rotation)

rotate = [[math.cos(angle_of_rotation_rad), math.sin(angle_of_rotation_rad)], [-math.sin(angle_of_rotation_rad),
                                                                               math.cos(angle_of_rotation_rad)]]

list_vertices_array = np.array(list_vertices)
rotate_array = np.array(rotate)
coordinates_of_vertices_after_rotation = np.dot(list_vertices_array, rotate_array)
avg_all = np.mean(coordinates_of_vertices_after_rotation, 0)
print(f"avg_x = {avg_all[0]:6.2f}, avg_y = {avg_all[1]:6.2f}")
