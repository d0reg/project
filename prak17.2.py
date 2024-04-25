import random

def generate_exam_schedule(num_exams, subjects):
    days_of_week = ["понедельник", "вторник", "среда", "четверг", "пятница"]
    exam_times = [9.0, 9.5, 10.0, 10.5, 11.0, 11.5, 12.0, 12.5, 13.0, 13.5, 14.0]
    tickets = random.sample(range(1, 21), num_exams)

    print("Расписание экзаменов:")
    for subject in subjects:
        day = random.choice(days_of_week)
        time = random.choice(exam_times)
        tickets_num = tickets.pop()
        print(f"Экзамен по дисциплине «{subject}» состоится в {day} время {int(time)}:{'30' if time % 1 else '00'}. Ваш счастливый билет №{tickets_num}.")

# Запрос пользователю для ввода количества экзаменов и наименований дисциплин
num_exams = int(input("Введите количество экзаменов: "))
subjects = input("Введите наименования дисциплин через запятую и пробел: ").split(", ")

generate_exam_schedule(num_exams, subjects)
