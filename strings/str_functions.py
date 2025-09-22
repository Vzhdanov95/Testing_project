str_int = '445'
str_float = "22.09"
str_byte = '00993'
some_name = 'Dream Stream' # условный tuple

# print(some_name.find('a', 4, 10)) # находит по первому вхождению, find('', start, end)
# print(str_int.isdigit())
# print(str_float.isdigit()) # False потому что воспринимает точку как не цифру
# print(str_byte.isdigit())
# print(some_name.index("a"))
# print(some_name.rindex("a"))
# print(some_name.casefold()) # проигнорировать регистр, все в нижний регистр
# print(some_name.lower())

# print(some_name.find("a", 2))
# print(some_name.rfind("a", 2))
# print(some_name.rindex('e'))
# print(some_name.rfind('e'))
# print(some_name.count('d'))

# print(some_name.isidentifier())

# cookies = 'name=Igor=age=44=pass=3yr=role=controler'
# print(cookies.split('=')) # разбивает строку на список
# text = "Select your variant"
# print(text.split()) # по умолчанию разделяет на пробелы 

# cars = ['Volksvagen', 'Nissan', 'BMW', 'Porche'] 
# all_cars = " + ".join(cars) # 
# print(all_cars) 

# names = '    Spaces     '
# print(names.strip()) # убрать пробелы по умолчанию 

# countries = '??  Countries ??'
# print(countries.strip("??")) # убрать нужный символ по бокам

# authors = 'ricko jamson, edgar poe'
# print(authors.capitalize())
# print(authors.title())

# ninja_turtles = 'Rafaelo. Donatelo'
# print(ninja_turtles.replace('.', ','))
# print(ninja_turtles.endswith('elo'))
# print(ninja_turtles.startswith('Raf'))