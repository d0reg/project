X = 10
total_distance = X

for i in range(2, 8):
    X *= 1.1
    total_distance += X

print(f"Суммарный путь спортсмена за неделю: {total_distance} км")