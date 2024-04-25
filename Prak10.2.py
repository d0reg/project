# Введите непустую последовательность символов
sequence = input("Введите непустую последовательность символов: ")

# Создадим пустое множество для хранения цифр
digits_set = set()

# Пройдемся по каждому символу в последовательности
for char in sequence:
    # Проверим, является ли символ цифрой
    if char.isdigit():
        # Если да, добавим его в множество
        digits_set.add(char)

# Выведем результат
print("Множество цифр, встречающихся в последовательности:", digits_set)
