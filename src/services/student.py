from ..models.student import Student
from ..types.type import StudentDto


def get_students() -> list[Student]:
    students = Student.find()
    return students


def get_student_by_id(id: str) -> Student:
    student = Student.find_one_by_id(id)
    if not student:
        raise Exception("Student Not Found!")
    return student


def create_student(student_dto: StudentDto) -> None:
    student = Student(student_dto)
    student.save()
