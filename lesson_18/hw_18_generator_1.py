def even_numb(start, stop):
    if start % 2 == 0:
        num = start
    else:
        num = start + 1

    while num < stop:
        yield num
        num += 2


gen = (x for x in even_numb(0, 10))

for item in gen:
    print(item)

