# Дан треугольник ABC на плоскости, заданный координатами своих вершин. Для этого треугольника вычислить:
#
# радиус вписанной в треугольник окружности;
# радиус описанной вокруг треугольника окружности;
# сумму длин трех медиан треугольника.

# 13_step_task.png


# Пояснения к реализации
# Для решения использовать шаблон (скопировать код в соответствующее окно среды разработки,
# после комментариев вставить необходимые операторы).
# Результаты вычислений (радиус вписанной окружности, радиус описанной окружности, сумму длин медиан)
# вывести без сообщений пользователю, в одном операторе print, округлив значения до 4-х знаков после запятой.
# Если по заданным точкам построить треугольник нельзя, вывести "error".
# Входные данные:
#
# вещественное число (координата x точки А);
# вещественное число (координата y точки А);
# вещественное число (координата x точки B);
# вещественное число (координата y точки B);
# вещественное число (координата x точки C);
# вещественное число (координата y точки C).
# Выходные данные:
#
# радиус вписанной окружности, радиус описанной окружности и сумма длин медиан или error. Все значения
# округлить с указанной точностью, в операторе print никаких пояснений (текст в кавычках) не использовать.
# Sample Input 1:
#
# 0
# 0
# 1
# 1
# 2
# 2
# Sample Output 1:
#
# error
# Sample Input 2:
#
# -12.8
# 3.4
# -7.7
# 8.6
# -14.6
# -3.5
# Sample Output 2:
#
# 0.9113 14.0042 22.8319

# подключить модуль math или импортировать из него все нужные функции

import math

x_a = -12.8

y_a = 3.4

x_b = -7.7

y_b = 8.6

x_c = -14.6

y_c = -3.5


# реализовать решение задачи

def compute_len(x_0, y_0, x_1, y_1):
    len_line = math.sqrt((x_1 - x_0) ** 2 + (y_1 - y_0) ** 2)
    return len_line


def compute_area(a_1, a_2, a_3):
    p = (a_1 + a_2 + a_3) / 2
    area = math.sqrt(p * (p - a_1) * (p - a_2) * (p - a_3))
    return area


a = compute_len(x_a, y_a, x_b, y_b)
b = compute_len(x_b, y_b, x_c, y_c)
c = compute_len(x_c, y_c, x_a, y_a)

if a + b <= c or b + c <= a or a + c <= b:
    print("error")
else:
    p = a + b + c
    radius_of_a_circle_inscribed_in_a_triangle = math.sqrt((((p / 2) - a) * ((p / 2) - b) * ((p / 2) - c)) / (p / 2))
    s = compute_area(a, b, c)
    radius_of_a_circle_circumscribed_around_a_triangle = (a * b * c) / (4 * s)

    the_lengths_of_the_medians_of_the_triangle_a = (1 / 2) * math.sqrt(2 * (c ** 2 + b ** 2) - a ** 2)
    the_lengths_of_the_medians_of_the_triangle_b = (1 / 2) * math.sqrt(2 * (a ** 2 + c ** 2) - b ** 2)
    the_lengths_of_the_medians_of_the_triangle_c = (1 / 2) * math.sqrt(2 * (a ** 2 + b ** 2) - c ** 2)
    the_lengths_of_the_medians_of_the_triangle_sum_a_b_c = the_lengths_of_the_medians_of_the_triangle_c + the_lengths_of_the_medians_of_the_triangle_b + the_lengths_of_the_medians_of_the_triangle_a

    print(round(radius_of_a_circle_inscribed_in_a_triangle, 4),
          round(radius_of_a_circle_circumscribed_around_a_triangle, 4),
          round(the_lengths_of_the_medians_of_the_triangle_sum_a_b_c, 4))
    # вывести результаты
