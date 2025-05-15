# 🎯 Cross-Site Request Forgery (CSRF)

## 🔍 Description

This demo shows how a form without CSRF protection is vulnerable to unauthorized actions via third-party pages.

---

## 🧪 Vulnerable Code (app.py)

```python
@app.route('/profile', methods=['GET', 'POST'])
def update_profile():
    name = None
    if request.method == 'POST':
        name = request.form['name']
    return render_template('profile.html', name=name)
