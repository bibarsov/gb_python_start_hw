"""
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа,
которые встречаются в обоих наборах.
Пользователь вводит 2 числа.
 n - кол-во элементов первого множества.
 m - кол-во элементов второго множества.
Затем пользователь вводит сами элементы множеств.
"""


# O(n*log(n)) sorting algorithms are certainly better,
# but I'll use this as a simplest solution here
def bubble_sort(given_list):
    for i in range(len(given_list)):
        for j in range(i, len(given_list)):
            if given_list[i] > given_list[j]:
                elem = given_list[j]
                given_list[j] = given_list[i]
                given_list[i] = elem


n = int(input())
m = int(input())
nums_set = set()

while n > 0:
    nums_set.add(int(input()))
    n -= 1
result = list()
while m > 0:
    num = int(input())
    if num in nums_set:
        result.append(num)
    m -= 1

print(result)
bubble_sort(result)
print(result)
