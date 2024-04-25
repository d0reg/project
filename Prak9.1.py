# Запрос ввода двух строк
first_string = input("Введите первую строку: ")
second_string = input("Введите вторую строку: ")

# Проверка условия и вывод результата
if first_string[-1] == second_string[0]:
    print("ВЕРНО")
else:
    print("НЕВЕРНО")
