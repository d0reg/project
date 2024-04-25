Y = 40
total_pages = Y

for i in range(2, 11):
    Y *= 1.05
    total_pages += Y

print(f"Количество страниц в книге: {total_pages}")