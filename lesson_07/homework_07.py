import re

# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""

def delimiter(num):
    print()
    print(f"Task {num}")

delimiter(1)

def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1
    if number >= 1:
        #Complete the while loop condition.
        while multiplier <= 25:
            result = number * multiplier
            if result > 25 or result == 0:
                break
            print(number, "x", multiplier, "=", result)

            # Increment the appropriate variable
            multiplier += 1
    else: 
        print("Not valid number")

multiplication_table(3)

# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""

delimiter(2)

def sum(num_1, num_2):
    print(f"Sum of two numbers {num_1} & {num_2} is {num_1 + num_2}")

sum(2, 5)

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""

delimiter(3)

def aver_list(lst):
    s = 0
    for num in lst:
        s += num
    return s / len(lst)

list_for_count = (1, 2, 3, 4, 5, 6, 7, 8, 9, 12)
res_ever = aver_list(list_for_count)
print(f"The arithmetic mean of the list {list_for_count} is equal to {res_ever}")
# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""

delimiter(4)

def revers_string(str):
    return str[::-1]

string_for_ex = "Kyiv is the capital of Ukraine"
result_revers = revers_string(string_for_ex)
print(f"The result of the reverse string '{string_for_ex}' is '{result_revers}'")

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

delimiter(5)

def longest_word(str):
    return max(str, key=len)

string_for_ex = "Kyiv is the capital of Ukraine"
result_check = longest_word(string_for_ex.split())
print(f"The longest word of the string '{string_for_ex}' is '{result_check}'")

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""

delimiter(6)

def find_substring(str1, str2):
    num_incl = -1
    num_incl = str1.find(str2)
    return num_incl

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
"""Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?"""

delimiter(7)

def total(dist, f_cons):
    return dist/  100 * f_cons

def stop_times(total, t_cap):
    return total / t_cap

distance = 1600
fuel_cons = 9
tank_cap = 48
print(f"{total(distance, fuel_cons)} liters of gasoline will be needed for {distance} km")
print(f"The family needs to stop at a gas station during this trip, filling up a full tank each time at least "
      f"{round(stop_times(total(distance, fuel_cons),tank_cap))}")

# task 8
""" Виведіть кількість слів останнього речення з text.
"""

delimiter(8)

text = """London is the capital and largest city of both England and the United Kingdom, with a population of 8,866,180 
in 2022. The wider metropolitan area is the largest in Western Europe, with a population of 14.9 million. 
London stands on the River Thames in southeast England, at the head of a 50-mile (80 km) estuary down to the North Sea, 
and has been a major settlement for nearly 2,000 years."""

def count_words(ch_text):
    text_sentences = re.split(r'(?<=[.!?])\s+', ch_text)
    return len(text_sentences[len(text_sentences) - 1].split())

print(f"The amount of words in the last sentence in the text is {count_words(text)}")

# task 9
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""

delimiter(9)

def count_pages(total_ph, on_page):
    return round(total_ph / on_page)

total_photos = 232
am_on_page = 8
print("Pages will be needed Igor to paste all the photos", count_pages(total_photos, am_on_page) )

# task 10

""" Виведіть, скільки слів у тексті починається з Великої літери?
"""

delimiter(10)

def am_upper_words(ch_text):
    words_text = ch_text.split()
    count_words_is_upper = 0
    for word in words_text:
        if word[0].isupper():
            count_words_is_upper += 1
    return count_words_is_upper
print(f"The words with the first upper letter are {am_upper_words(text)} times")

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""