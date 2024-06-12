from sqlalchemy.orm import sessionmaker
from sqlalchemy import inspect
from lib.models.db import engine, Base
from lib.models.user import User
from lib.models.task import Task

# Check for existing index before creating
inspector = inspect(engine)
indexes = inspector.get_indexes('users')


