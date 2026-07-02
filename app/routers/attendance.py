from fastapi import APIRouter, HTTPException
from app.database import attendance_collection, employees_collection
from app.models import Attendance

router = APIRouter()

@router.post("/attendance")
def mark_attendance(attendance: Attendance):

    # Check if employee exists
    employee = employees_collection.find_one(
        {"employee_id": attendance.employee_id}
    )

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    attendance_dict = attendance.model_dump()

    attendance_collection.insert_one(attendance_dict)

    return {
        "message": "Attendance marked successfully"
    }
    
@router.get("/attendance")
def get_attendance():

    attendance = []

    for record in attendance_collection.find():
        record["_id"] = str(record["_id"])
        attendance.append(record)

    return attendance

@router.put("/attendance/{employee_id}")
def update_attendance(employee_id: int, attendance: Attendance):

    result = attendance_collection.update_one(
        {"employee_id": employee_id},
        {"$set": attendance.model_dump()}
    )

    if result.matched_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Attendance record not found"
        )

    return {
        "message": "Attendance updated successfully"
    }

@router.delete("/attendance/{employee_id}")
def delete_attendance(employee_id: int):

    result = attendance_collection.delete_one(
        {"employee_id": employee_id}
    )

    if result.deleted_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Attendance record not found"
        )

    return {
        "message": "Attendance deleted successfully"
    }