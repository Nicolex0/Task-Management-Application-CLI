from .models import session, User, Task

# Helper functions for User model
def create_user(username, email, password):
    user = User(username=username, email=email, password=password)
    session.add(user)
    session.commit()
    return user

# Create function to get user by id
def get_user_by_id(user_id):
    return session.query(User).filter(User.id == user_id).first()

def get_user_by_username(username):
    return session.query(User).filter(User.username == username).first()

def delete_user(user_id):
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        session.delete(user)
        session.commit()
        return True
    return False

def get_all_users():
    return session.query(User).all()

# Helper functions for Task model
def create_task(name, description, priority, due_date, assigned_to=None):
    task = Task(name=name, description=description, priority=priority, due_date=due_date, assigned_to=assigned_to)
    session.add(task)
    session.commit()
    return task


