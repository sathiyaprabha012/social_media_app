from fastapi import APIRouter, Depends, FastAPI, HTTPException, Response , status
from app import models
from app.database import get_db
from app.oauth2 import get_current_user
from app.schemas import Vote
from sqlalchemy.orm import Session

router = APIRouter(
    prefix = "/vote" ,
    tags = ["VOTE"]
)

@router.post("/" , status_code =  status.HTTP_201_CREATED)
def vote( vote : Vote , db : Session = Depends(get_db) , current_user : int = Depends( get_current_user)) :     
    post  = db.query(models.Post).filter( models.Post.id == vote.post_id ).first()
    if not post :
        raise HTTPException( status_code = status.HTTP_404_NOT_FOUND , detail = "Post doesn't Exist!")
    
    vote_query = db.query(models.Vote).filter( models.Vote.post_id == vote.post_id , models.Vote.user_id == current_user.id)
    vote_found = vote_query.first()
    if (vote.dir == 1) :
        if vote_found is not None :
            raise HTTPException( status_code = status.HTTP_409_CONFLICT , detail = f"User : {current_user.id} has already voted on post {vote.post_id}")
        else :
            create_query = models.Vote ( post_id = vote.post_id , user_id = current_user.id )
            db.add(create_query)
            db.commit()
            return {"message" : "Successfully added Vote!"}
    else :
        if not vote_found : 
            raise HTTPException( status_code = status.HTTP_404_NOT_FOUND , detail = "Vote doesn't exist!")
        else :
            vote_query.delete( synchronize_session = False)
            db.commit()
            return {"message" : "Successfully Unvoted!"}