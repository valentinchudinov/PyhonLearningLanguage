import random

coins = int(input("Введите количество монеток: "))
index, eagle, tails = 0, 0, 0

while index < coins:
    side = random.randint(0, 1)

    if side == 0:
        eagle += 1
    else:
        tails += 1

    index += 1

print(f"eagle - {eagle}, tails - {tails}")

if eagle > tails:
    print(f"Минимальное количество переворотов: {tails}")
else:
    print(f"Минимальное количество переворотов: {eagle}")
