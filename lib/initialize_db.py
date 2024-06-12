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

# Create some initial data only if tables are created successfully
if not indexes or not any(index['name'] == 'ix_users_username' for index in indexes):
    user1 = User(username='john', email='john@example.com', password='password')
    session.add(user1)
    session.commit()

    task1 = Task(name='Task 1', description='Description 1', priority=1, due_date='2023-06-30', assigned_to=user1)
    session.add(task1)
    session.commit()

