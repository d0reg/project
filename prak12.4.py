import random

# Функция для вывода матрицы в общепринятом виде
def print_matrix(matrix):
    for row in matrix:
        print(*row)

# Функция для вычисления суммы положительных элементов под главной диагональю и на ней
def sum_positive_below_diagonal(matrix):
    size = len(matrix)
    total_sum = 0

    for i in range(size):
        for j in range(i + 1):  # Подсчитываем элементы только под главной диагональю и на ней
            if matrix[i][j] > 0:
                total_sum += matrix[i][j]

    return total_sum

# Генерация случайной квадратной матрицы
N = 4  # Размер квадратной матрицы
matrix = [[random.randint(-10, 10) for _ in range(N)] for _ in range(N)]

# Вывод исходной матрицы
print("Исходная матрица:")
print_matrix(matrix)

# Вычисление и вывод суммы положительных элементов под главной диагональю и на ней
positive_sum = sum_positive_below_diagonal(matrix)
print("Сумма положительных элементов под главной диагональю и на ней:", positive_sum)
