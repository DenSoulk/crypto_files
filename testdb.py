import sqlite3

conn = sqlite3.connect('message.db')
c = conn.cursor()

c.execute("ALTER TABLE message ADD COLUMN is_read BOOLEAN NOT NULL CHECK (is_read IN (0, 1))")
# c.execute("ALTER TABLE message ADD COLUMN date TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL")
