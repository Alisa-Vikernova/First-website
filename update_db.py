import sqlite3

conn = sqlite3.connect("forum.db")
cursor = conn.cursor()
cursor.execute("ALTER TABLE messages ADD COLUMN ip TEXT;")
conn.commit()
conn.close()
print("Колонка ip успешно добавлена!")
