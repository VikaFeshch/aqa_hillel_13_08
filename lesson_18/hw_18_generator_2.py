def even_numb(stop):
    num1 = 0
    num2 = 1
    while num1 <= stop:
        yield num1
        num1, num2 = num2, num1 + num2


gen = (x for x in even_numb(10))

for item in gen:
    print(item)

