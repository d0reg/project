# Запрос ввода слова
word = input("Введите слово: ")

# Проверка длины слова и вывод четвертой буквы или сообщения "НЕТ"
if len(word) >= 4:
    print("Четвертая буква:", word[3])
else:
    print("НЕТ")
