from src.utils.db_util import execute_query, execute_command
from src.models.student import Student, table_name


def get_students() -> list[Student]:
    rows = execute_query(f'select * from {table_name}')
    students: list[Student] = list(map(lambda row: Student(row), rows))
    # students = []
    # for row in rows:
    #     student = Student(row)
    #     students.append(student)

    return students


def get_student_by_id(id: int) -> Student:
    row = execute_query(f'select * from {table_name} where id = %s', (id,))
    return Student(row[0])


def create_student(student: Student) -> None:
    execute_command(f"""insert into {
                    table_name}(id, name, email) values (%s, %s, %s)""", (student.id, student.name, student.email))
