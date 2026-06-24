from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

students = []

class Student(BaseModel):
    name: str
    age: int
    course: str
    is_sponsored: bool = False


@app.post("/students")
def create_student(student: Student):
    students.append(student)
    return {
        "message": "Student added successfully",
        "data": student
    }


@app.get("/stucents")
def get_all_students():
    return students

@app.get("/students/{students_id}")
def get_student(studet_id:int):
    return students[studet_id]

# update - changing existing record
@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: Student):
    students[student_id] = update_student
    return {"message": "sudend updated successfully", "data": updated_student}
    

# Delete or renmoving arequest 
@ app.delete("/atudents/{student_id}")
def delete_student(student_id: int):
    removed = students.pop(student_id)
    return {"message": "student removed", "data": removed}

