my_name = 'Vadym' # Стринга под капотом условный Tuple тоесть immutable
# print(my_name[0])

# print(my_name[2:5]) # слайсинг, последнее не включительно.
# print(my_name[0:5:2]) # 2 здесь это шаг
# print(my_name[-1])  # Обратная индексация
# print(my_name[::-1]) # Переворот стринги

some_list = [3,4,5,6,7] # [start, stop, step(1 брать без пропусков)]
print(some_list[::-1])
print(some_list[1:2:1])