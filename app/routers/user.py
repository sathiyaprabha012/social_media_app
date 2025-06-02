import app
from fastapi import APIRouter, Depends, FastAPI, HTTPException, Response , status
from app import models
from app.schemas import UserCreate, UserOut
from app.database import SessionLocal, engine , get_db
from sqlalchemy.orm import Session
from app.utils import hash_password
router = APIRouter(
    prefix = "/users" ,
    tags = ["USERS"]
)

@router.post("/" , status_code=status.HTTP_201_CREATED , response_model = UserOut )
def create_user( user : UserCreate , db : Session = Depends(get_db)) :
    #hash the password so that the password is not stored in the database
    hashed_pwd = hash_password(user.password)
    user.password = hashed_pwd
    new_user = models.User( email = user.email , password = hashed_pwd)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/{id}" , response_model = UserOut)
def get_user(id : int , db : Session = Depends(get_db) ) :
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user :
        raise HTTPException( status_code = status.HTTP_404_NOT_FOUND , detail = f"User with ID:{id} doesn't Exist")
    return user 