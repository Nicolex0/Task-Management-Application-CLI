from sqlalchemy.orm import sessionmaker
from sqlalchemy import inspect
from lib.models.db import engine, Base
from lib.models.user import User
from lib.models.task import Task

# Check for existing index before creating
inspector = inspect(engine)
indexes = inspector.get_indexes('users')

if not any(index['name'] == 'ix_users_username' for index in indexes):
    # Create all tables if the index doesn't exist
    Base.metadata.create_all(bind=engine)
else:
    print("Index 'ix_users_username' already exists.")

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

