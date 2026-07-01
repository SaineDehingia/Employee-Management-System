from pydantic import BaseModel, EmailStr

class Employee(BaseModel):
    employee_id: int
    name: str
    email: EmailStr
    department: str
    designation: str
    salary: float

    
class User(BaseModel):
    username: str
    email: EmailStr
    password: str
    
class LoginRequest(BaseModel):
    username: str
    password: str