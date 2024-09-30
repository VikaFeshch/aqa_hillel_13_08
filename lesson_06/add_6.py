# addition 1
#
# income = float(input("enter your income "))
# tax_amount = 0
# if income < 10000:
#     tax_amount = income * 10 / 100
# elif income >= 10000 and income <= 50000:
#     tax_amount = income * 15 / 100
# else: tax_amount = income * 20 / 100
# print(tax_amount)

#addition 2

number = int(input("enter your number "))
conter_div = 0
if number < 2:
    print("error number")
elif number == 2:
    print("simple number")
else:
    for i in range(2, number):
        if number % i == 0:
            conter_div += 1
            break
    if conter_div == 0:
        print("simple number")
    else: print("difficult number")

