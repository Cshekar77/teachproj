import sqlite3

# Connect to database
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Enable foreign key support
cursor.execute("PRAGMA foreign_keys = ON")

# ---------------- Faculty Table ----------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS Faculty(
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    phone TEXT,
    email TEXT
)
""")

# ---------------- Subject Table ----------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS Subject(
    id TEXT PRIMARY KEY,
    subject_name TEXT NOT NULL,
    subject_code TEXT UNIQUE
)
""")

# ---------------- Section Table ----------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS Section(
    id TEXT PRIMARY KEY,
    section_name TEXT,
    semester TEXT
)
""")

# ---------------- Day Table ----------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS Day(
    id TEXT PRIMARY KEY,
    day_name TEXT
)
""")

# ---------------- TimeSlot Table ----------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS TimeSlot(
    id TEXT PRIMARY KEY,
    start_time TEXT,
    end_time TEXT
)
""")

# ---------------- SubjectMapping Table ----------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS SubjectMapping(
    id TEXT PRIMARY KEY,
    faculty_id TEXT,
    subject_id TEXT,
    section_id TEXT,
    FOREIGN KEY (faculty_id) REFERENCES Faculty(id) ON DELETE CASCADE,
    FOREIGN KEY (subject_id) REFERENCES Subject(id) ON DELETE CASCADE,
    FOREIGN KEY (section_id) REFERENCES Section(id) ON DELETE CASCADE
)
""")

# ---------------- Timetable Table ----------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS Timetable(
    id TEXT PRIMARY KEY,
    subject_mapping_id TEXT,
    day_id TEXT,
    timeslot_id TEXT,
    FOREIGN KEY (subject_mapping_id) REFERENCES SubjectMapping(id) ON DELETE CASCADE,
    FOREIGN KEY (day_id) REFERENCES Day(id) ON DELETE CASCADE,
    FOREIGN KEY (timeslot_id) REFERENCES TimeSlot(id) ON DELETE CASCADE
)
""")

# Commit and close
conn.commit()
conn.close()

print("Database Created Successfully ✅ (Alphanumeric ID Version)")