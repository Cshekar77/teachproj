import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Check existing columns
cursor.execute("PRAGMA table_info(SubjectMapping)")
cols = [row[1] for row in cursor.fetchall()]
print("Existing columns:", cols)

if "day_id" not in cols:
    cursor.execute("ALTER TABLE SubjectMapping ADD COLUMN day_id TEXT REFERENCES Day(id)")
    print("Added day_id")

if "timeslot_id" not in cols:
    cursor.execute("ALTER TABLE SubjectMapping ADD COLUMN timeslot_id TEXT REFERENCES TimeSlot(id)")
    print("Added timeslot_id")

conn.commit()
conn.close()
print("Migration complete!")