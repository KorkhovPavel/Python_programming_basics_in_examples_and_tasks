#
# 07_step.png
#
# Входные данные:
#
# нет
# Выходные данные:
#
#  вектор-решение.
# Результат при выводе округлить до одного знака после запятой, используя функцию модуля numpy.
#
# Sample Input:
#
# Sample Output:
#
# [ 0.1 -0.1  0.2 -0.4]
import numpy as np
import numpy.linalg as alg

a = np.array([[-2, -8.5, -3.4, 3.5], [0, 2.4, 0, 8.2], [2.5, 1.6, 2.1, 3], [0.3, -0.4, -4.8, 4.6]])
b = np.array([-1.8, -3.28, -0.5, -2.83])
inv_a = alg.inv(a)
c = np.dot(inv_a, b)
print(np.round(c, 1))
