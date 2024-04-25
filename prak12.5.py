import random

# Функция для вывода матрицы в общепринятом виде
def print_matrix(matrix):
    for row in matrix:
        print(*row)

# Функция для вычисления суммы отрицательных элементов над главной диагональю
def sum_negative_above_diagonal(matrix):
    size = len(matrix)
    total_sum = 0

    for i in range(size):
        for j in range(i):  # Подсчитываем элементы только над главной диагональю
            if matrix[i][j] < 0:
                total_sum += matrix[i][j]

    return total_sum

# Генерация случайной квадратной матрицы
N = 4  # Размер квадратной матрицы
matrix = [[random.randint(-10, 10) for _ in range(N)] for _ in range(N)]

# Вывод исходной матрицы
print("Исходная матрица:")
print_matrix(matrix)

# Вычисление и вывод суммы отрицательных элементов над главной диагональю
negative_sum = sum_negative_above_diagonal(matrix)
print("Сумма отрицательных элементов над главной диагональю:", negative_sum)
