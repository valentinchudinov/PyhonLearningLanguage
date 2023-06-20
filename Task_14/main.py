user_number = int(input("Введите число: "))
couples = 1

print(f"Целыe степени двойки до числа {user_number}", end=":| ")
while couples < user_number:
    print(couples, end=" | ")
    couples *= 2