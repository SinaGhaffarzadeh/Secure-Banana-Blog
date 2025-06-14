from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Connecting to database
SQLALCHAMY_DATABASE_URL = 'sqlite:///./blog.db'
engine = create_engine(SQLALCHAMY_DATABASE_URL, connect_args={
                       "check_same_thread": False})

# Creating a session
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False,)

# Declare a mapping
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()