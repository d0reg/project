# Ввод строки
input_string = input("Введите строку: ")

# Создание словаря для подсчета встречаемости символов
char_count = {}

# Подсчет количества символов
for char in input_string:
    # Игнорирование пробелов
    if char != ' ':
        # Преобразование символов в нижний регистр для учета регистронезависимости
        char = char.lower()
        char_count[char] = char_count.get(char, 0) + 1

# Нахождение максимального значения
max_count = max(char_count.values())

# Вывод максимального количества раз, которое встречается какой-либо символ
print("Максимальное количество раз, которое встречается какой-либо символ:", max_count)
