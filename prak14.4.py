# Ввод количества записей в словаре
num_entries = int(input("Введите количество записей в словаре: "))

# Создание словаря для хранения записей
dictionary = {}

# Ввод записей в словарь
for _ in range(num_entries):
    word, description = input("Введите слово и его описание через тире: ").split('-')
    dictionary[word] = description

# Запрос слова для поиска значения
query_word = input("Введите слово для поиска его значения: ")

# Поиск значения слова в словаре
if query_word in dictionary:
    print("Описание значения слова", query_word + ":", dictionary[query_word])
else:
    print("Нет в словаре")
