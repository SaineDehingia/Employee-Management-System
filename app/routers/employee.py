from fastapi import APIRouter, Depends, HTTPException

from app.models import Employee
from app.database import employees_collection
from app.dependencies import get_current_user

router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)


@router.post("/")
def add_employee(
    employee: Employee,
    current_user: str = Depends(get_current_user)
):

    employee_dict = employee.model_dump()

    employees_collection.insert_one(employee_dict)

    return {
        "message": "Employee Added Successfully"
    }


@router.get("/")
def get_all_employees(
    current_user: str = Depends(get_current_user)
):

    employees = []

    for employee in employees_collection.find():
        employee["_id"] = str(employee["_id"])
        employees.append(employee)

    return employees


@router.put("/{employee_id}")
def update_employee(
    employee_id: int,
    employee: Employee,
    current_user: str = Depends(get_current_user)
):

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


@router.delete("/{employee_id}")
def delete_employee(
    employee_id: int,
    current_user: str = Depends(get_current_user)
):

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