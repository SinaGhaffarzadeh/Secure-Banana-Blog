
from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status


def get_all(db: Session):
    
    blog = db.query(models.Blog).all()
    return blog

def create(request: schemas.Blog, db: Session):

    # by adding db in this way "db:Session = Depends(get_db)", we can use models to create anything we want.
    # then by add, commit, and refresh we will able to add them into database. 
    new_blog = models.Blog(title = request.title, body = request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    
    return new_blog 


def show(id: int, db: Session):

    '''
    This function by filtering method, filters the same thing that we want and return all its information
    saved in database.
    '''
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    # making error code and descrtiption when there is noting to show 
    if not blog:
        # # Fist Method
        # response.status_code = status.HTTP_404_NOT_FOUND 
        # return {"detail": f"blog with the id {id} is not available"}
        # Second method
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"blog with the id {id} is not available")
    return blog


def destroy(id: int, db: Session):

    blog = db.query(models.Blog).filter(models.Blog.id == id)
    # Like posting new thing, here we should commit the process.
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not found")
    
    else:
        blog.delete(synchronize_session=False)
        db.commit()
        return 'Done'

def update(id: int, request: schemas.Blog, db: Session):
    # To update by query we just need add update and what we want to be updated in the end of query. As they
    # mentioned in sqlalchemy docs.
    # By using request, we will able to update all parameters in database.
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not found")
    
    else:
        blog.update(request.dict(exclude_unset=True))
        db.commit()
        return {"message": "Updated successfully"}