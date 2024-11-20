'''Модуль отрисовки открытки 4'''
from PIL import Image, ImageDraw, ImageFont


def special_postcard():
    '''Функция рисует открытку для Никиты'''
    picture = Image.new('RGB', (400, 500), (255, 255, 255))
    draw = ImageDraw.Draw(picture) #Отрисовка открытки
    draw.ellipse((100, 200, 300, 400), 'yellow', 'blue')
    draw.ellipse((150, 260, 175, 285), 'black', 'blue')
    draw.ellipse((225, 260, 250, 285), 'black', 'blue')
    draw.arc((140, 310, 260, 370), 0, 180, 0)
    font = ImageFont.truetype('/Users/mariaboldinova/PycharmProjects/pythonProject1/design/font.ttf', size=25, encoding='UTF-8')
    draw.text((60, 40), "Поставь максимальный", font=font, fill='black') #Добавление надписи
    draw.text((100, 70), "балл, пожалуйста)", font=font, fill='black')
    picture.save('Postcard.jpg', 'JPEG')