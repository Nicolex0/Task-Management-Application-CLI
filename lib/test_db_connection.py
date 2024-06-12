import sqlite3
# Create a database connection
def create_connection(db_file):
    """ Create a database connection to the SQLite database specified by db_file """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Connection to SQLite database successful")
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to SQLite database: {e}")
        return None

# Path to your SQLite database file
db_file = "task_manager.db"