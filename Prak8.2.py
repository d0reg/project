# Запрос ввода строки с завершающейся точкой
input_string = input("Введите строку, заканчивающуюся точкой: ")

# Удаляем точку с конца строки, если она есть
if input_string.endswith('.'):
    input_string = input_string[:-1]

# Разделение строки на слова
words = input_string.split()

# Подсчет количества слов
word_count = len(words)

# Вывод результата
print("Количество слов в строке:", word_count)
