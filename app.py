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

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        # ✅ Secure query using parameterized values
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            return f"<h2>Welcome, {username}!</h2>"
        else:
            return "<h2>Login failed. Invalid credentials.</h2>"
    
    return render_template('login.html')

