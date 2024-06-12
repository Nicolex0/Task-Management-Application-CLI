from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Set up the database URL
DATABASE_URL = 'sqlite:///task_manager.db'

# Set up the engine class and the base class
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Base = declarative_base()

#Set up LocalSession
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal() 
Base.metadata.create_all(engine)

