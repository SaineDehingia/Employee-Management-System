from fastapi import APIRouter
from app.database import (
    employees_collection,
    departments_collection,
    attendance_collection,
    leave_collection
)

router = APIRouter()

@router.get("/dashboard")
def get_dashboard():

    total_employees = employees_collection.count_documents({})
    total_departments = departments_collection.count_documents({})
    total_attendance = attendance_collection.count_documents({})
    total_leave_requests = leave_collection.count_documents({})

    return {
        "total_employees": total_employees,
        "total_departments": total_departments,
        "total_attendance_records": total_attendance,
        "total_leave_requests": total_leave_requests
    }