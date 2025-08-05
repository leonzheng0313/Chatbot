import sqlite3

conn = sqlite3.connect('chatpersona.db')
cursor = conn.cursor()

print('Characters table structure:')
cursor.execute('PRAGMA table_info(characters)')
for row in cursor.fetchall():
    print(row)

print('\nSample character data:')
cursor.execute('SELECT * FROM characters LIMIT 3')
for row in cursor.fetchall():
    print(row)

conn.close()