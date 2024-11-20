'''Модуль отрисовки открытки 1'''
from PIL import Image, ImageDraw, ImageFont
from Choice import choose_color


def snowman():
    '''Функция отрисовки снеговика'''
    print('Выбери цвет фона: синий, красный, зелёный, жёлтый, белый, серый, розовый, голубой, коричневый')
    code = choose_color()
    picture = Image.new('RGB', (400, 500), code) #Создание фона + снега
    draw = ImageDraw.Draw(picture)
    print('Снег же будет белым? Ответь, да или нет')
    answer = input().lower()
    if answer == 'да':
        draw.polygon(((0, 500), (0, 350), (400, 350), (400, 500)), fill='white')
    if answer == 'нет':
        print('А какой? Введи цвет из перечисленных: синий, красный, зелёный, жёлтый, белый, чёрный, серый, розовый, голубой')
        code = choose_color()
        draw.polygon(((0, 500), (0, 350), (400, 350), (400, 500)), fill=code)
    print('А какого цвета будет снеговик? Варианты цветов те же(но лучше не выбирай чёрный)')
    code = choose_color()
    draw.line(((150, 250), (75, 326)), fill=(128, 64, 48), width=10) #Отрисовка снеговика
    draw.line(((250, 250), (325, 326)), fill=(128, 64, 48), width=10)
    draw.ellipse((125, 275, 275, 425), fill=code, outline='black')
    draw.ellipse((137, 199, 263, 325), fill=code, outline='black')
    draw.ellipse((150, 125, 250, 225), fill=code, outline='black')
    draw.ellipse((175, 150, 191, 166), fill='black')
    draw.ellipse((209, 150, 225, 166), fill='black')
    draw.ellipse((175, 180, 225, 200), fill='black', outline='black')
    draw.polygon(((175, 175), (175, 190), (225, 190), (225, 175)), fill=code)
    draw.polygon(((160, 140), (170, 85), (230, 85), (240, 140)), fill='grey', outline='black')
    font = ImageFont.truetype('/Users/mariaboldinova/PycharmProjects/pythonProject1/design/font.ttf', size=25, encoding='UTF-8')
    draw.text((100, 40), "Happy New Year!", font=font, fill='black') #Добавление надписи
    picture.save('NewYear.jpg', 'JPEG')
