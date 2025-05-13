from sqlalchemy.orm import Session
from sqlalchemy import func, desc, select
from db import SessionLocal
from models import Student, Group, Teacher, Subject, Grade


db = SessionLocal()


def select_1(n=5):
    result = (
        db.query(Student.name, func.round(func.avg(Grade.grade), 3).label("avg"))
        .join(Grade)
        .group_by(Student.id)
        .order_by(desc("avg"))
        .limit(n)
        .all()
    )
    print(f"\n(1) - {n} студентів із найвищим середнім балом:")
    for res in result:
        print(f" • {res[0]} - {res[1]}")
    return result


def select_2(i=1):
    subj = db.query(Subject.name).filter(Subject.id == i).scalar()
    result = (
        db.query(Student.name, func.round(func.avg(Grade.grade), 3).label("avg"))
        .join(Grade)
        .filter(Grade.subject_id == i)
        .group_by(Student.id)
        .order_by(desc("avg"))
        .first()
    )
    print(
        f"\n(2) - Студент із найвищим середнім балом з предмету '{subj}' - {result[0]}: {result[1]}"
    )
    return result


def select_3(i=1):
    subj = db.query(Subject.name).filter(Subject.id == i).scalar()
    result = (
        db.query(Group.name, func.round(func.avg(Grade.grade), 3))
        .select_from(Grade)
        .join(Student, Student.id == Grade.student_id)
        .join(Group, Group.id == Student.group_id)
        .join(Subject, Subject.id == Grade.subject_id)
        .filter(Subject.id == i)
        .group_by(Group.id)
        .all()
    )
    print(f"\n(3) - Середній бал у групах з предмету '{subj}':")
    for res in result:
        print(f" • {res[0]} - {res[1]}")
    return result


def select_4():
    result = db.query(func.round(func.avg(Grade.grade), 3)).scalar()
    print(f"\n(4) - Середній бал на потоці (по всій таблиці оцінок): {result}")
    return result


def select_5(i=1):
    tutor = db.query(Teacher.name).filter(Teacher.id == i).scalar()
    result = db.query(Subject.name).filter(Subject.teacher_id == i).all()
    print(f"\n(5) - Курси, які читає викладач '{tutor}':")
    for res in result:
        print(f" • {res[0]}")
    return result


def select_6(i=1):
    group = db.query(Group.name).filter(Group.id == i).scalar()
    result = db.query(Student.name).filter(Student.group_id == i).all()
    print(f"\n(6) - Список студентів у групі '{group}':")
    for res in result:
        print(f" • {res[0]}")
    return result


def select_7(i=1, j=1):
    group = db.query(Group.name).filter(Group.id == i).scalar()
    subj = db.query(Subject.name).filter(Subject.id == j).scalar()
    result = (
        db.query(Student.name, Grade.grade)
        .join(Grade)
        .filter(Student.group_id == i, Grade.subject_id == j)
        .all()
    )
    print(f"\n(7) - Оцінки студентів у групі '{group}' з предмету '{subj}':")
    for res in result:
        print(f" • {res[0]} - {res[1]}")
    return result


def select_8(i=1):
    tutor = db.query(Teacher.name).filter(Teacher.id == i).scalar()
    result = (
        db.query(func.round(func.avg(Grade.grade), 3))
        .join(Subject)
        .filter(Subject.teacher_id == i)
        .scalar()
    )
    print(f"\n(8) - Середній бал, який ставить викладач '{tutor}': {result}")
    return result


def select_9(i=1):
    stud = db.query(Student.name).filter(Student.id == i).scalar()
    result = (
        db.query(Subject.name)
        .join(Grade)
        .filter(Grade.student_id == i)
        .group_by(Subject.id)
        .all()
    )
    print(f"\n(9) - Список курсів, які відвідує студент '{stud}':")
    for res in result:
        print(f" • {res[0]}")
    return result


def select_10(i=1, j=1):
    stud = db.query(Student.name).filter(Student.id == i).scalar()
    tutor = db.query(Teacher.name).filter(Teacher.id == j).scalar()
    result = (
        db.query(Subject.name)
        .join(Grade)
        .filter(
            Grade.student_id == i,
            Subject.teacher_id == j,
            Grade.subject_id == Subject.id,
        )
        .group_by(Subject.id)
        .all()
    )
    print(f"\n(10) - Список курсів, які читає студенту '{stud}' викладач '{tutor}':")
    for res in result:
        print(f" • {res[0]}")
    return result


if __name__ == "__main__":
    """Знайти 5 студентів із найбільшим середнім балом з усіх предметів."""
    select_1(5)

    """Знайти студента із найвищим середнім балом з певного предмета."""
    select_2(5)

    """Знайти середній бал у групах з певного предмета."""
    select_3(2)

    """Знайти середній бал на потоці (по всій таблиці оцінок)."""
    select_4()

    """Знайти які курси читає певний викладач."""
    select_5(4)

    """Знайти список студентів у певній групі."""
    select_6(2)

    """Знайти оцінки студентів у окремій групі з певного предмета."""
    select_7(1, 2)

    """Знайти середній бал, який ставить певний викладач зі своїх предметів."""
    select_8(2)

    """Знайти список курсів, які відвідує певний студент."""
    select_9(13)

    """Список курсів, які певному студенту читає певний викладач."""
    select_10(13, 2)

    print()
