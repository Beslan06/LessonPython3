# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def sum_index(lst):
    s = 0
    for i in range(len(lst)):
        if i % 2 != 0:
            s += lst[i]
    print(f"Сумма равна: {s}")

lst = [2, 3, 5, 9, 3]
sum_index(lst)
lst = list(map(int, input("Введите числа через пробел:\n").split()))
sum_index(lst)

# x = [2, 3, 6, 10, 12, 16, 5]
# summ = 0
# for i in range(1, len(x), 2):
#         summ += x[i]       
# print(f"{x} -> сумма элементов на нечётных позициях: {summ}")