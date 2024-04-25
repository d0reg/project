def count_spaces_and_check_evenness(input_string):
    # Подсчитываем количество пробелов в строке
    space_count = input_string.count(' ')

    # Проверяем, является ли количество пробелов четным
    if space_count % 2 == 0:
        print("Четное число")
    else:
        print("Нечетное число")


# Функция для ввода строки с клавиатуры
def input_string():
    # Запрашиваем у пользователя ввод строки
    user_input = input("Введите строку: ")
    return user_input


# Основная функция
def main():
    # Ввод строки с клавиатуры
    user_string = input_string()

    # Подсчет пробелов и проверка четности их количества
    count_spaces_and_check_evenness(user_string)


# Вызов основной функции
main()
