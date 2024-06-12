# Add necessary SQLAlchemy and OS imports for database setup
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Add task_manager.db for task management database storage
DATABASE_FILE = "task_manager.db"

# Configure database URL for SQlite database connection
DATABASE_URL = f"sqlite:///{os.path.join(os.path.dirname(__file__), DATABASE_FILE)}"

#Initialize database engine with session maker bound to engine
engine = create_engine(DATABASE_URL)