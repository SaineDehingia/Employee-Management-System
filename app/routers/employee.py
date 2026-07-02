from fastapi import APIRouter, Query, HTTPException
from app.database import employees_collection
from app.models import Employee

router = APIRouter()


# Create Employee
@router.post("/employees")
def add_employee(employee: Employee):

    employee_dict = employee.model_dump()

    employees_collection.insert_one(employee_dict)

    return {
        "message": "Employee Added Successfully"
    }


# Get Employees with Pagination
from fastapi import Query

@router.get("/employees")
def get_all_employees(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1),
    search: str = Query(None)
):
    skip = (page - 1) * limit

    query = {}

    if search:
        query = {
            "$or": [
                {"name": {"$regex": search, "$options": "i"}},
                {"department": {"$regex": search, "$options": "i"}},
                {"designation": {"$regex": search, "$options": "i"}},
                {"email": {"$regex": search, "$options": "i"}}
            ]
        }

    employees = []

    cursor = employees_collection.find(query).skip(skip).limit(limit)

    for employee in cursor:
        employee["_id"] = str(employee["_id"])
        employees.append(employee)

    return employees

# Update Employee
@router.put("/employees/{employee_id}")
def update_employee(employee_id: int, employee: Employee):

    result = employees_collection.update_one(
        {"employee_id": employee_id},
        {"$set": employee.model_dump()}
    )

    if result.matched_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return {
        "message": "Employee updated successfully"
    }


# Delete Employee
@router.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):

    result = employees_collection.delete_one(
        {"employee_id": employee_id}
    )

    if result.deleted_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return {
        "message": "Employee deleted successfully"
    }