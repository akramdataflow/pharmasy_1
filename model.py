import sqlite3
from datetime import datetime

class Model:
    def __init__(self):
        self.conn = sqlite3.connect('data.db')  
        self.cursor = self.conn.cursor()

    def add_mat(self, name_mat, name_com, type_mat, count, expiry, Suitable_age):
        self.cursor.execute("INSERT INTO mat (name_mat, name_com, type_mat, count, expiry, Suitable_age) VALUES (?, ?, ?, ?, ?, ?)", (name_mat, name_com, type_mat, count, expiry, Suitable_age))
        self.conn.commit()


        
    def get_mat(self):
        self.cursor.execute('SELECT * FROM mat')
        rows = self.cursor.fetchall()  # جلب جميع البيانات دفعة واحدة
        mat_id = [col[0] for col in rows] 
        name_mat = [col[1] for col in rows] 
        name_com = [col[2] for col in rows]
        type_mat = [col[3] for col in rows] 
        count = [col[4] for col in rows]
        expiry = [col[5] for col in rows]
        Suitable_age = [col[6] for col in rows]
        return mat_id, name_mat, name_com, type_mat, count, expiry, Suitable_age
    
    
    def del_mat(self, mat_id):
        self.cursor.execute("DELETE FROM mat WHERE id = ?", (mat_id,))
        self.conn.commit()  

    
    def update_mat(self, mat_id, name_mat, name_com, type_mat, count, expiry, Suitable_age):
        self.cursor.execute('''
            UPDATE mat
            SET name_mat = ?, name_com = ?, type_mat = ?, count = ? , expiry = ? ,  Suitable_age = ?
            WHERE id = ?
        ''', (name_mat, name_com, type_mat, count, expiry, Suitable_age, mat_id))
        self.conn.commit()

        





        
#######################################################دفع مؤجل 
   
    def add_Deferred(self, customer_name, phone_num, address , price):
        self.cursor.execute("INSERT INTO deferred (cos_name, cos_phone, cos_location,  price) VALUES (?, ?, ?, ?)", (customer_name, phone_num, address, price))
        self.conn.commit()
        

        
    def get_Deferred(self):
        self.cursor.execute('SELECT * FROM deferred')
        rows = self.cursor.fetchall()  
        defe_id = [col[0] for col in rows] 
        customer_name = [col[1] for col in rows] 
        phone_num = [str(col[2]) for col in rows]  # Convert to string
        address = [col[3] for col in rows] 
        price = [col[4] for col in rows]
        return defe_id, customer_name, phone_num, address, price
        
        
    
    
    def del_Deferred(self, deferred_id):
        self.cursor.execute("DELETE FROM deferred WHERE id = ?", (deferred_id,))
        self.conn.commit()



    def update_Deferred(self, deferred_id, customer_name, phone_num, address, price):
        self.cursor.execute('''
            UPDATE deferred
            SET cos_name = ?,  cos_phone = ?, cos_location = ?, price = ?
            WHERE id = ?
        ''', (customer_name, phone_num, address, price, deferred_id))
        self.conn.commit()  
             
        ####################لمشتريات

    def add_Purchases(self, name_mat, count, type, com_name , buy_price ,sel_price , expiry ):
        self.cursor.execute("INSERT INTO purchases (name_mat, count, type, com_name , buy_price ,sel_price , expiry) VALUES (?,?,?,?, ?, ?, ?)", (name_mat, count, type, com_name , buy_price ,sel_price , expiry ))
        self.conn.commit()
        

        
    def get_purchases(self):
        self.cursor.execute('SELECT * FROM purchases')
        rows = self.cursor.fetchall()  
        pur_id = [col[0] for col in rows] 
        name_mat = [col[1] for col in rows] 
        count = [str(col[2]) for col in rows] 
        type = [col[3] for col in rows]
        com_name = [col[4] for col in rows] 
        buy_price = [col[5] for col in rows]
        sel_price = [col[6] for col in rows]
        expir = [col[7] for col in rows]
        return pur_id, name_mat, count, type, com_name , buy_price ,sel_price , expir
        
        
    
    
    def del_Purchases(self, purchases_id):
        self.cursor.execute("DELETE FROM purchases WHERE id = ?", (purchases_id,))
        self.conn.commit()



    def update_Purchases(self, purchases_id, name_mat, count, type, com_name , buy_price ,sel_price , expir):
        self.cursor.execute('''
            UPDATE purchases
            SET name_mat = ?,  count = ?, type = ?, com_name = ?, buy_price = ? , sel_price = ? , expiry = ?
            WHERE id = ?
        ''', (name_mat, count, type, com_name , buy_price ,sel_price , expir, purchases_id))
        self.conn.commit()  


        ############list

        
    def del_list(self, list_id):
        self.cursor.execute("DELETE FROM list WHERE id = ?", (list_id,))
        self.conn.commit()



########################################## bill

    def get_bill(self,):
        self.cursor.execute('SELECT * FROM bills')
        rows = self.cursor.fetchall()
        bill_id = [col[0] for col in rows]
        bill_amount =  [str(col[1]) for col in rows]
        bill_date =  [str(col[2]) for col in rows]

        return bill_id, bill_amount , bill_date
    
    


    
