
'''
Tips;
1- Response Status Code. It is one of the way that allow us to return a code that explain what has done
   into the code. did there a thing created, got it or anything.
   Each code has its defination that we can see them here (https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status)
   for example, 201 refer to created and 200 refers to okey.
   Response codes can be added by path operation decorator using status_code
2- Ensuring when a wrong thing passed, the FastAPI will return correct Response code and describtion. To do
   this we can use Response function from fastapi and create by a condition.
   The other way of showing errors is using HTTPExeptions.
3- For make a litle bit privecy, we are able to show what we want. for example, showing just piece of informations
   that are not privte, here like title and body. To do this we should create a class in schemas and refer it
   to response_model at decorator. An instance of it has been shown in get(/blog/{id}) and get(/blog).
   There will be two type example one of them refer to single parmeter and the other for showing a list of output.

'''

# from fastapi import FastAPI, Depends, status, Response, HTTPException
from fastapi import FastAPI
# from . import  models, schemas, Hashing
from . import  models
# from .database import engine, get_db
from .database import engine
# from sqlalchemy.orm import Session
# from typing import List
from .routers import blog, user, authentication
# from passlib.context import CryptContext

app = FastAPI()

# This line is extrimly important because it will able us to create our database.
models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)

