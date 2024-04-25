# Запрос ввода строки
input_string = input("Введите строку: ")

# Создание новой строки с удвоенными символами
doubled_string = ''.join(char * 2 for char in input_string)

# Вывод строки с удвоенными символами
print("Результат:", doubled_string)
