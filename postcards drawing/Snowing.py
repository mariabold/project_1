'''Модуль отрисовки открытки 3'''
from PIL import Image, ImageDraw, ImageFont
from Choice import choose_color


def snow():
    '''Функция отрисовки снежинку'''
    print('Выбери цвет фона: синий, красный, зелёный, жёлтый, белый, чёрный, серый, розовый, голубой, коричневый')
    code = phon = choose_color()
    picture = Image.new('RGB', (400, 400), code) #Отрисовка снежинки
    draw = ImageDraw.Draw(picture)
    print('Какого цвета будет снежинка?')
    code = choose_color()
    draw.line(((200, 75), (200, 375)), fill=code, width=20)
    draw.line(((50, 225), (350, 225)), fill=code, width=20)
    draw.line(((87, 112), (313, 338)), fill=code, width=20)
    draw.line(((87, 338), (313, 112)), fill=code, width=20)
    draw.ellipse((170, 195, 230, 255), fill=code)
    draw.ellipse((180, 205, 220, 245), fill=phon)
    font = ImageFont.truetype('/Users/mariaboldinova/PycharmProjects/pythonProject1/design/font.ttf', size=25, encoding='UTF-8')
    draw.text((100, 40), "Happy New Year!", font=font, fill='black') #Надпись
    picture.save('NewYear.jpg', 'JPEG')