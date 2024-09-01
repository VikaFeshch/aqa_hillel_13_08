numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sum_even_numbers = 0

for num in numbers:
    if num % 2 == 0:
        sum_even_numbers = sum_even_numbers + num

print("The sum of even numbers:", sum_even_numbers)
