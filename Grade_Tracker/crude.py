from sqlalchemy.orm import session
import models, schemas

def create_student(db:session, student: schemasCreate):
    db_student = models.student(**student.model_dump())
    db.add(db_student) #sage the record. Tells SQLAlchemy "I want to save this"
    db.commit() # save to disk . This when data is actually written to database
    db.refresh(db_student) # relpoads the object from databse after saving ,(new id)
    return db_student # return completed student object

# Read one record
def get_student(db: session, student_id: int ):
    return db.query (models.student).filter(models.student_id == student_id)

# read all records
def get_students(db: session):
    return db.query (models.student).all()

# UPDATE a record 
def update_student(db: session, student_id: int, data: schemas.StudentUpdate):
    student = db.query(models.student).filter(models.student.id == student_id).first()
    if not student:
        return None
    
    updates = data.model_dump(exclude_unset=True)
    for field, value in updates.items():
        setattr(student, field, value)

    db.commit()
    db.refresh(student)
    return student

#delete or remove a reccord

def delete_student(db: session, student_id: int):
    student = db.query(models.student).filter(models.student.id == student_id)
    if not student:
        return None
    db.delete(student)
    # save the deletion to disk
    db.commit()
    return student