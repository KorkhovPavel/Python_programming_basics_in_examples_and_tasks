# Задача
# Измерили дальности полета воды, выпущенной из шланга, под разными углами к горизонту. По этим данным построить
# тренд (полином второй степени) зависимости дальности полета от угла наклона шланга и найти дальность полета
# струи воды для произвольного угла.
#
# Входные данные:
#
# строка из целых чисел, разделенных пробелами, каждое значение - угол наклона шланга в градусах;
# строка из вещественных чисел, разделенных пробелами, каждое значение - дальность полета воды в метрах;
# угол наклона, для которого необходимо вычислить дальность (вещественное число).
# Выходные данные:
#
# дальность полета струи воды.
# Для вывода результатов использовать формат:
#
# "Дальность: %6.2f м"
#
# Sample Input:
#
# 27 34 41 48 55 62 69 76 83 90 97
# 75.23 95.49 98.03 89.5 84.57 82.07 69.58 48.82 26.36 0.0 -26.12
# 34
# Sample Output:
#
# Дальность:  89.19 м
import numpy as np

angles_of_inclination_list = input().split()
range_of_water_flight_list = input().split()
angles = int(input())
angles_of_inclination_arr = np.array(angles_of_inclination_list, float)
range_of_water_flight_arr = np.array(range_of_water_flight_list, float)
a = np.polyfit(angles_of_inclination_arr, range_of_water_flight_arr, 2)


def get_trend(x, a):
    y = a[0] * x ** 2 + a[1] * x + a[2]
    return y


x_target = angles

h_target = get_trend(x_target, a)

print(f'Дальность: {h_target:6.2f} м')
