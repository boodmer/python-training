
from .base import IBaseModel
from ..utils.db_util import execute_query, execute_command
from ..types.type import StudentDto


class Student(IBaseModel):
    table_name = 'public.student'

    def __init__(self, student: StudentDto):
        self.id = student['id']
        self.name = student['name']
        self.email = student['email']
        self.created_at = student['created_at']
        self.updated_at = student['updated_at']

    def __repr__(self):
        return f"id: {self.id}, name: '{self.name}', email: '{self.email}'"

    @classmethod
    def find_one_by_id(cls, id: str):
        rows = execute_query(
            f'select * from {cls.table_name} where id = %s limit 1', (id,))

        if not len(rows):
            return None

        row = rows[0]
        return cls({'id': row[0], 'name': row[1], 'email': row[2], 'created_at': row[3], 'updated_at': row[4]})

    @classmethod
    def find(cls):
        rows = execute_query(f'select * from {cls.table_name}')
        students: list[Student] = list(map(lambda row: Student(
            {'id': row[0], 'name': row[1], 'email': row[2], 'created_at': row[3], 'updated_at': row[4]}), rows))
        return students

    def save(self):
        execute_command(f"""insert into {
            self.table_name}(id, name, email) values (%s, %s, %s)""", (self.id, self.name, self.email))
