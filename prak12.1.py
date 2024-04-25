# Функция для вывода элементов строки в указанном направлении
def print_row(row, direction):
    if direction == "left_to_right":
        print(*row, end=" ")
    elif direction == "right_to_left":
        print(*reversed(row), end=" ")

# Функция для вывода матрицы в специфическом порядке
def print_matrix_in_pattern(matrix):
    for i, row in enumerate(matrix):
        # Определяем направление вывода элементов строки
        direction = "left_to_right" if i % 2 == 0 else "right_to_left"
        print_row(row, direction)
        print()  # Переход на новую строку после вывода элементов текущей строки

# Пример матрицы
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

# Вывод матрицы в специфическом порядке
print("Элементы матрицы в указанном порядке:")
print_matrix_in_pattern(matrix)
