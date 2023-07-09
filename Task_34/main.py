# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
#     **Вывод:** Парам пам-пам

vovels = 'аеёиоуыэюя' #список гласных букв

poem =((input('введите стих: ')).split())
countVovels = set() #множество для проверки различия количества гласных во фразах
print(poem)
for frase in poem:
    glas = list(filter(lambda x: x in vovels, frase))
    countVovels.add(len(glas)) #добавление количества гласных во фразе

if len(countVovels) == 1: #если количество гласных во всех фразах совпадает
    print('Парам пам-пам')
else:
    print('Пам парам')