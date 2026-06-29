from pydantic import BaseModel
from typing import Optional

# What the user sends to CREATE
# StudentCreate - is the schema wants to add a new student
# (name, course, grade, email)- request that must be sent

class StudentCreate(BaseModel):
    name: str
    course: str
    grade: float = 0.0
    email: str


# What the user sends to update
# StudentUpdate - is for when someone wants to change a student details.
# The key difference is, here everything optional. WHY? Because when updating
# The user should be able to send just one field and change only that.

class StudentUpdate(BaseModel):
    name: Optional[str] = None
    course: Optional[str] = None
    grade: Optional[float] = None


# What the API sends back
# StudentResponse is what comes back when someone makes a request
# Notice the StudentResponse includes id (because after we create a student,
# we want to tell the user what id they were assigned to)

class StudentResponse(BaseModel):
    id: int
    name: str
    course: str
    grade: float
    email: str

    class Config:  # special class in pydantic (it holds a configuration setting)
        from_attributes = True  # without this line, pydantic cannot read SQLAlchemy model object