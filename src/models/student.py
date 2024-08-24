
table_name = 'public.student'


class Student:
    def __init__(self, student: tuple):
        self.id = student[0]
        self.name = student[1]
        self.email = student[2]

    def __repr__(self):
        return f"id: {self.id}, name: '{self.name}', email: '{self.email}'"
