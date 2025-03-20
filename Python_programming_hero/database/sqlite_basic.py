import sqlite3
conn = sqlite3.connect('facebook.db')
cursor = conn.cursor()

cursor.execute("INSErt into users values(0, 'iron@avengers.com', 'iDiedAgain', Null)")

conn.commit()
conn.close()