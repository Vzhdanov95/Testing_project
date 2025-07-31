    # Mutable data types

# names = ["Alyona", "Adam", "Alice"]
# cities_countries = {"New York": "United States", "Kyiv": "Ukraine", "Deli": "India"}
# unique_ids = {124343, 38983493, 47583834, 37783394, 37783394}
# print(len(unique_ids))
# print(unique_ids)

    # Immutable data types 
number_int = 2 # new object - different id()
number_int = 3 # new object and reassigned value - different id()

number_float = 3,5
number_float = 9.9

type_string = "Same old song"
# type_string[0] = "T"
# print(type_string) # doesn't support item assignment

is_valid = True or False

# fs = frozenset([1, 2, 3])
# fs = frozenset({1, 2, 3})
# fs = frozenset((1, 2, 3))
# print(fs)

# company_names_nt_change = ("Desert inc.", "Black eagle.ent", "Blizzard")
# print(company_names_nt_change)


# another_tuple = (2, 3, [23, 23, 44])
# print(another_tuple)
# another_tuple[2].append(44)
# print(another_tuple)

    # Преобразование типов либо type conversion 
# change_value = 4
# print(type(change_value))
# change_value = str(change_value)
# print(type(change_value))

group_of_people = ["Nina", "Maks", "Anna", "Dimon", "Dimon"]

# group_of_people = set(group_of_people)
group_of_people = str(group_of_people)
print(group_of_people)
group_of_people = list(group_of_people)
print(group_of_people)
