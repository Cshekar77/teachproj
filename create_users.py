"""
Run this ONCE to set up the Users table and create the admin account.
Usage: python create_users.py
"""
import sqlite3
from werkzeug.security import generate_password_hash

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Create Users table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users (
        id       INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT    NOT NULL UNIQUE,
        password TEXT    NOT NULL,
        role     TEXT    NOT NULL CHECK(role IN ('admin', 'teacher')),
        faculty_id TEXT  REFERENCES Faculty(id)
    )
""")

# Create default admin — change password here before running!
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin@123"   # ← change this

cursor.execute("""
    INSERT OR IGNORE INTO Users (username, password, role)
    VALUES (?, ?, 'admin')
""", (ADMIN_USERNAME, generate_password_hash(ADMIN_PASSWORD)))

conn.commit()
conn.close()
print("✅ Users table created.")
print(f"✅ Admin user '{ADMIN_USERNAME}' created with hashed password.")
print("ℹ️  Teachers can be added from the Admin Dashboard.")