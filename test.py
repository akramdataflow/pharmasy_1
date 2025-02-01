import sqlite3

conn = sqlite3.connect('data.db')  
cursor = conn.cursor()
cursor.execute("INSERT INTO purchases (name_mat, count, com_name , buy_price ,sel_price , expiry) VALUES (?,?,?,?, ?, ?)", ('name_mat', 232, 'com_name' , 453 ,354 , 3 ))
conn.commit()