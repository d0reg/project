import random

# Генерация списка из 20 случайных элементов
A = [random.randint(-10, 10) for _ in range(20)]

# Вывод списка A
print("Список A:", A)

# Подсчет количества отрицательных элементов
count_negative = sum(1 for x in A if x < 0)

print("Количество отрицательных элементов в списке A:", count_negative)
