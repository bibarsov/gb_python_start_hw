"""
 На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
 Определите минимальное число монеток, которые нужно перевернуть,
 чтобы все монетки были повернуты вверх одной и той же стороной.
 Выведите минимальное количество монет, которые нужно перевернуть
"""

n = int(input())
inputs = 0
min_monetkis_up = 0
min_monetkis_down = 0

while inputs < n:
    up = input()
    if up == 'True':
        min_monetkis_down += 1
    else:
        min_monetkis_up += 1
    inputs += 1

if min_monetkis_up <= min_monetkis_down:
    print(min_monetkis_up)
else:
    print(min_monetkis_down)
