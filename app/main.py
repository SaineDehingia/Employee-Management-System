from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.routers.auth import router as auth_router
from app.routers.employee import router as employee_router
from app.database import users_collection
from app.routers.upload import router as upload_router
from app.routers.department import router as department_router
from app.routers.attendance import router as attendance_router
from app.routers.leave import router as leave_router
from app.routers.dashboard import router as dashboard_router

app = FastAPI(
    title="Employee Management System",
    version="1.0.0"
)

# Static Files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Templates
templates = Jinja2Templates(directory="app/templates")

# Routers
app.include_router(auth_router)
app.include_router(employee_router)
app.include_router(upload_router)
app.include_router(department_router)
app.include_router(attendance_router)
app.include_router(leave_router)
app.include_router(dashboard_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to Employee Management System"
    }


# Temporary endpoint for testing users
@app.get("/users")
def get_users():

    users = []

    for user in users_collection.find():
        user["_id"] = str(user["_id"])
        users.append(user)

    return users