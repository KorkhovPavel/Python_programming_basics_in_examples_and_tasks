# Задание
# Результаты сравнения экспериментального и вычисленного значения теплопроводности показывают, что
# наибольшая погрешность наблюдается для первой (200 К) и двух последних (1500оК и 1600оК) температур.
# Используя предыдущую задачу, вычислите максимальную и среднюю погрешность для интервала температур от 300оК до 1400оК.
#
# Пояснение. Для того, чтобы выделить из списка его часть используются  "срезы". Например, чтобы выделить
# из списка значения  с индексами от 2 до 4 (включительно) и сформировать новый список, используется запись:
#
# x_list = [2, 4, -5, 1, 8, -3, 7]
#
# y_list = x_list[2:5] # будет занесено [-5, 1, 8]
# Все результаты занести, округлив их до двух знаков после запятой.

def compute_lambda(t):
    b = 33
    l_0 = 884
    t_0 = 100
    y = b * l_0 / (t - t_0)
    return y


f = open("lambda_exp.txt", "r")

t_list = []
lambda_exp_list = []

for line in f:
    t_lambda_list = line.split()
    t_list.append(float(t_lambda_list[0]))
    lambda_exp_list.append(float(t_lambda_list[1]))

f.close()
lambda_list = [compute_lambda(t) for t in t_list]
error_list = [abs((lambda_exp_list[i] - lambda_list[i]) / lambda_exp_list[i])
              for i in range(len(t_list))]

print("-" * 40)

print("|%7s | %7s | %7s |%8s |" % ("t", "l(t)", "exp(t)", "error"))

print("-" * 40)

for i in range(len(t_list)):
    print("|%7d | %7.3f | %7.1f |%7.2f%% |"
          % (t_list[i], lambda_list[i], lambda_exp_list[i], error_list[i] * 100))

print("-" * 40)
max_error = max(error_list)
index_max_error = error_list.index(max_error)

print("Максимальная погрешность = %5.2f%%  при t = %5d"
      % (max_error * 100, t_list[index_max_error]))

min_error = min(error_list)

index_min_error = error_list.index(min_error)

print("Минимальная погрешность = %5.2f%%  при t = %5d"
      % (min_error * 100, t_list[index_min_error]))

avg_error = sum(error_list) / len(t_list)

print("Средняя погрешность = %5.2f%%" % (avg_error * 100))