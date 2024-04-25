def is_happy_date(date):
    import datetime

    # Проверка на кратность числа дня и не является ли день понедельником
    if date.day % 4 != 0 and date.weekday() != 0:
        return True
    return False

def predict_happy_dates(start_date, n, num_dates=3):
    import datetime

    happy_dates = []
    current_date = datetime.datetime.strptime(start_date, "%Y/%m/%d")

    while len(happy_dates) < num_dates:
        if is_happy_date(current_date):
            happy_dates.append(current_date.strftime("%d %B, %A"))
        current_date += datetime.timedelta(days=n)

    return happy_dates

# Запрос пользователю для ввода исходной даты и числа n
start_date = input("Введите исходную дату в формате YYYY/MM/DD: ")
n = int(input("Введите число n: "))

# Получение и вывод трех подходящих дат
happy_dates = predict_happy_dates(start_date, n)
print("Счастливые даты для экзамена:")
for date in happy_dates:
    print(date)
