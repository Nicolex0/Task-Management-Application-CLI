from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Set up the database URL
DATABASE_URL = 'sqlite:///task_manager.db'

