import random

# Функция для вывода матрицы в общепринятом виде
def print_matrix(matrix):
    for row in matrix:
        print(*row)

# Функция для вычисления суммы элементов каждой строки матрицы
def row_sums(matrix):
    sums = []  # Создаем список для хранения сумм каждой строки

    for row in matrix:
        row_sum = sum(row)  # Вычисляем сумму элементов текущей строки
        sums.append(row_sum)  # Добавляем сумму в список

    return sums

# Генерация случайной матрицы
M = 3  # Количество строк
N = 4  # Количество столбцов
matrix = [[random.randint(1, 10) for _ in range(N)] for _ in range(M)]

# Вывод исходной матрицы
print("Исходная матрица:")
print_matrix(matrix)

# Вычисление и вывод суммы элементов каждой строки
row_sums_result = row_sums(matrix)
print("Суммы элементов каждой строки:", row_sums_result)
