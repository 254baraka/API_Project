from pydantic import BaseModel
from typing import Optional

# What the user sends to CREATE
# srudentCreate - is the schema wants to add a nesw student
# (name, couurse, grade, email)- request that must be send

class studentCreate(BaseModel):
    name: str
    course: str
    grade: float = 0.0
    email: str

# What the user sends to update
# studentsUpdate - is for when someonme wants to change a student details.
# The key difference is, here everything optional . WHY? Because  when updating
#The user should be able to send just one filed and change only that.

class studentUpdate(BaseModel):
    name: Optional[str] = None
    course: Optional[str] = None    
    grade: Optional[float] = None

# What the API sends back
# student Reasponse is what comes back when someone makes a request
#  notice the studentResponse includes ( because after we create a student , we want to 
# tell the usser what id theynwere assinged to)
class StudentResponse(BaseModel):
    id: int
    name: str
    course: str
    grade: float
    email: str

    class config: # special class in pydantic (it holds a configuration setting)
        from_attributes = True # without this line . pydantic cannot read SQLAlchemy model object
        