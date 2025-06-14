from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship

# Defining our columns 
class Blog(Base):
    __tablename__ = 'blogs' # it should be there because it one the requirements in creating database

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)

    # Creating Relationship
    user_id = Column(Integer, ForeignKey('users.id'))
    creator = relationship("User", back_populates="blogs")
  
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    # Creating Relationship
    blogs = relationship("Blog", back_populates="creator")