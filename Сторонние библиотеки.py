# requests, numpy, matplotlib
import numpy
from PIL import Image
import requests


# Запросить данные с помощью библиотеки requests из API и вывести их в консоль.
url = 'https://www.google.com'
responce = requests.get(url)
if responce.status_code == 200:
    print(responce.text)
else:
    print('error:', responce.status_code)

# Создать массив чисел с помощью библиотеки numpy,
# выполнить математические операции с массивом и вывести результаты.
num1 = [1, 2, 5, 6]
arr = numpy.array(num1)
print(arr * 3)
print(arr ** 2)

# Обработать изображение с помощью библиотеки pillow, например,
# изменить его размер, применить эффекты и сохранить в другой формат.
image = Image.open('Figure_1.jpeg')
print(image.format, image.size, image.mode)
image_res = image.rotate(90)
image_res = image_res.resize((300, 300))
image_res.save('myplotRes.png')