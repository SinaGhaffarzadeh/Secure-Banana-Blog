from typing import List, Optional
from pydantic import BaseModel

# our template/ form that will show in swagger UI. In Swagger UI, we just need to fill up title and body,
# then database return an ID and save them into it.
class Blog(BaseModel):
    title:str
    body:str
    class Config():
        orm_mode = True 


class User(BaseModel): 

    
    name: str
    email: str
    password: str


class ShowUser(BaseModel):
    name: str
    email: str
    blogs : List[Blog] = [] # blogs is a relationship that created in schemas 
                      # if we can not able to put the class after another class to work properply.
                      # we can use the main class to show the results
    class Config():
        orm_mode = True


# This class allows us to show the variables in Blog class. Notice that without using Config class
# the output will not work properly. Because, we are using ORM (sqlalchemy.orm) we should say that Hey
# we are using orm mode. 
# Additionally, we can manage manually to show the output. by changing sub-class to BaseModel and
# write what we want it well return it in the output.
class ShowBlog(BaseModel):
    title:str
    body:str
    creator : ShowUser # it will return name and email of creator.
    class Config():
        orm_mode = True


class Login(BaseModel):
    username:str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None