import sqlite3
import random
from datetime import datetime, timedelta

# الاتصال بقاعدة البيانات
conn = sqlite3.connect('data.db')  
cursor = conn.cursor()



# تحديد النطاق الزمني للتواريخ العشوائية (آخر سنة مثلاً)
start_date = datetime.now() - timedelta(days=365)  # سنة واحدة للخلف



for i in range(1000):
    random_days = random.randint(0, 365)  # عدد عشوائي من الأيام
    random_date = (start_date + timedelta(days=random_days)).strftime('%d/%m/%Y')  # تحويل إلى صيغة يوم/شهر/سنة
    count = random.randint(1,20)
    unit_price = random.randint(1000, 100000)
    id = random.randint(0,100)
    cursor.execute("INSERT INTO bill_detals (id, mat_name, unit_price, count, total_price, date) VALUES (?, ?, ?, ?, ?, ?)", (id,'any', unit_price, count, unit_price*count, random_date))

# حفظ التغييرات وإغلاق الاتصال
conn.commit()
conn.close()
