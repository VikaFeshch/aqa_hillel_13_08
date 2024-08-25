# ##############
# # class str
# from os.path import split
#
# string = ""
# dir(string)
# #############
# # split()
#
# s = "My   name  is Vika. I'm QA engineer. I work and work, work..."
# words = s.split()
# print('string ', s)
# print("Example 1.1: ", s.split())
# print("Example 1.2: ", s.split(" "))
# print("Example 1.3: ", s.split(" "))
# print(words)
# print(s)
# print("Example 1.4: ", s.split("w"))
#
#
#
# splitlines()
# s = "My   name  is Vika. \n I'm QA engineer. \n I work and work, work..."
# print("Example 1.5: ", s.splitlines())
# #########
# # startswith(), endswith()
# s = "My   name  is Vika. \n I'm QA engineer. \n I work and work, work..."
# print("Example 1.6 ", s.startswith("My"))
#
# for word in s.split():
#     if word.startswith("w"):
#         print("Word starts with 'w'")
# ###########
#
# # lower(), upper(), islower(), isupper(), swapcase()
# expected_email = "ser@gmail.com"
# email_from_api = "Ser@gmail.com"
# lower_email_from_api = email_from_api.lower()
# if expected_email == email_from_api.lower():
#     print("comparison email")

########################
# istitle(), capitalise(), title()
# print("Is title& -> ", s.istitle())
# print("Capitalize -> ", s.capitalize())
# print("Title -> ", s.title())

###########################################
# # find() vs in, count()
#
# s = "My   name  is Vika.  I'm QA engineer. I work and work, work..."
#
# print("Example of find ", s.find("name"))
# print("Example of find ", s.find("QAQA"))
# print("Example of find with params ", s.find("work", 0, 50))
# if "m" in s:
#     print("Found letter 'm'")
# print("Example of count ", s.count("work"))

############################
# # strip(), rstrip(), lstrip()
# s = "   My   name  is Vika.  I'm QA engineer. I work and work, work...   "
# print("Example of strip ", s.strip())
# print("Example of rstrip ", s.rstrip())
# print("Example of lstrip ", s.lstrip())
# header = '(Built"'
# print("Example of strip ", header.strip('()'))

#########################################
# #replace()
#
# expected_header_with_price = "Apples cost 24.5 uah 24.5"
# new_h_price = expected_header_with_price.replace("24.5","30", 1)
# new_h_price1 = expected_header_with_price.replace("24.5","30")
# print("Replace: ", new_h_price)
# print("Replace: ", new_h_price1)

# #############################################
# # join()
#
# fruits = "apple,banana,pear,apple,pineapple,banana"
# fruits_without_apple = fruits.replace("apple", "")
# print(fruits_without_apple)
# lists_of_fruits = fruits.split(",")
# print(lists_of_fruits)
# fruits_without_apple = []
# for word in lists_of_fruits:
#     if word != 'apple':
#         fruits_without_apple.append(word)
# print(fruits)
# print(fruits_without_apple)
# print("| ".join(fruits_without_apple))
# lists_of_fruits_without_apple = ", ".join(fruits_without_apple)
# print(lists_of_fruits_without_apple)

##################################################
# form_data = {
#     "first_name": "Vika",
#     "age": "47"
# }
# print(int(form_data["age"])+2)
# print(float('12365445'))
#
# print("Empty string ->", bool(""))
# print("String ->", bool("Vika"))
# print("String ->", bool("True"))
# print("String 'False' ->", bool("False"))

#################################################

# fruits = "apple,banana,pear,apple,pineapple,banana"
# # fruits_without_apple = fruits.replace("apple", "")
# # print(fruits_without_apple)
# lists_of_fruits = fruits.split(",")
# tuple_of_fruits = tuple(lists_of_fruits)
# print(tuple_of_fruits)

################################
#
# numbers = "1236547896547."
# print("Is all number", numbers.isalnum())

##################################


