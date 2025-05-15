from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

# Global comment list (for demonstration only)
comments = []

@app.route('/')
def home():
    return '''
    <h1>Welcome to the Vulnerable Flask App</h1>
    <ul>
        <li><a href="/login">Login Page (SQL Injection)</a></li>
        <li><a href="/comments">Comments Page (XSS)</a></li>
        <li><a href="/profile">Profile Page (CSRF)</a></li>
    </ul>
    '''

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # ✅ Secure query using parameterized values (Fixed SQLi)
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            return f"<h2>Welcome, {username}!</h2>"
        else:
            return "<h2>Login failed. Invalid credentials.</h2>"
    
    return render_template('login.html')

@app.route('/comments', methods=['GET', 'POST'])
def comment_section():
    if request.method == 'POST':
        comment = request.form['comment']
        comments.append(comment)  # 💀 Vulnerable to XSS
    return render_template('comments.html', comments=comments)

@app.route('/profile', methods=['GET', 'POST'])
def update_profile():
    name = None
    if request.method == 'POST':
        name = request.form['name']  # 💀 No CSRF protection here
    return render_template('profile.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
