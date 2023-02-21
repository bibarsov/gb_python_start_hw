# Задача 6: Требуется написать программу, которая проверяет счастливость билета.

# соблюдаем DRY
def get_sum(num):
    num_sum = 0
    for digit in num:
        num_sum += int(digit)
    return num_sum


ticket_num = input()
if len(ticket_num) != 6:
    print("no")  # kind of validation
if get_sum(ticket_num[0:3]) == get_sum(ticket_num[3:6]):
    print("yes")
else:
    print("no")
