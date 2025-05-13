from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db import SessionLocal
import random
from faker import Faker
from models import Student, Group, Teacher, Subject, Grade


db = SessionLocal()
fake = Faker()


def make_groups():
    names = ["Group One", "Group Two", "Group Three"]
    groups = []
    for name in names:
        group = Group(name=name)
        groups.append(group)
    db.add_all(groups)
    db.commit()
    return groups


def make_students(groups):
    students = []
    for i in range(50):
        group = random.choice(groups)
        student = Student(name=fake.name(), group=group)
        db.add(student)
        students.append(student)
    db.commit()
    return students


def make_teachers():
    teachers = []
    for i in range(4):
        teacher = Teacher(name=fake.name())
        db.add(teacher)
        teachers.append(teacher)
    db.commit()
    return teachers


def make_subjects(teachers):
    subjects = []
    names = [
        "Алгебра",
        "Геометрія",
        "Мат. аналіз",
        "Історія",
        "Малювання",
        "Основи алгоритмів",
        "Англійська мова",
    ]
    for name in names:
        teacher = random.choice(teachers)
        subject = Subject(name=name, teacher=teacher)
        db.add(subject)
        subjects.append(subject)
    db.commit()
    return subjects


def make_grades(students, subjects):
    for subject in subjects:
        for student in students:
            for i in range(random.randint(15, 20)):
                grade = Grade(
                    student=student,
                    subject=subject,
                    grade=random.randint(60, 100),
                    date=fake.date_between(start_date="-1y", end_date="today"),
                )
                db.add(grade)
    db.commit()


def seed_db():
    try:
        groups = make_groups()
        students = make_students(groups)
        teachers = make_teachers()
        subjects = make_subjects(teachers)
        make_grades(students, subjects)
        db.commit()
        print("Database was seeded.")
    except Exception as e:
        print(f"Something went wrong: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    seed_db()
    db.close()
