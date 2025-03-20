import sqlite3
conn = sqlite3.connect('table.db')
cursor = conn.cursor()

cursor.execute("SELECT Name, Mom FROM Kids INNER JOIN Family ON kids.FamilyId = Family.FamilYId")

users = cursor.fetchall()
for row in users:
    print(row)


conn.commit()
conn.close()