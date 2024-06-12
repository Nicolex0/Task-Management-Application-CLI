from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from .db import Base
from .user import User

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    priority = Column(Integer)
    due_date = Column(String)
    assigned_to = Column(Integer, ForeignKey('users.id'))

    assignee = relationship("User", back_populates="tasks")