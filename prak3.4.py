# Ввод данных
a = float(input("Введите число a: "))
b = float(input("Введите число b: "))
c = float(input("Введите число c: "))

# Подсчет количества положительных чисел
count_positive = 0
if a > 0:
    count_positive += 1
if b > 0:
    count_positive += 1
if c > 0:
    count_positive += 1

# Вывод результатов
print("Количество положительных чисел среди a, b, c:", count_positive)