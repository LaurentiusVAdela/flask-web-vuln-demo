# ⚠️ Cross-Site Scripting (XSS) Vulnerability

## 🔍 Description

This page demonstrates a **stored XSS vulnerability** where user-submitted input is displayed without sanitization.

---

## 💥 How to Reproduce

1. Visit: http://localhost:5000/comments
2. Submit this input:
   ```html
   <script>alert("XSS vulnerability!")</script>
