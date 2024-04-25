def print_average_of_list(numbers):
    # Проверяем, пуст ли список
    if not numbers:
        print("0")  # Выводим ноль, если список пуст
        return

    # Вычисляем сумму всех элементов списка
    total = sum(numbers)

    # Вычисляем среднее значение
    average = total / len(numbers)

    # Выводим среднее значение
    print("Среднее значение элементов списка:", average)


# Функция для ввода списка с клавиатуры
def input_numbers():
    # Запрашиваем у пользователя ввод чисел через пробел и разбиваем строку на список чисел
    numbers_input = input("Введите числа через пробел: ").split()

    # Преобразуем каждый элемент списка из строкового представления в целое число
    numbers = [int(num) for num in numbers_input]

    # Возвращаем список чисел
    return numbers


# Основная функция
def main():
    # Ввод списка чисел с клавиатуры
    numbers = input_numbers()

    # Вывод среднего значения списка
    print_average_of_list(numbers)


# Вызов основной функции
main()
