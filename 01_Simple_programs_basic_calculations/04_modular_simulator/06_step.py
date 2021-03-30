# Задача
# Дано значение времени в 12-ти часовом формате h:m:s. Определить угол в градусах между
# положением часовой стрелки в начале суток и ее положением в h часов, m минут и s секунд.
#
# Допустимыми значениями считать целое число часов от 0 до 11, минут и секунд от 0 до 59.
# Если введены другие значения - вывести "error".
#
# Входные данные:
#
# количество часов h (целое число);
# количество минут m (целое число);
# количество секунд s (целое число).
# Выходные данные:
#
# значение угла в градусах или error.
# Результат округлить до двух знаков после запятой.
#
# Sample Input 1:
#
# 12
# 1
# 1
# Sample Output 1:
#
# error
# Sample Input 2:
#
# 6
# 47
# 19
# Sample Output 2:
#
# 203.66


hour = int(input())
minute = int(input())
second = int(input())

if hour in range(0, 12) and minute in range(0, 59) and second in range(0, 59):
    hour_grad = hour * (360 / 12)
    minute_grad = minute * (30 / 60)
    second_grad = second * (0.5 / 60)
    res = hour_grad + minute_grad + second_grad
    print(round(res, 2))
else:
    print('error')
