import sqlite3

# Connect to database (creates it if it doesn't exist)
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Drop and create the users table
cursor.execute('DROP TABLE IF EXISTS users')
cursor.execute('''
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
''')

# Insert a test user
cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'admin123')")

# Save and close
conn.commit()
conn.close()

print("Database initialized and test user created.")
