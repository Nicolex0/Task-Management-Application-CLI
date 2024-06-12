# Add necessary SQLAlchemy and OS imports for database setup
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Add task_manager.db for task management database storage
DATABASE_FILE = "task_manager.db"