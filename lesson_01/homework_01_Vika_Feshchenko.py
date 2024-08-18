# task 01 == Fix syntax errors
print("Hello", end = " ")
print("world!")

# task 02 == Fix syntax errors
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03  == Insert the missing variable into the function print
for letter in "Hello world!":
    print(letter)

# task 04 == Make it so that the number of bananas is
# always four times larger than apples
apples = 2
banana = apples * 4

# task 05 == fix the variable names
side_1 = 1
side_2 = 2
side_3 = 3
side_4 = 4

# task 06 == Calculate the perimeter of the figure from task 05
# and print it for the user
perimetery = side_1 + side_2 + side_3 + side_4
print(perimetery)


"""
    # Tasks 07 -10:
    # Translate tasks from the book "Mathematics, 2nd grade"
    # into the Python language and output the answer in a way that
    # would be understandable to a child studying in the second grade
"""
# task 07
"""
4 apple trees were planted in the garden. Pears are 5 more than apple trees, and plums are 2 less.
How many trees were planted in the garden?
"""

apple = 4
pear = apple + 5
plum = apple - 2
all_trees = apple + pear + plum
print("There are", all_trees, "trees in the garden")

# task 08
"""
By noon, the air temperature was 5 degrees above zero.
After lunch, the temperature dropped by 10 degrees.
In the evening it warmed by 4 degrees. What is the temperature at night?
"""

am = 5
pm = am - 10
evn = pm + 4
print("The temperature in the evening was", evn, "degrees")

# task 09
"""
In general, there are 24 boys in the theater group, and half as many girls.
1 boy got sick and 2 girls didn't come today.
How many children are there in the theater group today?
"""

boys = 24
girls = 24//2
child_today = boys - 1 + girls - 2
print("Today there are", child_today,"children in the theater group")

# task 10
"""
The first book costs UAH 8, the second - UAH 2. more expensive
and the third - as half the cost of the first and second together.
How much will all the books cost if you buy one copy each?
"""
cost_book_1 = 8
cost_book_2 = cost_book_1 + 2
cost_book_3 = (cost_book_1 + cost_book_2) / 2
print("If you buy books one copy at a time, the purchase price will be", cost_book_1 + cost_book_2 + cost_book_3, "uah")