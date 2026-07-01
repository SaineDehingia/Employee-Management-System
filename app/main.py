from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from app.routers.auth import router as auth_router
from app.routers.employee import router as employee_router

app = FastAPI(
    title="Employee Management System",
    version="1.0.0"
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")



app = FastAPI(
    title="Employee Management System",
    version="1.0.0"
)

app.include_router(auth_router)
app.include_router(employee_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to Employee Management System"
    }
    
from app.database import users_collection

@app.get("/users")
def get_users():

    users = []

    for user in users_collection.find():
        user["_id"] = str(user["_id"])
        users.append(user)

    return users