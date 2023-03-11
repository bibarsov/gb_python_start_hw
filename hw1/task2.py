# Задача 2: Найдите сумму цифр трехзначного числа.
num_str = input()
num_sum = 0
for digit in num_str:
    num_sum += int(digit)
print(num_sum)
