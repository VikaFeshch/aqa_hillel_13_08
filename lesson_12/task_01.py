import pytest


"""

Список містить словники - дані співробітників фірми (прізвище, зарплата і стать).

Скласти функцію, яка повертає тапл:

а) прізвище особи, яка має найбільшу

зарплату (якщо більше одного - перше по алфавіту);

б) розмір найменшої зарплати чоловіків,

в) розмір найвищої зарплати жінок

[

    {"name": "Azimova", "salary": 20000, "gender": "f"},

    {"name": "Borenko", "salary": 9000, "gender": "m"},

    {"name": "Vasilenko", "salary": 10000, "gender": "m"},

    {"name": "Zabolotna", "salary": 25000, "gender": "f"},

    {"name": "Koval", "salary": 35000, "gender": "m"},

]
"""

def selected_staff_for_max_salary(list_of_staff, ch):
    staff_with_max_salary = max(list_of_staff, key=lambda staff: staff['salary'])
    a = staff_with_max_salary['name'], staff_with_max_salary['salary']
    min_salary_of_men = min([staff for staff in list_of_staff if staff['gender'] == 'm'],
                            key=lambda staff: staff['salary'])
    b = min_salary_of_men['salary']
    max_salary_of_women = max([staff for staff in list_of_staff if staff['gender'] == 'f'],
                            key=lambda staff: staff['salary'])
    c = max_salary_of_women['salary']
    if ch == "a":
        return a
    elif ch == "b":
        return b
    elif ch == "c":
        return c
    else:
        return None



def test_max_salary():
    list_of_staff =  [

        {"name": "Azimova", "salary": 20000, "gender": "f"},

        {"name": "Borenko", "salary": 9000, "gender": "m"},

        {"name": "Vasilenko", "salary": 10000, "gender": "m"},

        {"name": "Zabolotna", "salary": 25000, "gender": "f"},

        {"name": "Koval", "salary": 35000, "gender": "m"},

    ]
    exp_result_max_salary = ("Koval", 35000)
    result = selected_staff_for_max_salary(list_of_staff, "a")
    assert result == exp_result_max_salary, f"Expected {exp_result_max_salary}, but got {result}"


def test_man_salary():
    list_of_staff = [

        {"name": "Azimova", "salary": 20000, "gender": "f"},

        {"name": "Borenko", "salary": 9000, "gender": "m"},

        {"name": "Vasilenko", "salary": 10000, "gender": "m"},

        {"name": "Zabolotna", "salary": 25000, "gender": "f"},

        {"name": "Koval", "salary": 35000, "gender": "m"},

    ]
    exp_result_min_salary_of_men = 9000
    result = selected_staff_for_max_salary(list_of_staff, "b")
    assert result == exp_result_min_salary_of_men, f"Expected {exp_result_min_salary_of_men}, but got {result}"


def test_women_salary():
    list_of_staff = [

        {"name": "Azimova", "salary": 20000, "gender": "f"},

        {"name": "Borenko", "salary": 9000, "gender": "m"},

        {"name": "Vasilenko", "salary": 10000, "gender": "m"},

        {"name": "Zabolotna", "salary": 25000, "gender": "f"},

        {"name": "Koval", "salary": 35000, "gender": "m"},

    ]
    exp_result_max_salary_of_women = 25000
    result = selected_staff_for_max_salary(list_of_staff, "c")
    assert result == exp_result_max_salary_of_women, f"Expected {exp_result_max_salary_of_women}, but got {result}"