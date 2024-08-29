from tabulate import tabulate
from ..services.student import get_students


def view_students() -> None:
    print('List Students:')
    students = get_students()
    headers = students[0].__dict__.keys()
    rows = map(lambda student: student.__dict__.values(), students)

    print(tabulate(rows, headers=headers, tablefmt="grid"))
