# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

A = int(input("Введите первое число: "))
B = int(input("Введите второе число: "))

def func_sum(x, y):
    if x == 0 and y == 0:
        return 0
    elif x!=0 and y == 0:
        return 1+func_sum(x-1, y)
    elif x == 0 and y!=0:
        return 1+func_sum(x, y-1)
    else:
        return 2 + func_sum(x-1, y-1)
print(func_sum(A, B))