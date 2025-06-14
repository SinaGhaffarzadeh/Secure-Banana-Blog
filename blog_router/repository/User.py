from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status
from ..Hashing import Hash

def userRepository(request: schemas.User, db: Session):

    # As we define a models for creating input information into the database. 
    # we should create for User sperately.
    # hashedPassword = pwd_cxt.hash(request.password) # This line transfer to Hashing foldor
    # new_user = models.User(name = request.name, email = request.email, password = hashedPassword) # This line because of tranfering hashing to Hashing folder is commented

    new_user = models.User(name = request.name, email = request.email, password = Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user


def show(id:int, db: Session):

    user = db.query(models.User).filter(models.User.id == id).first()
    # making error code and descrtiption when there is noting to show 
    if not user:
        # # Fist Method
        # response.status_code = status.HTTP_404_NOT_FOUND 
        # return {"detail": f"user with the id {id} is not available"}
        # Second method
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"User with the id {id} is not available")
    return user