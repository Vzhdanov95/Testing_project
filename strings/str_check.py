# provided_names = 'john peter brian Morgan Adam Maria bart'
# print(provided_names.title())

# ######################

# friends = ["John", "Marta", "James", "Amanda", "Marianna"]
# print("Names".center(15, "*"))
# for friend in friends:
#     print(f"{friend.rjust(10)}")

# ########################################
# """there is a string " name=Amanda=sssss&age=32&&salary=1500&currency=euro ". 
# Convert this string to a dictionary {name: Amanda, age: 32, salary: 1500, currency: euro}"""


# some_string = "name=Amanda=sssss&age=32&&salary=1500&currency=euro"

# cleaned = some_string.replace("=sssss", "").replace("=", ":").replace("&&", "&").replace("&", ",")
# pairs = cleaned.split(",")
# # print(pairs) # ['name:Amanda', 'age:32', 'salary:1500', 'currency:euro']

# result = {} # initialize an empty dictionary where we pull key values from our string

# for pair in pairs:
#     if ":" in pair:
#         key, value = pair.split(":", 1)
#         result[key] = value
# print(result)

some_flt = '12445'
country = "Bangladesh is Huge country"
print(country.encode('UTF-16'))

coded = country.encode('UTF-16')
print(coded.decode('UTF-16'))

