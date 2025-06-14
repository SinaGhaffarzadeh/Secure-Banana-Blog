from fastapi import APIRouter
from .. import database, schemas, models
from sqlalchemy.orm import Session
from typing import List
from fastapi import APIRouter, Depends, status, HTTPException, Response
from ..Hashing import Hash

from ..repository import User

router = APIRouter(
    prefix= "/user",
    tags= ['User']
) 
get_db = database.get_db


# Defining User
@router.post('/', response_model= schemas.ShowUser ,status_code=status.HTTP_201_CREATED)
def user(request: schemas.User, db:Session = Depends(get_db)):
    return User.userRepository(request, db)


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model= schemas.ShowUser)
def get_user(id, response: Response, db:Session = Depends(get_db)):
    return User.show(id, db)