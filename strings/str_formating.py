# форматирование стринги, F-string 
name = 'George'
age = 33
year = 2008
decimal = 493.7567
percent = 43.483
big_number = 1_000_000_0000_483
big_decimal_number = 1_383_84.6768
text = 'Honestly'

# print(f'Name and age: {name} is {age}') 
# print(f'Dan\'s mission') # екранирование
# print(f'1 + 1 = {1 + 1}')

# print(f'{year=}')

# print(f'{decimal:.2f}') # округлить или убрать десятичные числа
# print(f'{decimal:.0f}') # округлить или убрать десятичные числа
# print(f'{decimal:.1f}') # округлить или убрать десятичные числа
# print(f'{decimal:.3f}') # округлить или убрать десятичные числа

# print(f'{percent:.1%}') # отобразить в процентах

# print(f'{big_number:_}') # можно в f стринге применять разделитель _
# print(f'{big_number:,}') # можно в f стринге применять разделитель ,  #только два
# print(f'{big_decimal_number:_.2f}') # применяя разделитель можно укзать количество десятых
# print(f'{big_decimal_number:,.1f}') # # применяя разделитель можно укзать количество десятых

# nested F strings
# print(f'{1 + 1} and {f'{2 + 2}'}') not that often used


# Add spaces ofr specific separator for formating (выравнивания)
# print(f'{text:>20}')
# print(f'{text:*^20}')
# print(f'{text:_<20}')
# n = 20
# print(f'{text:">{n}}')

# print(f'Name:{name}\nAge:{age}') # \n является отступом

# multi_str = """Hens are for the motherland ducks are against.
# And the dog is divided. For a moment he turns
# his bloodshot eyes to the sky. Then his gaze
# drops to the road again. In dust up to his armpits"""

# formating using format() method

writers = 'Wraiters names are {0}{1}{2}'
print(writers.format('Jack London ', 'Edgar Poe ', 'W. Shakespear'))