from fastapi import Depends , status , HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError , jwt
from datetime import datetime , timedelta
from app import models
from app.database import get_db
from app.schemas import TokenData
from sqlalchemy.orm import Session 
from app.config import settings


oauth2_schema = OAuth2PasswordBearer( tokenUrl = 'login')
#SECRET KEY
#ALGORITHM
#Expriration time 

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes

def create_access_token( data : dict) :
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta( minutes = ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp" : expire})

    encode_jwt = jwt.encode( to_encode ,SECRET_KEY , algorithm = ALGORITHM)

    return encode_jwt



def verify_access_token ( token : str , credentials_exception ) :
    
    try : 
        payload = jwt.decode( token , SECRET_KEY , algorithms = [ALGORITHM])

        id : str = payload.get("user_id")

        if id is None :
            raise credentials_exception 
        token_data = TokenData( id = id )
        return token_data
    except JWTError :
        raise credentials_exception


def get_current_user ( token : str = Depends(oauth2_schema) , db : Session = Depends(get_db)) :
    credentials_exception = HTTPException(status_code = status.HTTP_401_UNAUTHORIZED , detail = "Could not validate credentials" , headers = {"WWW-Authenticate" : "Bearer"})
    token =  verify_access_token ( token , credentials_exception )
    user = db.query(models.User).filter(models.User.id == token.id).first()
    return user
