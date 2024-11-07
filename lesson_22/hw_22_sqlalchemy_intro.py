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

#####################################################################################

# # Query about all students with the courses
# def query_about_all():
#     results = (
#         session.query(
#             Student.name.label("student"),
#             func.array_agg(Courses.name).label("courses")
#         )
#         .join(student_course, Student.id == student_course.c.student_id)
#         .join(Courses, student_course.c.course_id == Courses.id)
#         .group_by(Student.id)
#         .all()
#     )
#
#     for result in results:
#         print(f"Student: {result.student}, Courses: {', '.join(result.courses)}")
#


# # Add new student
# def add_new_student(name, age, course_numbers):
#     selected_courses = session.query(Courses).filter(Courses.id.in_(course_numbers)).all()
#
#     new_student = Student(name=name, age=age, courses=selected_courses)
#     session.add(new_student)
#     session.commit()
#
#     print(f"Student {name} was added with courses: {', '.join(course.name for course in selected_courses)}")
#
#
# # Add new course
# def add_new_course(name):
#     new_course = Courses(name=name)
#     session.add(new_course)
#     session.commit()
#
#     print(f"Course {name} was added")
#
#

# # Query about a specific student with courses
# def query_ab_one_student(name):
#     results = (
#         session.query(Student.name.label("student"), Courses.name.label("course"))
#         .join(student_course, Student.id == student_course.c.student_id)
#         .join(Courses, student_course.c.course_id == Courses.id)
#         .filter(Student.name == name)
#         .all()
#     )
#
#     if results:
#         courses = [result.course for result in results]
#         print(f"Student: {results[0].student}, Courses: {', '.join(courses)}")

# # Query about all students for a specific course
# def query_ab_all_st_for_c(course_name):
#     results = (
#         session.query(
#             Courses.name.label("course"),
#             func.array_agg(Student.name).label("students")
#         )
#         .join(student_course, Courses.id == student_course.c.course_id)
#         .join(Student, student_course.c.student_id == Student.id)
#         .filter(Courses.name == course_name)
#         .group_by(Courses.id)
#         .first()
#     )
#
#     if results:
#         print(f"Course: {results.course} has students: {', '.join(results.students)}")
#     else:
#         print(f"No students found for course '{course_name}'.")
#
# # Update information about student
# def update_student(name, course_ids):
#     student_to_update = session.query(Student).filter(Student.name == name).first()
#     if student_to_update:
#         selected_courses = session.query(Courses).filter(Courses.id.in_(course_ids)).all()
#         student_to_update.courses = selected_courses
#         session.commit()
#
#         print(f"Student {name} was updated with courses: {', '.join(course.name for course in selected_courses)}")
#     else:
#         print(f"Student with name '{name}' wasn't found")
#

# # Delete information about student
# def delete_student(name):
#     student_to_delete = session.query(Student).filter(Student.name == name).first()
#     if student_to_delete:
#         session.delete(student_to_delete)
#         session.commit()
#         print(f"Student {name} was deleted")
#     else:
#         print(f"Student {name} not found and could not be deleted")

# # Delete information about course
# def delete_course(course_id):
#     course_to_delete = session.query(Courses).filter(Courses.id == course_id).first()
#     if course_to_delete:
#         session.delete(course_to_delete)
#         session.commit()
#         print(f"Course {course_to_delete.name} was deleted")
#     else:
#         print(f"Course with id {course_id} wasn't found")

# ###########################################################################################################
#
# Query about all students with the courses
# query_about_all()

# # Add new student
# name = "Gregory"
# age = 25
# course_ids = [1, 3, 5]
# add_new_student(name, age, course_ids)

# # Add new course
# name = "Postman Advanced: REST API"
# add_new_course(name)
#
# # Query about a specific student with courses
# name = "Bob"
# query_ab_one_student(name)

# # Query about all students for a specific course
# name = "QA Automation Java"
# query_ab_all_st_for_c(name)

# # Update information about student
# name = "Bob"
# course_ids = [1, 3, 6]
# update_student(name, course_ids)

# # Delete information about student
# name = "Gregory"
# delete_student(name)

# # Delete information about course
# course_id = 6
# delete_course(course_id)
#

