import sqlite3

class Database:
    def __init__(self, db_name="awallet.db"):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.create_tables()

    def create_tables(self):
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT
            )
        """)
        self.conn.commit()

    def create_user(self, user_id, name):
        self.conn.execute("INSERT OR IGNORE INTO users (id, name) VALUES (?, ?)", (user_id, name))
        self.conn.commit()

    def get_user(self, user_id):
        cursor = self.conn.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        return cursor.fetchone()

# Global instance
db = Database()

# Exposed functions
def init_db():
    pass  # tables are already created in constructor

def create_user(user_id, name):
    db.create_user(user_id, name)

def get_user(user_id):
    return db.get_user(user_id)
