""" Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума) """

import random

Min = int(input("Введите минимум: "))
Max = int(input("Введите максимум: "))
N = int(input("Введите длину массива: "))

number_search = []
array_random = []
for i in range(N):
    array_random.append(random.randint(Min-10, Max+10))
print(f"Список чисел: {array_random}")

for i in range(N):
    if Min < array_random[i] < Max:
        number_search.append(i)

print(f"Номера позиций чисел в списке, которые находятся в нужном диапазоне: {number_search}")