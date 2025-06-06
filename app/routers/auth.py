from fastapi import APIRouter , Depends , status , HTTPException , Response 
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app import models
from app.database import get_db
from app.oauth2 import create_access_token
from app.schemas import UserLogin , Token
from app.utils import verify
router = APIRouter (
    tags = ["AUTHENTICATION"]
)

@router.post("/login" , response_model = Token )
def login( user_credentials : OAuth2PasswordRequestForm = Depends() , db : Session = Depends(get_db) ) :
    # OAuth2PasswordRequestForm returns username and password

    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()
    if not user :
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST , detail = "Invalid Email!")
    if not verify(user_credentials.password , user.password) :
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED , detail = "Invalid Password!")
    
    access_token = create_access_token (data = {"user_id" : user.id})

    return {"access_token" : access_token , "token_type" : "bearer"}
