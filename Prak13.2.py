# Функция для преобразования слова в верхний регистр с добавлением дефисов
def capitalize_with_hyphens(word):
    # Преобразование слова в верхний регистр и добавление дефисов
    capitalized_word = '-'.join(list(word.upper()))
    return capitalized_word

# Ввод строки с несколькими словами
input_string = input("Введите строку с несколькими словами: ")

# Разделение строки на отдельные слова
words_list = input_string.split()

# Список для хранения преобразованных слов
capitalized_words_list = []

# Преобразование каждого слова и добавление его в список
for word in words_list:
    capitalized_words_list.append(capitalize_with_hyphens(word))

# Вывод преобразованных слов
print("Преобразованные слова:", ' '.join(capitalized_words_list))
