from PIL import Image, ImageDraw
from math import sin, cos, radians

# Создаем новое изображение
width, height = 800, 600
image = Image.new("RGB", (width, height), "skyblue")
draw = ImageDraw.Draw(image)

# Рисуем солнце
draw.ellipse((700, 50, 750, 100), fill='yellow')

# Рисуем лучи солнца
for i in range(0, 360, 30):
    draw.line((725, 75, 725 + 50 * cos(radians(i)), 75 + 50 * sin(radians(i))), fill='yellow', width=2)

# Рисуем поле
draw.rectangle((0, 400, width, height), fill='green')

# Рисуем дом
draw.rectangle((200, 300, 500, 500), fill='orange')

# Рисуем окна
draw.rectangle((250, 350, 350, 450), fill='white')
draw.rectangle((400, 350, 500, 450), fill='white')

# Рисуем дверь
draw.rectangle((320, 400, 380, 500), fill='brown')

# Рисуем крышу
draw.polygon([(200, 300), (350, 200), (500, 300)], fill='red')

# Рисуем дымоход
draw.rectangle((450, 200, 480, 300), fill='gray')

# Рисуем дым
draw.arc((450, 150, 480, 200), start=0, end=180, fill='gray')

# Сохраняем изображение
image.save("dom.png")