def main():
    # Инициализация переменной для хранения суммы кубов
    sum_of_cubes = 0

    # Итерируемся по всем трехзначным числам
    for num in range(100, 1000):
        # Проверяем, делится ли число на 8 без остатка
        if num % 8 == 0:
            # Если условие выполняется, добавляем куб числа к общей сумме
            sum_of_cubes += num ** 3

    # Выводим общую сумму кубов
    print("Сумма кубов всех трехзначных чисел, делящихся на 8:", sum_of_cubes)


# Вызов основной функции
main()
