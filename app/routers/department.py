from fastapi import APIRouter, HTTPException
from app.database import departments_collection
from app.models import Department

router = APIRouter()


# Create Department
@router.post("/departments")
def add_department(department: Department):

    department_dict = department.model_dump()

    departments_collection.insert_one(department_dict)

    return {
        "message": "Department Added Successfully"
    }


# Get All Departments
@router.get("/departments")
def get_all_departments():

    departments = []

    for department in departments_collection.find():
        department["_id"] = str(department["_id"])
        departments.append(department)

    return departments


# Update Department
@router.put("/departments/{department_id}")
def update_department(department_id: int, department: Department):

    result = departments_collection.update_one(
        {"department_id": department_id},
        {"$set": department.model_dump()}
    )

    if result.matched_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Department not found"
        )

    return {
        "message": "Department updated successfully"
    }


# Delete Department
@router.delete("/departments/{department_id}")
def delete_department(department_id: int):

    result = departments_collection.delete_one(
        {"department_id": department_id}
    )

    if result.deleted_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Department not found"
        )

    return {
        "message": "Department deleted successfully"
    }