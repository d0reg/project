from PIL import Image

# Открываем изображение
image = Image.open('risunok3.jpg')

# Преобразуем изображение в черно-белое
bw_image = image.convert('L')

# Зеркально отражаем изображение
mirrored_image = bw_image.transpose(Image.FLIP_LEFT_RIGHT)

# Изменяем размер изображения (замените значения на нужные вам)
new_width = 800
new_height = 600
resized_image = mirrored_image.resize((new_width, new_height))

# Сохраняем преобразованное изображение
resized_image.save('risunok4.jpg')

# Закрываем изображения
image.close()
resized_image.close()
