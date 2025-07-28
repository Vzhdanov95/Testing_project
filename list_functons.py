object_list = [1, 3, 4, 5, 56, 9, 23, 9]
# print(object_list.index(9))

# object_list.append(44)
# object_list.append(99)
# object_list.remove(99)
# object_list.remove(9)
# print(object_list)

# object_list.sort(reverse=True)
# # print(object_list)

# object_lsit_1 = object_list.copy()
# print(object_lsit_1)
# print(object_list)


# print(object_list.count(9)) 

# subject_list = ["Breathe", 5555]  # вместо использования "+"" в обьеденении листов
# object_list.extend(subject_list)
# print(object_list)

object_list.insert(3, "this is five:")

object_list.pop(3) # удалили то что заинсертили методом insert() выше
print(object_list)
