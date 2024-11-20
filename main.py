from CristmasTree import tree
from Snowman import snowman
from Snowing import snow
from Special import special_postcard
import datetime


def printer():
    '''Функция выводит информацию о том, где найти готовую открытку'''
    print('Твоя открытка готова! Проверь файлы твоего проекта, она будет называться "NewYear.jpg"')


def days_till_new_year():
    '''Функция считает, сколько дней осталось до Нового года'''
    today = datetime.datetime.now().date()
    new_year = datetime.date(2025, 1, 1)
    num_days = (new_year - today).days
    print(f'Кстати, знаешь, сколько дней до Нового года? {num_days}! С наступающим!')


print('Привет читающий! Добро пожаловать в генератор новогодних открыток. Тут ты можешь создать открытку или добавить надпись на уже существующую')
print('Выбери, что будет нарисовано на открытке и введи цифру')
text = '''1. Снеговик
2. Ёлка
3. Снежинка
4. Открытка для Никиты'''
print(text)
theme = int(input())
if theme == 1: #Выбор вида открытки
    snowman()
    printer()
    days_till_new_year()
elif theme == 2:
    tree()
    printer()
    days_till_new_year()
elif theme == 3:
    snow()
    printer()
    days_till_new_year()
elif theme == 4:
    special_postcard()
    print('Твоя открытка готова! Проверь файлы твоего проекта, она будет называться "Postcard.jpg"')
    days_till_new_year()
else:
    print('К сожалению, я не могу распосзнать твой ввод:( Попробуй запустить программу снова и всё обязательно получиться!')