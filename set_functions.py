unique_set_of_values = {3, 4, 5, 77, 100, 40}

    # update()
# unique_set_of_values.update({3, 40, 99})
# print(unique_set_of_values)

    # pop() deletes from the last index
# print(unique_set_of_values)
# unique_set_of_values.pop()
# print(unique_set_of_values)

    # add() добавление
# unique_set_of_values.add("Hello")
# print(unique_set_of_values)

    # difference() сравнение каких значений между сетами нету
# data_set_1 = {40, 33, 130, 120, 7, 2, 1, 80, 90}
# data_set_2 = {40, 33, 130, 120, 7, 2, 1, 81, 92}

# print(data_set_1.difference(data_set_2))
# print(data_set_2.difference(data_set_1))

    # discard() удаляет елемент и не выдает ошибку даже если елемента нет
# print(unique_set_of_values.discard('fox'))

#     # issubset() возвращает True или False если один сет имеет значения другого сета
# data_set_1 = {40, 33, 130, 120, 7, 2, 1, 80, 90}
# data_set_2 = {40, 120, 7}

# print(data_set_1.issubset(data_set_2)) # все ли елементы data_set_1 находятся в data_set_2 - нет не все - False
# print(data_set_2.issubset(data_set_1)) # все ли елементы data_set_2 находятся в data_set_1 - да все - True

    # intersection() - "пересечение" находит общие елементы межу сетами
# new_set_1 = {3, 4, 5, 77, 9}
# new_set_2 = {3, 55, 100}
# result = new_set_1.intersection(new_set_2)
# print(result)

    # union() - обьеденяет два сета
# new_set_1 = {3, 4, 5, 77, 9}
# new_set_2 = {3, 55, 100}
# print(new_set_1.union(new_set_2))
