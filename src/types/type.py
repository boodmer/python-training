from datetime import datetime
from typing import TypedDict


class StudentDto(TypedDict):
    id: str
    name: str
    email: str
    created_at: datetime
    updated_at: datetime
