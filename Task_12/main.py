sum = int(input("Введите сумму чисел: "))
multi = int(input("Введите произведение чисел: "))

count = 1
while count < sum:

    if sum - count == multi / count:
        print(f"Первое число {count}, второе число {sum - count}")
        break
    count += 1
