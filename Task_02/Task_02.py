userNumber = int(input("Введите трехчначное число: "))

if userNumber < 0:
    userNumber = abs(userNumber)

if userNumber > 99 and userNumber < 1000:
    res = (userNumber // 100) + ((userNumber // 10) % 10) + (userNumber % 10)
    print(f"Сумма цифр числа {userNumber} = {res}.")
else:
    print("Число не является трехзначным.")
