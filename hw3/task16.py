# Требуется вычислить, сколько раз встречается некоторое число X
# в массиве A[1..N]. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X

elem_count = int(input())
num_list = list()
while elem_count > 0:
    num_list.append(int(input()))
    elem_count -= 1
search = int(input())

result = 0
for item in num_list:
    if item == search:
        result += 1
print(result)
