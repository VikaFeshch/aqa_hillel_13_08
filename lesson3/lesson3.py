# name = "John"
# name1 = 'John'
# name2 = """
# SELECT * FROM users
# WHERE name = "John"
# ORDER BY id DESC
# """
#
# command = """
# find / -name "*.log; grep - r 'erroe' /var/log
# """
#
# print("Division ", 10/3)
# number = 10/3
# print("Division with round ", round(number))
# print("Division with round 2 ", round(number,2))
# print(f"Division with round 3: {number:.4f} ")
#
# int_number = int(10/3) # int / int = float
# print(type(int_number)) # int

##################################
# ==

# 1. compare values
# 2. compare data type
# 3. compare memory address

# a = 10
# b = 10
# print("a == b", a == b)

# print(10 == '10')

# == vs is
# 1. compare memory address
#
# a = 10000
# b = 10000
# print(a is b)

# list1 = [1, 2, 3]
# list2 = list1
# list3 = [1, 2, 3]
# print("Lists comparison1: ", list1 == list2)
# print("Lists comparison2: ", list1 == list3)
# print("Lists comparison3: ", list1 is list2)
# print("Lists comparison4: ", list1 is list3)
#
# some = None
# print(some is None)
# some = 10
# print("Some is not 10", some !=10)


# a == 2
# a = a + 2
# a += 2
# b = 10
# b = b - 2
# b -= 2
# b /= 2
# b *= 2
#
# # and, or, not
#
# #and
# a = 0 # False
# b = 1 # True
# print("False and False", False and False)
# print("True and False", True and False)
# print("False and True", False and True)
# print("True and True", True and True)
#
# # or
# a = 0 # False
# b = 1 # True
# print("False or False", False or False)
# print("True or False", True or False)
# print("False or True", False or True)
# print("True or True", True or True)
#
# # not
# print(not True)
# print(not False)

# # int and float
# print(10 == 10)
# print(10 == 10.0)
# print(10 == [10])

# ціле_число = 42
# восьмеричне_число = 0o52
# шістнадцяткове_число = 0x2A
# двійкове_число = 0b101010
# print(hex(10000))
# print(bin(10000))
# print(oct(10000))

########################################
# # Sequences: list, str, tuple
# sentence = "London is the capital of GB"
# print(sentence[0])
# print(sentence[5])
# print(sentence[-1])
# # slices
# print(sentence[:5]) # [0:5)
# print(sentence[5:15])
# print(sentence[15:])
# #print(sentence[start:end:step])
# print(sentence[0:20:2])
#
# print("len ",len(sentence))
# print("index L", sentence.index('L'))
# print("Count o ", sentence.count('o'))
#
# prices = [23.2, 13, 455]
# print(prices[:2])
#
# not_updatable_prices = (121, 154, 364)
# print(not_updatable_prices[0])
# print(not_updatable_prices[:2])
#
# #################
# # Sequences: set
# numbers = {1, 2, 3, 4}
# print(type(numbers))
# print(len(numbers))

# # #################
# # # Sequences: None
# a = None
# print(a)
# print(a is None)
# print(a is not None)
# print(bool(a)) # a -> bool
#
# #falsy values
# print(bool(""))
# print(bool([]))
#
# prices = [23.2, 13, 455]
# print(min(prices), max(prices))

################################

# input/output

name = input("Enter your name ")
print(f"Hello {name}")
age = int(input("Enter your age "))
age += 1
print(f"My age {age}")
