
'''
1- define a router
2- define our path decorator
3- register it from main.py 
4- define the features of our function
5- verify the passwords
'''

from fastapi import APIRouter, Depends, HTTPException, status
from .. import models, schemas, database
from . import token 
from sqlalchemy.orm import Session
from ..Hashing import Hash
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    tags= ['Authantication']
)


@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f"Invalid Credintials")
    # Check and verify the passwords
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f"Incorect Password")
    
    access_token = token.create_access_token(data={"sub": user.email})
    return {'access_token':access_token,
             "token_type" : "bearer"}

