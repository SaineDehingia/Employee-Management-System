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
    
class Department(BaseModel):
    department_id: int
    department_name: str
    manager: str
    location: str
    
class Attendance(BaseModel):
    employee_id: int
    date: str
    status: str
    check_in: str
    check_out: str
class Leave(BaseModel):
    employee_id: int
    leave_type: str
    from_date: str
    to_date: str
    reason: str
    status: str