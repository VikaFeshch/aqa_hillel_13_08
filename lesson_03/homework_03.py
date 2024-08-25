alice_in_wonderland = ('"Would you tell me, please, which way I ought to go from here?"\n'
                       '"That depends a good deal on where you want to get to," said the Cat.\n'
                       '"I don\'t much care where ——" said Alice.\n'
                       '"Then it doesn\'t matter which way you go," said the Cat.\n'
                       '"—— so long as I get somewhere," Alice added as an explanation.\n'
                       '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."')
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк
print(alice_in_wonderland)

"""
    # Tasks 04 -10:
    # Translate the tasks from the book "Mathematics, 5th grade"
    # into the python language and output the answer, so that it was
    # understandable to a child studying in the fifth grade
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""

print()
print("Task 4")
area_Bl_S = 436402
area_Az_S = 37800
print("The area of the Black Sea and the Sea of Azov together is", area_Bl_S + area_Az_S, "sq.km.")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""

print()
print("Task 5")
warehouses = 375291
warehouse_3 = warehouses - 250449
warehouse_1 = warehouses - 222950
warehouse_2 = warehouses - warehouse_1 - warehouse_3
print("Amount of goods in the warehouse 1 is", warehouse_1,
      "\n                in the warehouse 2 is", warehouse_2,
      "\n                in the warehouse 3 is", warehouse_3)

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""

print()
print("Task 6")
monthly_payment = 1179
print("The computer costs UAH", monthly_payment * 18)

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""

print()
print("Task 7")
print("Remainder from division")
print(" a)", 8019 % 8," d)", 7248 % 6)
print(" b)", 9907 % 9," e)", 7128 % 5)
print(" c)", 2789 % 5," f)", 19224 % 9)


# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""

print()
print("Task 8")
lists = [(4, 274), (2, 218), (4, 35), (1, 350), (3, 21)]
all=0
for amount, cost in lists:
    all += amount * cost
print("The total cost of the order is UAH", all)


# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""

print()
print("Task 9")
print("Pages will be needed Igor to paste all the photos", round(232 / 8) )

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""

print()
print("Task 10")
total = (1600/100)*9
print("1)", total, "liters of gasoline will be needed for 1600 km")
times = total/48
print("2)", "The family needs to stop at a gas station during this trip, filling up a full tank each time at least", round(times))
