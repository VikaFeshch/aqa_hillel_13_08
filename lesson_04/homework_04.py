import re
from itertools import count

from pygments.lexer import words

adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

print()
print("Task 01")
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
print(adwentures_of_tom_sawer)

# task 02 ==
""" Замініть .... на пробіл
"""

print()
print("Task 02")
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")
print(adwentures_of_tom_sawer)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""

print()
print("Task 03")
adwentures_of_tom_sawer = " ".join(adwentures_of_tom_sawer.split())
print(adwentures_of_tom_sawer)


# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""

print()
print("Task 04")
print("The letter 'h' in the text are", adwentures_of_tom_sawer.count("h"), "times")


# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""

print()
print("Task 05")
words_text = adwentures_of_tom_sawer.split()
count_words_is_upper = 0
for word in words_text:
    if word[0].isupper():
        count_words_is_upper += 1
print("The words with the first upper letter are", count_words_is_upper, "times")

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""

print()
print("Task 06")
first_tom = adwentures_of_tom_sawer.find("Tom")
print("The word 'Tom' in the text second time is on the", adwentures_of_tom_sawer.find("Tom", first_tom + len("Tom")))


# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""

print()
print("Task 07")
adwentures_of_tom_sawer_sentences = None
adwentures_of_tom_sawer_sentences = re.split(r'(?<=[.!?])\s+', adwentures_of_tom_sawer)
print(adwentures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""

print()
print("Task 08")
print("The forth sentence is '", adwentures_of_tom_sawer_sentences[3].lower(), "'")

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""

print()
print("Task 09")
if "By the time" in adwentures_of_tom_sawer:
    print('Some sentence begins with "By the time"')

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""

print()
print("Task 10")
count_words_last_sent = len(adwentures_of_tom_sawer_sentences[len(adwentures_of_tom_sawer_sentences)-1].split())
print(f'The last sentence contains {count_words_last_sent} words')
