from sqlalchemy import create_engine, Table, Column, Integer, String, ForeignKey, select, func
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

DATABASE_URL = "postgresql+psycopg2://feshv:3221@localhost/manage_students"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

student_course = Table(
    'student_course', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id', ondelete="CASCADE"), primary_key=True),
    Column('course_id', Integer, ForeignKey('courses.id', ondelete="CASCADE"), primary_key=True)
)


class Courses(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(200))
    students = relationship('Student',  secondary=student_course, back_populates="courses")

    def __repr__(self):
        return f"Courses(name={self.name}, id={self.id}"


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(200))
    age = Column(Integer)
    # course_id = Column(Integer, ForeignKey("courses.id", ondelete='SET NULL'))
    courses = relationship('Courses',secondary=student_course, back_populates="students")

    def __repr__(self):
        return f"Student(name={self.name}, age={self.age})"

# Base.metadata.create_all(engine)
#
# course_1 = Courses(name = "Python Pro")
# course_2 = Courses(name = "QA Automation Python")
# course_3 = Courses(name = "QA Automation Java")
# course_4 = Courses(name = "ISTQB certification for QA")
# course_5 = Courses(name = "QA Technical Pro")
#
# session.add_all([course_1, course_2, course_3, course_4, course_5])
# session.commit()
#
# students_data = [
#     {"name": "Alice", "age": 20, "courses": [course_1, course_2]},
#     {"name": "Bob", "age": 22, "courses": [course_3]},
#     {"name": "Nick", "age": 25, "courses": [course_1, course_3]},
#     {"name": "Rocky", "age": 20, "courses": [course_2]},
#     {"name": "Will", "age": 21, "courses": [course_5, course_1]},
#     {"name": "Dock", "age": 22, "courses": [course_4]},
#     {"name": "Mick", "age": 18, "courses": [course_1, course_2]},
#     {"name": "Poll", "age": 21, "courses": [course_2]},
#     {"name": "Joy", "age": 22, "courses": [course_1, course_4]},
#     {"name": "Toy", "age": 29, "courses": [course_5]},
#     {"name": "Ron", "age": 21, "courses": [course_2, course_3]},
#     {"name": "Lili", "age": 23, "courses": [course_1]},
#     {"name": "Ana", "age": 25, "courses": [course_1, course_2]},
#     {"name": "Jorg", "age": 19, "courses": [course_5]},
#     {"name": "Luck", "age": 25, "courses": [course_3, course_4]},
#     {"name": "Rob", "age": 28, "courses": [course_1]},
#     {"name": "Tom", "age": 26, "courses": [course_2, course_4]},
#     {"name": "Born", "age": 24, "courses": [course_3]},
#     {"name": "Jack", "age": 22, "courses": [course_1, course_5]},
#     {"name": "Bona", "age": 23, "courses": [course_4]}
# ]
#
# students = [Student(name=data["name"], age=data["age"], courses=data["courses"]) for data in students_data]
#
# session.add_all(students)
# session.commit()

# Query about all students with the courses
def query_about_all():
    query = (
        select(Student.name, func.array_agg(Courses.name).label("courses"))
        .select_from(Student)
        .join(student_course)
        .join(Courses)
        .group_by(Student.id)
    )

    results = session.execute(query).fetchall()

    for student in results:
        print(f"Student: {student.name}, Courses: {', '.join(student.courses)}")

# Add new student
def add_new_student(name, age, course_input):
    # Розділяємо введені курси по комі та видаляємо пробіли
    # course_numbers = [num.strip() for num in course_input.split(',')]
    selected_courses = []

    for num in course_input:
        try:
            index = int(num) - 1  # Конвертуємо номер в індекс
            course = session.get(Courses, index + 1)  # Отримуємо курс за ID
            if course:
                selected_courses.append(course)
            else:
                print(f"Курс з номером {num} не знайдено.")
        except ValueError:
            print(f"Неправильний номер курсу: {num}. Будь ласка, введіть дійсні номери.")
            return  # Виходимо, якщо стався виняток

            # Створюємо нового студента
        new_student = Student(name=name, age=age, courses=selected_courses)

        # Додаємо студента в сесію та комітимо
        session.add(new_student)
        session.commit()

        print(f"Студента {name} додано з курсами: {', '.join(course.name for course in selected_courses)}")


# Query about a specific student in a specific course
def query_ab_one_student():
    pass

# Query about all courses for a specific student
def query_ab_all_courses_for_st():
    pass

# Update information about student
def update_student():
    pass

# Update information about course
def update_course():
    pass

# Delete information about student
def delete_student():
    pass

# Update information about course
def delete_course():
    pass


def what_do_you_want_to_do():
    print('1 - Query about all students with the courses\n'
          '2 - Add new student\n'
          '3 - Query about a specific student in a specific course\n'
          '4 - Query about all courses for a specific student\n'
          '5 - Update information about student\n'
          '6 - Update information about course\n'
          '7 - Delete information about student\n'
          '8 - Delete information about course\n')

    act = input("What do you want to do? ")

    if act == '1':
        query_about_all()
    elif act == '2':
        name = input('Input student name: ')
        age = input('Input student age: ')
        course_input = input('Input course numbers (comma separated): ')
        course_numbers = course_input.split(',')
        print(course_numbers)
        add_new_student(name, age, course_numbers)

    elif act == '3':
        query_ab_one_student()
    elif act == '4':
        query_ab_all_courses_for_st()
    elif act == '5':
        update_student()
    elif act == '6':
        update_course()
    elif act == '7':
        delete_student()
    elif act == '8':
        delete_course()
    else:
        print("Invalid option selected. Please try again.")


what_do_you_want_to_do()

