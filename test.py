import sqlite3

conn = sqlite3.connect('data.db')  
cursor = conn.cursor()
for i in range(1000):
    cursor.execute("INSERT INTO bills (amount, date) VALUES (?,?)", (i, 2))
    conn.commit()