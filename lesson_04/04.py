# s = "dkhf. sr    . Hjlkj           ert"
# p = s.find(".",10, )
# print(p)
# s = s[p:]
# print(s)
# HW ext 2
# list1 = ["a.txt", "b.txt", "c.log", "d.html", "e.log", ".diff"]
# str1 = ".txt"
# new_list = []
# for l in list1:
#     print(l)
#     if l.endswith(str1):
#         new_list.append(l)
# print(new_list)
# HW ext 1
# test_string = "2023-04-27 15:30:45 - test PASS"
# p = test_string.find(":", 20, )
# if p != -1:
#     test_string = test_string[p + 2:]
# else: test_string = "No test case name"
# print(test_string)

# HW ext 3

old_value = "800x600"
new_value = "1024x800"
filetext = """\
    screen_size = 800x600
    paralel_processes = 10
    db_conection = localhost:5432"""
filetext = filetext.replace(old_value,new_value)

print(filetext)