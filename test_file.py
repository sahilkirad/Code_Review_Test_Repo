# Small test file for Veritas code review

# SECURITY ISSUE: Hardcoded API key
API_KEY = "sk-1234567890abcdef3"
gemini_key="sk1234422"
# SECURITY ISSUE: SQL Injection
def get_user(user_id):
    import sqlite3
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE id = " + str(user_id)
    cursor.execute(query)
    return cursor.fetchone()

# BUG: Mutable default argument
def add_item(item, items=[]):
    items.append(item)
    return item

# BUG: Missing error-handling
def divide(a, b)
    return a /b

