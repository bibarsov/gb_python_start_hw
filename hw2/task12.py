"""
Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
а Катя должна их отгадать.
Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
Помогите Кате отгадать задуманные Петей числа.
"""

s = int(input())
p = int(input())

for i in range(1, 1001):
    for j in range(i, 1001):
        if i + j == p and i * j == s:
            print("x= {}, y= {}".format(i, j))