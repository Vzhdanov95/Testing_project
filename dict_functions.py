cars_dict = {"car_1": "Audi", "car_2": "Ford"}

# cars_dict.pop("car_2") # удаление по ключу

# print(cars_dict)

    # copy() creating new object 
# check = cars_dict.copy() # creating new object
# print(check is cars_dict) # False

    # now point to the same object in memory. 
# check = cars_dict 
# print(check is cars_dict) # True

    # So if you change one — the other changes too
# check["car_3"] = "BMW"

    # items() возвращает tuple с ключ значениями
# items = cars_dict.items() 
# print(items)   

    # get() это безопасный способ получения значения по ключу  
# data = {"name": "Oleg"}
# print(data.get("age"))  # Он не вызывает ошибку, если ключа нет
# print(data.get("age", 12)) # Работаете с неустойчивыми или необязательными ключами. Указать значение по умолчанию

# print(data["age"]) # так выведет ошибку

    # values() and keys()
# print(cars_dict.values())
# print(cars_dict.keys())

    # update() меняет значение ключа либо добавляет новое
# cars_dict.update({"car_1": "Chevrolet"})
# cars_dict.update({"car_3": "Chevrolet"})
# print(cars_dict)

    # fromkeys() создать из значений ключи
# list_with_ids = [1, 2, 3, 4, 5, 6]
# my_ids = {}.fromkeys(list_with_ids, "add any value") # по умолчанию None
# print(my_ids)

    # popitem() удаляет последнее значение с dict
# cars_dict.popitem()
# print(cars_dict)