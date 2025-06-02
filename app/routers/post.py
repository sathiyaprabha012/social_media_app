from fastapi import APIRouter, Depends, FastAPI, HTTPException, Response , status
from sqlalchemy import func
from app import models
import app
from typing import List, Optional 
from app.database import SessionLocal, get_db
from app.oauth2 import get_current_user
from app.schemas import Post, PostCreate, PostOut
from sqlalchemy.orm import Session

router = APIRouter( 
    prefix = "/posts" ,
    tags = ["POSTS"]
)

@router.get("/" , response_model = List[PostOut])
def get_posts( db : Session = Depends(get_db) , current_user : int = Depends(get_current_user) , limit : int = 10 , skip : int = 0 , search : Optional[str] = "") :
    # cursor.execute("""SELECT * FROM posts""")
    # posts = cursor.fetchall()
    # posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    posts =db.query(models.Post , func.count(models.Vote.post_id).label("votes")).join(models.Vote , models.Vote.post_id == models.Post.id , isouter = True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()

    return posts



@router.post("/" , status_code=status.HTTP_201_CREATED , response_model = Post )
def create_posts( new_post : PostCreate , db : Session = Depends(get_db) ,  current_user : int = Depends(get_current_user)) :
    # cursor.execute("INSERT INTO posts (title , content , published) VALUES (%s , %s , %s ) RETURNING *;" , (new_post.title , new_post.content , new_post.published))
    # n_post = cursor.fetchone()
    # conn.commit()

    # n_post = models.Post( title = new_post.title , content = new_post.content , published = new_post.published)

    n_post = models.Post( owner_id = current_user.id , **new_post.dict()) #Unpacking the dictionary incase of more feilds 
    db.add(n_post)
    db.commit()
    db.refresh(n_post)
    return n_post


@router.get("/{id}" , response_model = PostOut)
def get_post (id : int , db : Session = Depends(get_db) , current_user : int = Depends(get_current_user)) :
    # cursor.execute("""SELECT * from posts where id = %s""" , (str(id),))
    # post = cursor.fetchone()

    # post_query = db.query(models.Post)
    # post = post_query.first()
    post =db.query(models.Post , func.count(models.Vote.post_id).label("votes")).join(models.Vote , models.Vote.post_id == models.Post.id , isouter = True).filter( models.Post.id == id ).group_by(models.Post.id).first()
    if not post :
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND , detail = f"Post with ID :  {id} doesn't exist!")
    return post


@router.delete("/{id}") 
def delete_post(id : int , db : Session = Depends(get_db) , current_user : int = Depends(get_current_user) ) :
    # cursor.execute("""DELETE FROM posts where id = %s RETURNING * """ , (str(id),))
    # deleted_post = cursor.fetchone()
    # conn.commit() 

    post_query = db.query(models.Post).filter(models.Post.id == id)
    to_be_deleted_post = post_query.first()
    if to_be_deleted_post == None :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail = f"Post with ID : {id} doesn't exist!")
    if to_be_deleted_post.owner_id != current_user.id :
        raise HTTPException( status_code = status.HTTP_403_FORBIDDEN , detail = "Not Authorized to perform the requested action!")
    
    post_query.delete( synchronize_session = False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)



@router.put("/{id}" , response_model = Post) 
def update_post (id : int , updated_post : PostCreate , db : Session = Depends(get_db) , current_user : int = Depends(get_current_user)) :
    # cursor.execute("""UPDATE posts SET title = %s , content = %s , published = %s   WHERE id = %s RETURNING *; """ , (post.title , post.content , post.published , str(id)))
    # updated_post = cursor.fetchone()
    # conn.commit()

    post_query = db.query(models.Post).filter(models.Post.id == id)

    to_be_updated_post = post_query.first()
    if to_be_updated_post == None :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail = f"Post with ID : {id} doesn't exist!")

    if to_be_updated_post.owner_id != current_user.id :
        raise HTTPException( status_code = status.HTTP_403_FORBIDDEN , detail = "Not Authorized to perform the requested action!")
    
    post_query.update( updated_post.dict() , synchronize_session=False)
    db.commit()
    return  post_query.first()

