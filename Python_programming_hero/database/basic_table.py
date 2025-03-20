import sqlite3
conn = sqlite3.connect('table.db')
cursor = conn.cursor()

cursor.execute("CREATE TABLE family(FamilyID integer primary key, Dad Text, Mom text)")

cursor.execute("INSERT INTO family VALUES (1, 'Will Smith', 'Jada Smith')")
cursor.execute("INSERT INTO family VALUES (2, 'Billy Cyrus', 'Tish Cyrus')")
cursor.execute("INSERT INTO family VALUES (3, 'Barack Obama', 'Michelle Obama')")
cursor.execute("INSERT INTO family VALUES (4, 'Bill Gates', 'Melinda Gates')")

cursor.execute("CREATE TABLE kids (KidId integer primary key, Name Text, Age integer, FamilyID Integer)")

cursor.execute("INSERT INTO kids Values (1, 'Jaden Smith', 21, 1)")
cursor.execute("INSERT INTO kids Values (2, 'Willow smith', 19, 1)")
cursor.execute("INSERT INTO kids Values (4, 'Malia Obama', 21, 3)")
cursor.execute("INSERT INTO kids Values (5, 'Sasha Obama', 18, 3)")
cursor.execute("INSERT INTO kids Values (6, 'Justin Bieber', 18, 5)")

conn.commit()
conn.close()