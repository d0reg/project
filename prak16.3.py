def print_even_numbers(numbers):
    # Итерируемся по элементам списка
    for num in numbers:
        # Проверяем, является ли число четным
        if num % 2 == 0:
            # Выводим четное число
            print(num)

# Произвольный список чисел
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Вызов функции для печати четных чисел из списка
print_even_numbers(numbers)
