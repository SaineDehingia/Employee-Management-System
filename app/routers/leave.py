from fastapi import APIRouter, HTTPException
from app.database import leave_collection, employees_collection
from app.models import Leave
from app.utils.email import send_leave_email

print("LEAVE ROUTER LOADED")

router = APIRouter()


# Apply Leave
@router.post("/leave")
def apply_leave(leave: Leave):

    print(">>> INSIDE APPLY LEAVE", flush=True)

    return {
        "message": "Reached apply_leave"
    }

# Get All Leave Requests
@router.get("/leave")
def get_leave_requests():

    leave_requests = []

    for leave in leave_collection.find():
        leave["_id"] = str(leave["_id"])
        leave_requests.append(leave)

    return leave_requests


# Update Leave
@router.put("/leave/{employee_id}")
def update_leave(employee_id: int, leave: Leave):

    result = leave_collection.update_one(
        {"employee_id": employee_id},
        {"$set": leave.model_dump()}
    )

    if result.matched_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Leave request not found"
        )

    return {
        "message": "Leave request updated successfully"
    }


# Delete Leave
@router.delete("/leave/{employee_id}")
def delete_leave(employee_id: int):

    result = leave_collection.delete_one(
        {"employee_id": employee_id}
    )

    if result.deleted_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Leave request not found"
        )

    return {
        "message": "Leave request deleted successfully"
    }