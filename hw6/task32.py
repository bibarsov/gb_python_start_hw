"""
Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше заданного максимума)
"""
from numpy import random

left: int = int(input())
right: int = int(input())

arr = [random.randint(10) for _ in range(10)]
print(*arr)
arr = {index for index, value in enumerate(arr) if left <= value <= right}
print(*arr)
