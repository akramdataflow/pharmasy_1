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
    
    cursor.execute("INSERT INTO bills (amount, date) VALUES (?, ?)", (random.randint(1000, 100000), random_date))

# حفظ التغييرات وإغلاق الاتصال
conn.commit()
conn.close()
