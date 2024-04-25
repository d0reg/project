# Функция для формирования нового предложения
def create_sentence(numbers, words):
    # Разбиваем строки на списки
    numbers_list = numbers.split()
    words_list = words.split()

    # Создаем новое предложение, начиная с большой буквы
    new_sentence = words_list[int(numbers_list[0]) - 1].capitalize()

    # Добавляем остальные слова
    for number in numbers_list[1:]:
        new_sentence += " " + words_list[int(number) - 1]

    # Добавляем точку в конце
    new_sentence += "."

    return new_sentence


# Ввод номеров слов
numbers = input("Введите номера слов через пробел: ")

# Ввод самих слов
words = input("Введите слова через пробел: ")

# Формирование нового предложения
new_sentence = create_sentence(numbers, words)

# Вывод нового предложения
print("Новое предложение:", new_sentence)
