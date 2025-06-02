from typing import Optional
from pydantic import BaseModel, EmailStr , Field
from datetime import datetime

class PostBase (BaseModel) : # A Pydantic Model
    title : str
    content : str 
    published : bool = True

class PostCreate( PostBase) :
    pass

class UserOut (BaseModel) :
    id : int 
    email : EmailStr
    created_at : datetime
    
    class Config :
        orm_model = True 
        
class Post(PostBase) : #Exact data to be seen on the frontend
    id : int
    created_at : datetime
    owner_id : int 
    owner : UserOut
    class Config :
        orm_model = True 

class PostOut(BaseModel) :
    Post : Post
    votes : int 
    class Config :
        orm_model = True 


class UserCreate (BaseModel) :
    email : EmailStr 
    password : str



class UserLogin (BaseModel) :
    email : EmailStr
    password : str  


class Token (BaseModel) :
    access_token : str 
    token_type : str 

class TokenData(BaseModel) :
    id : Optional[int] = None 


class Vote (BaseModel) :
    post_id : int 
    dir : int = Field(..., ge=0, le=1)