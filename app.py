from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome! Go to /login to test SQL injection."

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Intentionally vulnerable SQL query
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        print(f"Executing query: {query}")  # for debugging
        cursor.execute(query)
        user = cursor.fetchone()
        conn.close()

        if user:
            return f"<h2>Welcome, {username}!</h2>"
        else:
            return "<h2>Login failed. Invalid credentials.</h2>"
    
    return render_template('login.html')
