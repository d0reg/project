import random

random_number = random.randint(100, 999)

digit1 = random_number // 100
digit2 = (random_number % 100) // 10
digit3 = random_number % 10

print(digit1, digit2, digit3, sep=',')