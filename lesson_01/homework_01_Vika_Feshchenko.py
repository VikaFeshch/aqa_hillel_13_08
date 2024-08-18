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

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimetery = side_1 + side_2 + side_3 + side_4
print(perimetery)


"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""

apple = 4
pear = apple + 5
plum = apple - 2
all_trees = apple + pear + plum
print("There are", all_trees, "trees in the garden")

# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""

am = 5
pm = am - 10
evn = pm + 4
print("The temperature in the evening was", evn, "degrees")

# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""

boys = 24
girls = 24//2
child_today = boys - 1 + girls - 2
print("Today there are", child_today,"children in the theater group")

# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
cost_book_1 = 8
cost_book_2 = cost_book_1 + 2
cost_book_3 = (cost_book_1 + cost_book_2) / 2
print("If you buy books one copy at a time, the purchase price will be", cost_book_1 + cost_book_2 + cost_book_3, "uah")