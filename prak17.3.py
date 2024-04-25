def days_to_exam(K):
    import datetime

    # Текущая дата
    current_date = datetime.datetime.now()

    # Добавляем K дней к текущей дате
    exam_date = current_date + datetime.timedelta(days=K)

    # Форматируем дату для вывода
    formatted_date = exam_date.strftime("%d.%m")

    return formatted_date

# Запрос пользователю для ввода количества дней до экзамена
K = int(input("Введите количество дней до экзамена: "))

# Получение и вывод конкретного дня и месяца экзамена
print("Экзамен состоится", days_to_exam(K))
