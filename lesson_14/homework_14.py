"""Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал". Створіть об'єкт цього класу,
 представляючи студента. Потім додайте метод до класу "Студент", який дозволяє змінювати середній бал студента.
  Виведіть інформацію про студента та змініть його середній бал."""


class Student:
    def __init__(self, name, surname, age, av_score):
        self.name = name
        self.surname = surname
        self.age = age
        self.av_score = av_score

    def change_av_score(self, new_av_score):
        self.av_score = new_av_score



student_1 = Student("Lina", "Grooth", 22, 89)
print(f"Student {student_1.name} {student_1.surname} (age {student_1.age}) has an average score of {student_1.av_score}")

student_1.change_av_score(95)
print(f"Student {student_1.name} {student_1.surname} (age {student_1.age}) has an average score of {student_1.av_score}")
