# 💉 SQL Injection Vulnerability Demo

## 🔍 Description

This page demonstrates a classic **SQL Injection vulnerability** in a login form using Flask and SQLite.

The application fails to sanitize user input before executing it in an SQL query, allowing an attacker to manipulate the query logic and bypass authentication.

---

## 🧪 Vulnerable Code (in `app.py`)

```python
query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
cursor.execute(query)
