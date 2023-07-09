#Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

A = int(input("Введите первое число: "))
B = int(input("Введите второе число: "))

def func_grade(x, y):
    if y == 0:
        return 1
    else:
        return x * func_grade(x, y-1)

print(func_grade(A, B))
