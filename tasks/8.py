
# region 📚 Шпаргалка ЕГЭ | Задание №8


# Условие:
# Все шестибуквенные слова, в составе которых могут быть только русские буквы А, Е, К, Н, С записаны
# в алфавитном порядке и пронумерованы начиная с 1.
# Ниже приведено начало списка.
#
# АААААА
# АААААЕ
# АААААК
# АААААН
# АААААС
# ААААЕА
# Под каким номером в списке идёт слово СЕНЕКА?


# Решение (через itertools):
'''
import itertools
count = 0
for s in itertools.product('АЕКНС', repeat=6):
    slovo = ''.join(s)
    count += 1
    if slovo == 'СЕНЕКА':
        print(count)
'''


# Решение (через цикл for):
'''
s = 'АЕКНС'
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        slovo = a + b + c + d + e + f
                        count += 1
                        if slovo == 'СЕНЕКА':
                            print(count)
'''


# Условие:
# Ярослав составляет коды из букв, входящих в слово ЯРОСЛАВ.
# Код должен состоять из 5 букв,
# буквы в коде не должны повторяться, согласных в коде должно быть больше, чем гласных,
# две гласные буквы нельзя ставить рядом.
# Сколько кодов может составить Ярослав?


# Решение (через itertools):
'''
import itertools
count = 0
for s in itertools.permutations('ЯРОСЛАВ', 5):
    slovo = ''.join(s)
    glas = [i for i in slovo if i in 'ЯОА']
    sogl = [i for i in slovo if i in 'РСЛВ']
    if len(sogl) > len(glas):
        if all(x not in slovo for x in 'ЯА АЯ АО ОА ЯО ОЯ'.split()):
            count += 1
print(count)
'''


# Решение (через цикл for):
'''
s = 'ЯРОСЛАВ'
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    slovo = a + b + c + d + e
                    if len(set(slovo)) == 5:
                        glas = [i for i in slovo if i in 'ЯОА']
                        sogl = [i for i in slovo if i in 'РСЛВ']
                        if len(sogl) > len(glas):
                            if all(x not in slovo for x in 'ЯА АЯ АО ОА ЯО ОЯ'.split()):
                                count += 1
print(count)
'''


# 📚 Полезные ссылки на статьи и разборы задач:
# 📘 Полная версия шпаргалки доступна в нашем тг канале: https://t.me/informatika_kege_itpy/362?comment=1424
# 📙 Разбор номера 15947 #reshu по информатике: https://t.me/informatika_kege_itpy/473
# 📗 Разбор номера 4199 #polyakov по информатике: https://t.me/informatika_kege_itpy/475
# 📘 Разбор номера 12917 #kege по информатике: https://t.me/informatika_kege_itpy/477
# 📕 Разбор номера из нового варианта #statgrad по информатике: https://t.me/informatika_kege_itpy/484
# 💡 Функции split() и join(), где они могут пригодиться на КЕГЭ: https://t.me/informatika_kege_itpy/126
# 💡 Функции all() и any(), где они могут пригодиться на ЕГЭ: https://t.me/informatika_kege_itpy/378
# 🐍 Функция permutations() из библиотеки itertools в Python: https://t.me/informatika_kege_itpy/391
# 🐍 Функция product из библиотеки itertools в Python: https://t.me/informatika_kege_itpy/393
# 🐍 Вспомним полезные функции из библиотеки itertools: https://t.me/informatika_kege_itpy/470


# endregion (не удаляйте меня, я тут не просто так)


# todo: сюда можно писать заметки, чтобы не забыть задать вопрос репетитору ☝️
progress_result = ()  # Сюда заносятся номера, прорешанных задач.
print('Рекомендуемое кол-во решенных задач для закрепления номера 50.')
print(f'Проверим прогресс: ~{int(len(progress_result) * (100 / 50))}% задач прорешано.')
