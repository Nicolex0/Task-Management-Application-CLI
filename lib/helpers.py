from .models import session, User, Task

# Helper functions for User model
def create_user(username, email, password):
    user = User(username=username, email=email, password=password)
    session.add(user)
    session.commit()
    return user