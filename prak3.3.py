x = float(input("Введите первое число x: "))
y = float(input("Введите второе число y: "))

if x < y:
    x = (x + y) / 2
    y = 2 * x * y
else:
    y = (x + y) / 2
    x = 2 * x * y

print("Измененные значения x и y:", x, y)