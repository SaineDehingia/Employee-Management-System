from fastapi import APIRouter, HTTPException
from app.models import User, LoginRequest
from app.database import users_collection
from app.security import (
    hash_password,
    verify_password,
    create_access_token,
)

router = APIRouter()


@router.post("/register")
def register(user: User):

    existing_user = users_collection.find_one(
        {"username": user.username}
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )

    user_dict = user.model_dump()

    user_dict["password"] = hash_password(user.password)

    users_collection.insert_one(user_dict)

    return {
        "message": "User Registered Successfully"
    }


@router.post("/login")
def login(login_data: LoginRequest):

    user = users_collection.find_one(
        {"username": login_data.username}
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    if not verify_password(
        login_data.password,
        user["password"]
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    access_token = create_access_token(
        {
            "sub": user["username"]
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }