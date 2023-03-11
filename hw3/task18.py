# Требуется найти в массиве A[1..N] самый близкий по величине элемент
# к заданному числу X. Пользователь в первой строке вводит натуральное число N
# – количество элементов в массиве. В последующих  строках записаны
# N целых чисел Ai. Последняя строка содержит число X

elem_count = int(input())
num_list = list()
while elem_count > 0:
    num_list.append(int(input()))
    elem_count -= 1
search = int(input())

diff = abs(search - num_list[0])
result = num_list[0]

for el in num_list:
    if abs(search - el) < diff:
        diff = abs(search - el)
        result = el

print(result)
