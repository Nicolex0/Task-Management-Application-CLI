from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .db import Base  

# Create User class
class User(Base):
    __tablename__ = "users"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    tasks = relationship("Task", back_populates="assignee") 