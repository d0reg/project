# Ввод количества студентов
num_students = int(input("Введите количество студентов: "))

# Создание словаря для хранения информации о студентах
students_dict = {}

# Ввод информации о студентах
for _ in range(num_students):
    last_name, specialty, group_number = input("Введите фамилию, специальность и номер группы через пробел: ").split()
    if specialty not in students_dict:
        students_dict[specialty] = []
    students_dict[specialty].append(last_name)

# Запрос названия специальности
query_specialty = input("Введите название специальности для поиска студентов: ")

# Поиск студентов по названию специальности
if query_specialty in students_dict:
    print("Фамилии студентов на специальности", query_specialty + ":", ", ".join(students_dict[query_specialty]))
else:
    print("Проверьте запрос")
