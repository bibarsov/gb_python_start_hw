"""
 Задача 4:
 Петя, Катя и Сережа делают из бумаги журавликов.
 Вместе они сделали S журавликов.
 Сколько журавликов сделал каждый ребенок, если известно,
 что Петя и Сережа сделали одинаковое количество журавликов,
 а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
"""
cranes_num = int(input())
# x + 4x + x = S
# Петя:  S/6
# Катя: (S/6) * 4
# Серж:  S/6
print("%f %f %f" % (cranes_num / 6, cranes_num / 6 * 4, cranes_num / 6))