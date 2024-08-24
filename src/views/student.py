from src.services.student import get_students


def view_students() -> None:
    print('List Students:')
    students = get_students()
    for student in students:
        print(' - ', end='')
        print(student)
