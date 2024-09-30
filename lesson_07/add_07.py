# # addition 1
#
# def solution(grades1, grades2):
#     res_comp = {}
#     for key_1, value_1 in grades1.items():
#         for key_2, value_2 in grades2.items():
#             if key_1 == key_2:
#                 res_comp[key_1] = value_1 - value_2
#     return res_comp
#
# # grades_1 = {'Анна Коваленко': 90, 'Олег Петров': 85, 'Ірина Сидорова': 78}
# # grades_2 = {'Анна Коваленко': 92, 'Олег Петров': 87, 'Ірина Сидорова': 80}
# grades_1 = {'Анна Коваленко': 92, 'Олег Петров': 85, 'Ірина Сидорова': 78, 'Свирид Свиридович': 99}
#
# grades_2 = {'Анна Коваленко': 90, 'Олег Петров': 85, 'Ірина Сидорова': 80}
# print(grades_1.keys())
# for key, value in grades_2.items():
#     print(key, value)
# result = solution(grades_1, grades_2)
# print(result)

# addition 2

def solution(i_d, sep = "."):
    return sep.join(map(str,i_d))

def solution1(*args, sep = "."):
    return sep.join(map(str,args))

inp_date = ('15', '10', '2024')
#print(solution((inp_date)))
print(15, 10, 2024)

i = 11, 22, 2003
#print(solution(i, "/"))
print(123, 11, 22, 2003, sep="/")