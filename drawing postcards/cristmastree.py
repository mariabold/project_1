'''Модуль отрисовки открытки 2 '''
from PIL import Image, ImageDraw, ImageFont
from choice import choose_color, colors


def tree():
    '''Функция рисует ёлку в комнате'''
    print('Выбери цвет стен в комнате: синий, красный, зелёный, жёлтый, белый, чёрный, серый, розовый, голубой, коричневый')
    code = choose_color()
    picture = Image.new('RGB', (400, 500), code) #Отрисовка
    draw = ImageDraw.Draw(picture)
    print('Теперь выбери цвет пола(варианты цветов те же)')
    code = choose_color()
    draw.polygon(((0, 500), (0, 350), (400, 350), (400, 500)), fill=code, outline='black')
    print('Пришло время выбрать цвет для ведраи ёлки: варианты те же. Введи два выбранных цвета через пробел без знаков')
    flag = True
    while flag: #За счёт двойного ввода не можем отслать к модулю Choice
        color = input().split()
        try:
            code = colors[color[0].lower()]
            code_tree = colors[color[1].lower()]
            flag = False
        except:
            print("Пока ты не можешь выбрать этот цвет, но скоро мы это обязательно исправим!")
    draw.polygon(((140, 425), (120, 325), (280, 325), (260, 425)), fill=code, outline='black')
    draw.line(((200, 325), (200, 310)), fill='brown', width=30)
    draw.polygon(((90, 310), (310, 310), (200, 210)), fill=code_tree, outline='black')
    draw.polygon(((100, 220), (300, 220), (200, 130)), fill=code_tree, outline='black')
    draw.polygon(((110, 140), (290, 140), (200, 40)), fill=code_tree, outline='black')
    font = ImageFont.truetype('font.ttf', size=25, encoding='UTF-8')
    draw.text((100, 10), "Happy New Year!", font=font, fill='black') #Добавление надписи
    picture.save('NewYear.jpg', 'JPEG')