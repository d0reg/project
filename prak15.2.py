def filter_even_numbers_above_10(numbers):
    # Создаем пустой список для хранения отфильтрованных чисел
    filtered_numbers = []

    # Проходим по каждому числу в исходном списке
    for num in numbers:
        # Проверяем, является ли число четным и больше 10
        if num % 2 == 0 and num > 10:
            # Если да, добавляем его в список отфильтрованных чисел
            filtered_numbers.append(num)

    # Возвращаем список отфильтрованных чисел
    return filtered_numbers


# Функция для ввода списка с клавиатуры
def input_numbers():
    # Запрашиваем у пользователя ввод чисел через пробел и разбиваем строку на список чисел
    numbers_input = input("Введите числа через пробел: ").split()

    # Преобразуем каждый элемент списка из строкового представления в целое число
    numbers = [int(num) for num in numbers_input]

    # Возвращаем список чисел
    return numbers


# Пример использования функции
def main():
    # Ввод списка чисел с клавиатуры
    numbers = input_numbers()

    # Фильтрация четных чисел больше 10
    filtered_numbers = filter_even_numbers_above_10(numbers)

    # Вывод отфильтрованного списка
    print("Отфильтрованный список четных чисел больше 10:", filtered_numbers)


# Вызов основной функции
main()
