# Ввод количества оценок
num_grades = int(input("Введите количество оценок: "))

# Инициализация списка для хранения оценок
grades = []

# Считывание оценок
for i in range(num_grades):
    grade = float(input(f"Введите оценку {i+1}: "))
    grades.append(grade)

# Вывод оценок
print("Оценки:")
for grade in grades:
    print(grade)

# Вычисление средней оценки
average_grade = sum(grades) / num_grades
print("Средняя оценка за урок:", average_grade)
