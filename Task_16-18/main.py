import random

list_num = list()
min_list_num = 1
max_list_num = 10

for i in range(0, int(input('Введите количество элементов:\n'))):
    list_num.append(random.randint(min_list_num, max_list_num))
print(list_num)

desired_element = int(input(f"Какой элемент нужно найти?\n"))
count = list_num.count(desired_element)
print(f"Найденных элементов со значением {desired_element}: => {count}.")

if count == 0:
    temp = None
    min_num = abs(desired_element - list_num[0])
    for i in list_num:
        if abs(desired_element - i) <= min_num:
            temp = i
            min_num = abs(desired_element - i)
    print(f"Ближайшее число к искомому значению: {temp}. ")