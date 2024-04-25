import random

# Функция для вывода матрицы в общепринятом виде
def print_matrix(matrix):
    for row in matrix:
        print(*row)

# Функция для вычисления суммы элементов каждого столбца матрицы
def column_sums(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    sums = [0] * num_cols  # Создаем список для хранения сумм каждого столбца, инициализируем нулями

    for row in matrix:
        for j in range(num_cols):
            sums[j] += row[j]  # Добавляем элемент в j-том столбце к сумме этого столбца

    return sums

# Генерация случайной матрицы
M = 3  # Количество строк
N = 4  # Количество столбцов
matrix = [[random.randint(1, 10) for _ in range(N)] for _ in range(M)]

# Вывод исходной матрицы
print("Исходная матрица:")
print_matrix(matrix)

# Вычисление и вывод суммы элементов каждого столбца
column_sums_result = column_sums(matrix)
print("Суммы элементов каждого столбца:", column_sums_result)
