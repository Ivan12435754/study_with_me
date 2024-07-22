
# region 📚 Шпаргалка ЕГЭ | Задание №2

# Задание №1: https://inf-ege.sdamgia.ru/problem?id=56502
# Логическая функция F задаётся выражением:
# ((x→ y) ∨ (z → w)) ∧ ((z ≡ y) → (w ≡ x)).
#
# Дан частично заполненный фрагмент, содержащий неповторяющиеся строки таблицы истинности функции F.
# Определите, какому столбцу таблицы истинности соответствует каждая из переменных w, x, y, z.

# Решение:
'''
print("x y z w")
for x in 0, 1:
    for y in range(2):
        for z in 0, 1:
            for w in range(2):
                F = (((x <= y) or (z <= w)) and ((z == y) <= (w == x)))
                if F == 0:
                    print(x, y, z, w)
'''

# Чистое решение кодом:
'''
from itertools import *

def F(x, y, z, w):
    return ((x <= y) or (z <= w)) and ((z == y) <= (w == x))


for a1, a2, a3, a4 in product([0, 1], repeat=4):
    table = [(a1, 1, 0, a2), (0, 1, 0, 1), (a3, 1, 0, a4)]
    if len(set(table)) == len(table):
        for i in permutations('xyzw'):
            if [F(**dict(zip(i, r))) for r in table] == [0, 0, 0]:
                print(*i, sep='')

'''


# Задание №2: https://stepik.org/lesson/1038536/step/5?unit=1062771
# Логическая функция F задаётся выражением: (z ≡ ¬x) → ((w → ¬y) ∧ (y → x)).
# Дан частично заполненный фрагмент, содержащий неповторяющиеся строки таблицы истинности функции F.
# Определите, какому столбцу таблицы истинности соответствует каждая из переменных x, y, z, w.

# Решение:
'''
print('x y z w F')
for x in 0, 1:
    for y in 0, 1:
        for z in range(2):
            for w in range(2):
                F = (z == (not x)) <= ((w <= (not y)) and (y <= x))
                if F == 0:
                    print(x, y, z, w, int(F))
                    
for x in range(2):
    for y in range(2):
        for z in 0, 1:
            for w in 0, 1:
                F = (z == (not x)) <= ((w <= (not y)) and (y <= x))
                if F == 1:
                    print(x, y, z, w, int(F))
'''


# 📚 Полезные ссылки на статьи и разборы задач:
# 📘 Полная версия шпаргалки доступна в нашем тг канале: https://t.me/informatika_kege_itpy/362?comment=1424
# 📘 Разборы 2 номеров по информатике: https://t.me/informatika_kege_itpy/360?comment=1461
# endregion (не удаляйте меня, я тут не просто так)


# todo: сюда можно писать заметки, чтобы не забыть задать вопрос репетитору ☝️
progress_result = ()  # Сюда заносятся номера, прорешанных задач.
print('Рекомендуемое кол-во решенных задач для закрепления номера 30.')
print(f'Проверим прогресс: ~{int(len(progress_result) * (100 / 30))}% задач прорешано.')