my_ids = [12, 33, 44, 55, 686]

    ##### for loop -> range (откуда до куда) по индексу не включительно
    ##### len() длинна моего массива (списка, кортежа и т.д.)

# for index in range(len(my_ids)):
#     print(my_ids[index])
#     pass

    #### используем _ вместо пременной если она нигде внутри цикла не используется 

    # for _ in range(4):
#       print("Repeat 4 times")

    #### for each четко для итерации наших обьектов/массивов
    #### break завершает цикл при условии а continue нечего не делай и иди дальше

# for number in my_ids:
#     if number == 44:
#         continue
#     print(number)


    #### можно пройтись по каждой итерации внутри итерации. Вложений цикл

# dif_numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# for column in dif_numbers:
#     for row in column:
#         print(row)
#     print('End iteration')


    ##### while цикл должен иметь каккой то выход а иначе выйдет беконечный цикл. 
    ##### выходы из цикла зачастую пишутся из вне

# counter = 0
# while True:
#     print("Count this")
#     if counter > 50:
#         break
#     counter = counter + 1

