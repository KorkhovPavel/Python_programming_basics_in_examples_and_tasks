# Задание
# Постройте графики следующих функций на интервале от -240o до 360o:
# 10_step.png
# На оси OX должны быть отмечены значения в ГРАДУСАХ.
#
# Пояснение.
#
# Для вычисления функций cos и sin значения x нужно перевести в радианы.
#
# По графику ответьте на вопросы.
from math import cos, sin, log1p, radians, exp
import matplotlib.pyplot as plt


# log1p - натуральный логарифм ln
# exp - e^x , пример: exp( sin(radians(x)) ) - это e^sin(X)

def func_1(x):
    res = exp(cos(radians(x))) + log1p(((sin(radians(x) * 0.8) ** 2) + 1)) * cos(radians(x))
    return res


def func_2(x):
    res = -log1p((cos(radians(x)) + sin(radians(x))) ** 2 + 1.7) + 2
    return res


func_1_x = []
func_1_y = []
func_2_x = []
func_2_y = []

for i in range(-240, 360):
    func_1_x.append(i)
    func_1_y.append(func_1(i))
    func_2_x.append(i)
    func_2_y.append(func_2(i))

line_f = plt.plot(func_1_x, func_1_y, label='f(x)')
line_y = plt.plot(func_2_x, func_2_y, label='y(x)')

plt.setp(line_f, color="blue", linewidth=2)
plt.setp(line_y, color="red", linewidth=2)

plt.legend()
plt.title("Графики функций")

plt.show()
