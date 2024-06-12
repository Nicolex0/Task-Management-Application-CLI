# lib/models/__init__.py
from .db import Base, session, engine
from .user import User
from .task import Task

# Create the database tables
Base.metadata.create_all(bind=engine)

__all__ = ["User", "Task", "session", "Base"]