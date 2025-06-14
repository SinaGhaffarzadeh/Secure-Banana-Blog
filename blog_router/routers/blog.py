
from typing import List
from fastapi import APIRouter, Depends, status, HTTPException, Response
from .. import schemas, database, models # it should be called from main folder (blog_router). so we can do it by "..".
from sqlalchemy.orm import Session
from . import oauth2
from ..repository import blog  # some function defined there to use them here to have a clean code
 

router = APIRouter(
    prefix = '/blog',
    tags= ['Blog']
)


get_db = database.get_db
# Getting all the blocks from database
@router.get('/', response_model= List[schemas.ShowBlog])
def all(db:Session = Depends(get_db), 
        current_user: schemas.User = Depends(oauth2.get_current_user)):
    # # This function will return all the blogs have been saved into the database.
    # # It will return a List of dictionary like;
    #     #     [
    #     # {
    #     #     "title": "Title",
    #     #     "body": "My body",
    #     #     "id": 1
    #     # },
    #     # {
    #     #     "title": "Second Title",
    #     #     "body": "My second body",
    #     #     "id": 2
    #     # }
    #     # ]
    return blog.get_all(db)

# To store the information and connect to database we need to use add db as a Session that is depends on get_db function. whitout 
# this, db will recognize as a query parameter.
@router.post('/', status_code= status.HTTP_201_CREATED)
def create(request: schemas.Blog, db:Session = Depends(get_db), 
        current_user: schemas.User = Depends(oauth2.get_current_user)):
    # # This function will return all the blogs have been saved into th
    # # by adding db in this way "db:Session = Depends(get_db)", we can use models to create anything we want.
    # # then by add, commit, and refresh we will able to add them into database. 

    return blog.create(request, db)

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model= schemas.ShowBlog)
def show(id:int , db:Session = Depends(get_db), 
        current_user: schemas.User = Depends(oauth2.get_current_user)):
    # # This function will return all the blogs have been saved into th
    '''
    This function by filtering method, filters the same thing that we want and return all its information
    saved in database.
    '''

    return blog.show(id, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session =Depends(get_db), 
        current_user: schemas.User = Depends(oauth2.get_current_user)):
    # # This function will return all the blogs have been saved into th
    return blog.destroy(id, db)

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
# It is like creating part. by adding request:... we will allow to get access to contents of database.
def update(id, request: schemas.Blog, db: Session = Depends(get_db), 
        current_user: schemas.User = Depends(oauth2.get_current_user)):
    # # This function will return all the blogs have been saved into th
    # # To update by query we just need add update and what we want to be updated in the end of query. As they
    # # mentioned in sqlalchemy docs.
    # # By using request, we will able to update all parameters in database.
    return blog.update(id, request, db)