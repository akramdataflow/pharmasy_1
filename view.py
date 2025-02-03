

import sys 
from PySide6.QtWidgets import QSpinBox, QMainWindow, QPushButton, QGridLayout, QFrame, QVBoxLayout, QLabel , QLineEdit , QSizePolicy , QHeaderView , QTableWidget, QTableWidgetItem,QDateEdit
from PySide6.QtGui import QIcon, QFont
from PySide6.QtCore import Qt, QSize
from PySide6.QtCore import QDate, QSize
from datetime import datetime






#akram
class MyView(QMainWindow):
    def __init__(self, controller=None):
        super().__init__()
        self.controller = controller

        self.setGeometry(100, 200, 800, 1000)
        
        

        main_frame = QFrame()
        main_frame.setStyleSheet(
            """background-color: #fff"""
        )
        layout = QGridLayout(main_frame)

        label_frame = QFrame()
        label_frame.setStyleSheet("""
                                  background-color: #1A3654; 
                                  color: white;
                                  background-image: url('./static/لنكيدو Pharmacy.png');
                                  background-repeat: no-repeat;
                                  background-position: center;
                                  """)
        label_frame.setFixedHeight(100)
        label_frame.setGeometry(0, 0, 800, 1000)

        
        

        



        layout.addWidget(label_frame, 0, 0)

        self.setCentralWidget(main_frame)

        frame = QFrame()
        frame_layout = QGridLayout(frame)
        layout.addWidget(frame, 1, 0)

        icon = QIcon('./static/Untitled (4).png')

        
        # Button 1
        button1 = QPushButton()
        button1.clicked.connect(controller.show_list)
        button1.setStyleSheet("""
            QPushButton {
                background-color: #FFF;
                border-radius: 5px;
                padding: 10px;
                font-size: 16px;
                background-image: url('./static/Group 27.png');
                background-repeat: no-repeat;
                background-position: center;
            }
            QPushButton:hover {
                background-color: #E9FDF2;
            }
        """)
        button1.setIcon(icon)
        button1.setIconSize(QSize(250, 250))
        frame_layout.addWidget(button1, 0, 0)

        # Button 2
        button2 = QPushButton()
        button2.clicked.connect(controller.show_sales)
        button2.setStyleSheet("""
            QPushButton {
                background-color: #FFF;
                border-radius: 5px;
                padding: 10px;
                font-size: 16px;
                background-image: url('./static/Group 2.png');
                background-repeat: no-repeat;
                background-position: center;
            }
            QPushButton:hover {
                background-color: #E9FDF2;
            }
        """)
        button2.setIcon(icon)
        button2.setIconSize(QSize(250, 250))
        frame_layout.addWidget(button2, 0, 1)

        # Button 3
        button3 = QPushButton()
    
        button3.setStyleSheet("""
            QPushButton {
                background-color: #FFF;
                border-radius: 5px;
                padding: 10px;
                font-size: 16px;
                background-image: url('./static/Group 3.png');
                background-repeat: no-repeat;
                background-position: center;
            }
            QPushButton:hover {
                background-color: #E9FDF2;
            }
        """)
        button3.setIcon(icon)
        button3.clicked.connect(controller.show_Purchases)
        button3.setIconSize(QSize(250, 250))
        frame_layout.addWidget(button3, 0, 2)

        # Button 4
        button4 = QPushButton()
        button4.setStyleSheet("""
            QPushButton {
                background-color: #FFF;
                border-radius: 5px;
                padding: 10px;
                font-size: 16px;
                background-image: url('./static/Group 4.png');
                background-repeat: no-repeat;
                background-position: center;
            }
            QPushButton:hover {
                background-color: #E9FDF2;
            }
        """)
        button4.setIcon(icon)
        button4.clicked.connect(controller.show_deferred)
        button4.setIconSize(QSize(250, 250))
        frame_layout.addWidget(button4, 1, 0)


        # Button 6
        button6 = QPushButton()
        button6.setStyleSheet("""
            QPushButton {
                background-color: #FFF;
                border-radius: 5px;
                padding: 10px;
                font-size: 16px;
                background-image: url('./static/Group 6.png');
                background-repeat: no-repeat;
                background-position: center;
            }
            QPushButton:hover {
                background-color: #E9FDF2;
            }
        """)
        button6.setIcon(icon)
        button6.clicked.connect(controller.show_closet)       
        button6.setIconSize(QSize(250, 250))
        frame_layout.addWidget(button6, 1, 1)

        # Button 7
        button7 = QPushButton()
        button7.setStyleSheet("""
            QPushButton {
                background-color: #FFF;
                border-radius: 5px;
                padding: 10px;
                font-size: 16px;
                background-repeat: no-repeat;
                background-image: url('./static/Group 7.png');
                background-position: center;
            }
            QPushButton:hover {
                background-color: #E9FDF2;
            }
        """)
        button7.setIcon(icon)
        button7.clicked.connect(controller. show_Data_analysis) 
        button7.setIconSize(QSize(250, 250))
        frame_layout.addWidget(button7, 1, 2)


        
class Lists(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.setWindowTitle("الفاتورة")
        self.resize(500, 500)

         
        # فريم جديد
        new_frame = QFrame(self)
        new_frame.setStyleSheet("""background-color: #1A3654; border-radius: 4px;""")
        new_frame.setGeometry(0, 0, self.width(), self.height())
        self.setCentralWidget(new_frame)

        new_layout = QGridLayout(new_frame)

        # فريم العنوان مع Layout خاص به
        lest_label_frame = QFrame()
        layout1 = QVBoxLayout(lest_label_frame)  # استخدام Layout منفصل
        lest_label_frame.setStyleSheet("""
            background-color: #50F296; 
            color: white;
            background-repeat: no-repeat;
            background-position: center;
        """)
        lest_label_frame.setFixedHeight(50)
        # 1,2 لكي تاخذ صف واحد وعمودين الاول والثاني
        new_layout.addWidget(lest_label_frame, 0, 0, 1, 2)  # الهيدر 

        # فريم يحتوي على باقي العناصر مع Layout منفصل
        frame = QFrame()
        new_layout.addWidget(frame, 1, 0, 1, 2)

        # إضافة أيقونة في Layout1 (Layout العنوان)
        icon_label = QLabel(lest_label_frame)
        icon = QIcon('./static/Group 28.png')  
        icon_label.setPixmap(icon.pixmap(100, 100))  # تحديد حجم الأيقونة
        layout1.addWidget(icon_label)



        
        #انشاء فريم لوضع البيانات الفريم الابيض السفلي
        frame = QFrame()
        data_frame_layout = QVBoxLayout(frame)
        
        # استرجاع البيانات من الموديل عبر الكونترولر
        data_tabel = self.controller.get_bill_detales_from_model()
        
        # إنشاء جدول البيانات
        self.table = QTableWidget()

        #جعل حجم الجدول يتناسب مع حجم الشاشه 
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.table.setAlternatingRowColors(True)
        
        # تعيين خلفية الجدول إلى اللون الأبيض
        self.table.setStyleSheet("background-color: white;")

        
        # إعداد الجدول: تعيين الأعمدة
        self.table.setColumnCount(4)  # عدد الأعمدة (المادة، العدد، اسم الشركة، سعر الشراء ,سعر البيع ,تاريخ الانتهاء)
        self.table.setHorizontalHeaderLabels(['المادة', ' سعر القطعة', 'العدد', 'السعر الكلي'])  # العناوين
        
        # تعبئة الجدول بالبيانات
        if data_tabel and len(data_tabel[0]) > 0:  # التأكد من وجود بيانات
            row_count = len(data_tabel[0])  # افتراض أن جميع الأعمدة لها نفس الطول
            self.table.setRowCount(row_count)
        
            # تعبئة البيانات في الجدول
            for row in range(row_count):
                self.table.setItem(row, 0, QTableWidgetItem(data_tabel[0][row]))  # إدخال الاسم
                self.table.setItem(row, 1, QTableWidgetItem(str(data_tabel[1][row])))
                self.table.setItem(row, 2, QTableWidgetItem(str(data_tabel[2][row])))   # إدخال اسم الشركة
                self.table.setItem(row, 3, QTableWidgetItem(str(data_tabel[3][row])))  # إدخال النوع

        
            # تعديل حجم الأعمدة لتناسب المحتوى بعد تعبئة الجدول
            self.table.resizeColumnsToContents()
        else:
            self.table.setRowCount(0)
        
        # إضافة الجدول إلى التخطيط داخل الفريم
        data_frame_layout.addWidget(self.table)
        
        # تعيين التخطيط للفريم
        frame.setLayout(data_frame_layout)
        
        # إضافة الفريم إلى التخطيط الخارجي
        new_layout.addWidget(frame, 1, 0)


        
        #انشاء فريم للحفض الفريم الابيض الجانبي
        save_frame = QFrame()
        save_frame.setStyleSheet("""
            border-radius: 4px;
            background-color: #1A3654;
        """)
        save_frame_layout = QGridLayout(save_frame)
        new_layout.addWidget(save_frame,1,1)
        # save_frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        
        #فريم الابيض الزغير 
        frame_whit = QFrame()
        frame_whit.setStyleSheet("""
            border-radius: 16px;
            background-color: #50F296;

       """ )
        frame_whit.setFixedHeight(10)
        save_frame_layout.addWidget(frame_whit,0,0 )
        #الصفر على يساري هوه row
        # الصفر على يميني هوه الكولوم الخطوط العاموديه 

        
        #فريم الابيض الزغير 
        

        bill1 = QPushButton()
        bill1.setStyleSheet("""
                QPushButton {
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    background-repeat: no-repeat;
                    background-position: center;}
                              
                    QPushButton:hover {
                    background-color: lightblue; /* Hover color */
                      
                              
                               }
                              
                    QPushButton:pressed {
                    background-color: #92F7BD; /* Pressed color */
                    color: white; /* Change text color on press */
                        }           
                               """)
        bill1.setFixedHeight(70)
        save_frame_layout.addWidget(bill1,0,0)

        icon = QIcon('./static/Group 32.png')  # تحميل الأيقونة
        bill1.setIcon(icon)
        bill1.setIconSize(QSize(229, 62))


        bill2 = QPushButton()
        bill2.setStyleSheet("""
                QPushButton {
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    background-repeat: no-repeat;
                    background-position: center;}
                              
                    QPushButton:hover {
                    background-color: lightblue; /* Hover color */
                      
                              
                               }
                              
                    QPushButton:pressed {
                    background-color: #92F7BD; /* Pressed color */
                    color: white; /* Change text color on press */
                        }           
                               """)
        bill2.setFixedHeight(70)
        save_frame_layout.addWidget(bill2,0,1) 
        icon = QIcon('./static/Group 33.png')  # تحميل الأيقونة
        bill2.setIcon(icon)
        bill2.setIconSize(QSize(229, 62))   

        bill3 = QPushButton()
        bill3.setStyleSheet("""
                QPushButton {
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    background-repeat: no-repeat;
                    background-position: center;}
                              
                    QPushButton:hover {
                    background-color: lightblue; /* Hover color */
                      
                              
                               }
                              
                    QPushButton:pressed {
                    background-color: #92F7BD; /* Pressed color */
                    color: white; /* Change text color on press */
                        }           
                               """)
        bill3.setFixedHeight(70)
        save_frame_layout.addWidget(bill3,1,0) 
        icon = QIcon('./static/Group 34.png')  # تحميل الأيقونة
        bill3.setIcon(icon)
        bill3.setIconSize(QSize(229, 62))





        bill4 = QPushButton()
        bill4.setStyleSheet("""
                QPushButton {
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    background-repeat: no-repeat;
                    background-position: center;}
                              
                    QPushButton:hover {
                    background-color: lightblue; /* Hover color */
                      
                              
                               }
                              
                    QPushButton:pressed {
                    background-color: #92F7BD; /* Pressed color */
                    color: white; /* Change text color on press */
                        }           
                               """)
        bill4.setFixedHeight(70)
        save_frame_layout.addWidget(bill4,1,1)  

        icon = QIcon('./static/Group 35.png')  # تحميل الأيقونة
        bill4.setIcon(icon)
        bill4.setIconSize(QSize(229, 62))  



        button1 = QPushButton()
        button1.setStyleSheet("""
                QPushButton {
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    
                    background-repeat: no-repeat;
                    background-position: center;}
                              
                    QPushButton:hover {
                    background-color: lightblue; /* Hover color */
                      
                              
                               }
                              
                    QPushButton:pressed {
                    background-color: #92F7BD; /* Pressed color */
                    color: white; /* Change text color on press */
                        }           
                               """)
        
        icon = QIcon('./static/13.png')  # تحميل الأيقونة
        button1.setIcon(icon)
        button1.setIconSize(QSize(229, 62))
       
        save_frame_layout.addWidget(button1,2,0,1,2)



        
        button2 = QPushButton()
        button2.clicked.connect(self.controller.del_lis_show)
        button2.setStyleSheet("""
                    QPushButton{
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    
                    background-repeat: no-repeat;
                    background-position: center;}
                    QPushButton:hover {
                    background-color: lightblue; /* Hover color */
                        }  

                    QPushButton:pressed {
                    background-color: #92F7BD; /* Pressed color */
                    color: white; /* Change text color on press */
                        }       
                              
                               """)
        
        icon = QIcon('./static/14.png')  # تحميل الأيقونة
        button2.setIcon(icon)
        button2.setIconSize(QSize(90, 36))
        
        save_frame_layout.addWidget(button2,3,0,1,2)
        
        

        
        button3 = QPushButton()
        button3.clicked.connect(self.controller.show_deferred)
        button3.setStyleSheet("""
                    QPushButton{
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    
                    background-repeat: no-repeat;
                    background-position: center;}
                    QPushButton:hover {
                    background-color: lightblue; /* Hover color */
                        }  

                    QPushButton:pressed {
                    background-color: #92F7BD; /* Pressed color */
                    color: white; /* Change text color on press */
                        }       
                              
                               """)
        
        icon = QIcon('./static/15.png')  # تحميل الأيقونة
        button3.setIcon(icon)
        button3.setIconSize(QSize(90, 36))
        
        save_frame_layout.addWidget(button3,4,0,1,2)
       










        
class Sales(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.setWindowTitle("المبيعات")
        self.resize(500, 500)

         # فريم جديد
        new_frame = QFrame(self)
        new_frame.setStyleSheet("""background-color: #1A3654; border-radius: 4px;""")
        new_frame.setGeometry(0, 0, self.width(), self.height())
        self.setCentralWidget(new_frame)

        new_layout = QGridLayout(new_frame)

        # فريم العنوان مع Layout خاص به
        lest_label_frame = QFrame()
        layout1 = QVBoxLayout(lest_label_frame)  # استخدام Layout منفصل
        lest_label_frame.setStyleSheet("""
            background-color: #50F296; 
            color: white;
            background-repeat: no-repeat;
            background-position: center;
        """)
        lest_label_frame.setFixedHeight(50)
        # 1,2 لكي تاخذ صف واحد وعمودين الاول والثاني
        new_layout.addWidget(lest_label_frame, 0, 0, 1, 2)  # الهيدر 

        # فريم يحتوي على باقي العناصر مع Layout منفصل
        frame = QFrame()
        new_layout.addWidget(frame, 1, 0, 1, 2)

        # إضافة أيقونة في Layout1 (Layout العنوان)
        icon_label = QLabel(lest_label_frame)
        icon = QIcon('./static/10.png')  
        icon_label.setPixmap(icon.pixmap(100, 100))  # تحديد حجم الأيقونة
        layout1.addWidget(icon_label)



         #انشاء فريم لوضع البيانات الفريم الابيض السفلي
        frame = QFrame()
        data_frame_layout = QVBoxLayout(frame)
        
        # استرجاع البيانات من الموديل عبر الكونترولر
        data_tabel = self.controller.get_bills_from_model()

        total_amount = data_tabel[1]

        total_amount = [float(price) for price in total_amount]

        total_amount = sum(total_amount)
        
        # إنشاء جدول البيانات
        self.table = QTableWidget()

        #جعل حجم الجدول يتناسب مع حجم الشاشه 
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.table.setAlternatingRowColors(True)
        
        # تعيين خلفية الجدول إلى اللون الأبيض
        self.table.setStyleSheet("background-color: white;")

        
        # إعداد الجدول: تعيين الأعمدة
        self.table.setColumnCount(3)  # عدد الأعمدة (المادة، العدد، اسم الشركة، سعر الشراء ,سعر البيع ,تاريخ الانتهاء)
        self.table.setHorizontalHeaderLabels(['المبلغ',"التاريخ","الترميز"])  # العناوين
        
        # تعبئة الجدول بالبيانات
        if data_tabel and len(data_tabel[0]) > 0:  # التأكد من وجود بيانات
            row_count = len(data_tabel[0])  # افتراض أن جميع الأعمدة لها نفس الطول
            self.table.setRowCount(row_count)
        
            # تعبئة البيانات في الجدول
            for row in range(row_count):
                self.table.setItem(row, 2, QTableWidgetItem(str(data_tabel[0][row])))  
                self.table.setItem(row, 0, QTableWidgetItem(data_tabel[1][row]))  # إدخال الاسم
                self.table.setItem(row, 1, QTableWidgetItem(data_tabel[2][row]))
              
        
            # تعديل حجم الأعمدة لتناسب المحتوى بعد تعبئة الجدول
            self.table.resizeColumnsToContents()
        else:
            self.table.setRowCount(0)
        
        # إضافة الجدول إلى التخطيط داخل الفريم
        data_frame_layout.addWidget(self.table)
        
        # تعيين التخطيط للفريم
        frame.setLayout(data_frame_layout)
        new_layout.addWidget(frame,2,0)
        

        
        #انشاء فريم للحفض الفريم الابيض الجانبي
        save_frame = QFrame()
        save_frame.setStyleSheet("""
            border-radius: 4px;
            background-color: #1A3654;
        """)
        save_frame_layout = QGridLayout(save_frame)


        
        label = QLabel("")
        label.setStyleSheet('''
             background-color: #1A3654;
            font-family: Inter;
            font-size:20px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')

        save_frame_layout.addWidget(label,0,0)
        # 1,1 تعني العمود الثاني والصف الثاني

        # 2,1 تعني انهو ياخذ صفين الثاني والثالث وياخذ عمود واحد
        new_layout.addWidget(save_frame,1,0)


        label = QLabel(f'المجموع : {total_amount}')
        label.setStyleSheet('''background-color: #FFF;''')
        label.setFixedHeight(50)
        new_layout.addWidget(label, 3, 0)

        # البحث في فريم الجانبي لل (save frame layout)

        label_history = QLabel("التاريخ")
        label_history.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        save_frame_layout.addWidget(label_history, 0, 1)

        # إضافة QDateEdit جديد لتحديد التاريخ للفلتر
        history_input_filter = QDateEdit()
        history_input_filter.setDate(QDate.currentDate())
        history_input_filter.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        history_input_filter.setDisplayFormat("dd/MM/yyyy")  # تعيين تنسيق التاريخ هنا
        save_frame_layout.addWidget(history_input_filter, 1, 0)

        # إضافة زر لتطبيق الفلتر
        filter_button = QPushButton("تصفية")
        filter_button.setStyleSheet("""
            background-color: #50F296;
            border-radius: 4px;
            color: #000000;
        """)
        save_frame_layout.addWidget(filter_button, 1, 1)

        # دالة لتصفية البيانات حسب التاريخ
        def filter_data_by_date():
            selected_date = history_input_filter.date().toString("dd/MM/yyyy")

            # تصفية البيانات باستخدام التاريخ المحدد
            filtered_data = []
            for row in range(len(data_tabel[0])):
                if data_tabel[2][row] == selected_date:  # assuming date is in column 2 (index 2)
                    filtered_data.append([data_tabel[0][row], data_tabel[1][row], data_tabel[2][row]])

            # تحديث الجدول بالبيانات المفلترة
            self.table.setRowCount(len(filtered_data))
            for row_index, row_data in enumerate(filtered_data):
                self.table.setItem(row_index, 2, QTableWidgetItem(str(row_data[0])))  
                self.table.setItem(row_index, 0, QTableWidgetItem(row_data[1]))  
                self.table.setItem(row_index, 1, QTableWidgetItem(row_data[2]))

            self.table.resizeColumnsToContents()

        # ربط الزر بوظيفة الفلتر
        filter_button.clicked.connect(filter_data_by_date)

        

        




        
class Purchases(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.setWindowTitle("المشتريات")
        self.resize(500, 500)

         # فريم جديد
        new_frame = QFrame(self)
        new_frame.setStyleSheet("""background-color: #1A3654; border-radius: 4px;""")
        new_frame.setGeometry(0, 0, self.width(), self.height())
        self.setCentralWidget(new_frame)

        new_layout = QGridLayout(new_frame)

        # فريم العنوان مع Layout خاص به
        lest_label_frame = QFrame()
        layout1 = QVBoxLayout(lest_label_frame)  # استخدام Layout منفصل
        lest_label_frame.setStyleSheet("""
            background-color: #50F296; 
            color: white;
            background-repeat: no-repeat;
            background-position: center;
        """)
        lest_label_frame.setFixedHeight(50)
        # 1,2 لكي تاخذ صف واحد وعمودين الاول والثاني
        new_layout.addWidget(lest_label_frame, 0, 0, 1, 2)  # الهيدر 

        

        # إضافة أيقونة في Layout1 (Layout العنوان)
        icon_label = QLabel(lest_label_frame)
        icon = QIcon('./static/09.png')  
        icon_label.setPixmap(icon.pixmap(100, 100))  # تحديد حجم الأيقونة
        layout1.addWidget(icon_label)



        save_frame = QFrame()
        save_frame_layout = QGridLayout(save_frame)
        new_layout.addWidget(save_frame, 1, 1)

        label = QLabel("الماده")
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        save_frame_layout.addWidget(label, 0, 1)

        

        self.mat_name = QLineEdit("")
        self.mat_name.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)

        save_frame_layout.addWidget(self.mat_name, 0, 0)


        label = QLabel("عدد العلب")
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        save_frame_layout.addWidget(label, 1, 1)

        

        self.cuont = QLineEdit("")
        self.cuont.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(self.cuont, 1, 0)

        label = QLabel("عدد القطع في كل علبه")
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        save_frame_layout.addWidget(label, 2, 1)

        

        self.cuont_of_set = QLineEdit("")
        self.cuont_of_set.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(self.cuont_of_set, 2, 0)
        

        label = QLabel("النوع")
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        save_frame_layout.addWidget(label, 3, 1)

        

        self.type = QLineEdit("")
        self.type.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)

        save_frame_layout.addWidget(self.type, 3, 0)


        label = QLabel("اسم الشركة")
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        save_frame_layout.addWidget(label, 4, 1)

        

        self.com_name = QLineEdit("")
        self.com_name.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)

        save_frame_layout.addWidget(self.com_name, 4, 0)


        label = QLabel("سعر الشراء للعلبة")
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        save_frame_layout.addWidget(label, 5, 1)

        

        self.buy_price = QLineEdit("")
        self.buy_price.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)

        save_frame_layout.addWidget(self.buy_price, 5, 0)
        

        label = QLabel("سعر البيع للعلبة")
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        save_frame_layout.addWidget(label, 6, 1)

        

        self.sile_price_set = QLineEdit("")
        self.sile_price_set.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)

        save_frame_layout.addWidget(self.sile_price_set, 6, 0)

        label = QLabel("سعر البيع للقطعة")
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        save_frame_layout.addWidget(label, 7, 1)

        

        self.sile_price = QLineEdit("")
        self.sile_price.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)

        save_frame_layout.addWidget(self.sile_price, 7, 0)



        label = QLabel("تاريخ الانتهاء")
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        save_frame_layout.addWidget(label, 8, 1)

        

        self.expiry = QDateEdit()
        self.expiry.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)

        save_frame_layout.addWidget(self.expiry, 8, 0)


         #انشاء فريم لوضع البيانات الفريم الابيض السفلي
        frame = QFrame()
        data_frame_layout = QVBoxLayout(frame)
        
        # استرجاع البيانات من الموديل عبر الكونترولر
        data_tabel = self.controller.get_Purchases_from_model()
        
        # إنشاء جدول البيانات
        self.table = QTableWidget()

        #جعل حجم الجدول يتناسب مع حجم الشاشه 
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.table.setAlternatingRowColors(True)
        
        # تعيين خلفية الجدول إلى اللون الأبيض
        self.table.setStyleSheet("background-color: white;")

        
        # إعداد الجدول: تعيين الأعمدة
        self.table.setColumnCount(10)  # عدد الأعمدة (المادة، العدد، اسم الشركة، سعر الشراء ,سعر البيع ,تاريخ الانتهاء)
        self.table.setHorizontalHeaderLabels(['المادة،', ' العدد', 'النوع', 'اسم الشركة ', ' سعر الشراء للعلبة', 'سعر البيع للعلبة', ' سعر الشراء للقطة', "سعر البيع للقطعة ", "تاريخ الانتهاء",'الترميز'])  # العناوين
        
        # تعبئة الجدول بالبيانات
        if data_tabel and len(data_tabel[0]) > 0:  # التأكد من وجود بيانات
            row_count = len(data_tabel[0])  # افتراض أن جميع الأعمدة لها نفس الطول
            self.table.setRowCount(row_count)
        
            # تعبئة البيانات في الجدول
            for row in range(row_count):
                self.table.setItem(row, 9, QTableWidgetItem(str(data_tabel[0][row])))  
                self.table.setItem(row, 0, QTableWidgetItem(data_tabel[1][row]))  # إدخال الاسم
                self.table.setItem(row, 1, QTableWidgetItem(data_tabel[2][row]))
                self.table.setItem(row, 2, QTableWidgetItem(data_tabel[3][row]))   # إدخال اسم الشركة
                self.table.setItem(row, 3, QTableWidgetItem(str(data_tabel[4][row])))  # إدخال النوع
                self.table.setItem(row, 4, QTableWidgetItem(str(data_tabel[5][row])))
                self.table.setItem(row, 6, QTableWidgetItem(str(data_tabel[6][row])))  # إدخال العدد 
                self.table.setItem(row, 5, QTableWidgetItem(str(data_tabel[7][row]))) #الانتهاء
                self.table.setItem(row, 7, QTableWidgetItem(str(data_tabel[8][row]))) #الانتهاء
                self.table.setItem(row, 8, QTableWidgetItem(str(data_tabel[9][row]))) # العمر المناسب
        
            # تعديل حجم الأعمدة لتناسب المحتوى بعد تعبئة الجدول
            self.table.resizeColumnsToContents()
        else:
            self.table.setRowCount(0)
        
        # إضافة الجدول إلى التخطيط داخل الفريم
        data_frame_layout.addWidget(self.table)
        
        # تعيين التخطيط للفريم
        frame.setLayout(data_frame_layout)
        
        # إضافة الفريم إلى التخطيط الخارجي
        new_layout.addWidget(frame, 1, 0)

        
         #للفريم الاسفل للحفض
        down_save_frame = QFrame()
        down_save_frame.setStyleSheet("""
            border-radius: 4px;
            background-color: #1A3654;
        """)
        down_save_frame_layout = QGridLayout(down_save_frame)



        # 2,1 تعني انهو ياخذ صفين الثاني والثالث وياخذ عمود واحد
        new_layout.addWidget(down_save_frame,2,0,1,2)


         
        #حذف 
        button1 = QPushButton()
        button1.clicked.connect(self.controller.del_purch_show)
        button1.setStyleSheet("""
                   QPushButton {
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    
                    background-repeat: no-repeat;
                    background-position: center;}
                              
                    QPushButton:hover {
                    background-color: lightblue; /* Hover color */
                      
                              
                               }
                              
                    QPushButton:pressed {
                    background-color: #92F7BD; /* Pressed color */
                    color: white; /* Change text color on press */
                        } 
           
                               """)
        
        icon = QIcon('./static/14.png')  # تحميل الأيقونة
        button1.setIcon(icon)
        button1.setIconSize(QSize(90, 36))
        
        down_save_frame_layout.addWidget(button1,0,2)

         #حفظ
        #المجموع 
        button2 = QPushButton()
        button2.clicked.connect(self.send_data_to_controller)
        button2.setStyleSheet("""
                    QPushButton {
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    
                    background-repeat: no-repeat;
                    background-position: center;}
                              
                    QPushButton:hover {
                    background-color: lightblue; /* Hover color */
                      
                              
                               }
                              
                    QPushButton:pressed {
                    background-color: #92F7BD; /* Pressed color */
                    color: white; /* Change text color on press */
                        } 
                             
                               """)
        
        icon = QIcon('./static/Group 29.png')  # تحميل الأيقونة
        button2.setIcon(icon)
        button2.setIconSize(QSize(90, 36))
        
        down_save_frame_layout.addWidget(button2,0,3)
         #المجموع
        button3 = QPushButton()
        button3.clicked.connect(self.controller.update_purch_show)
        button3.setStyleSheet("""
                     QPushButton {
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    
                    background-repeat: no-repeat;
                    background-position: center;}
                              
                    QPushButton:hover {
                    background-color: lightblue; /* Hover color */
                      
                              
                               }
                              
                    QPushButton:pressed {
                    background-color: #92F7BD; /* Pressed color */
                    color: white; /* Change text color on press */
                        }
                             
                               """)
        
        icon = QIcon('./static/20.png')  # تحميل الأيقونة
        button3.setIcon(icon)
        button3.setIconSize(QSize(90, 36))
        
        down_save_frame_layout.addWidget(button3,0,1)

        
        total_input = QLineEdit()
        total_input.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        down_save_frame_layout.addWidget(total_input, 0, 0)


        
    def send_data_to_controller(self):
        # الحصول على البيانات من الواجهة
        name_mat = self.mat_name.text()
        count = float(self.cuont.text()) * float(self.cuont_of_set.text())
        type = self.type.text()
        com_name = self.com_name.text()
        buy_price_for_set = self.buy_price.text()
        buy_price_for_unit = float(self.buy_price.text()) / float(self.cuont_of_set.text())
        sel_price = self.sile_price.text()
        expiry = self.expiry.date().toString("yyyy-MM-dd") 
        sile_price_set = self.sile_price_set.text()
        

        # إرسال البيانات إلى الكونترولر لإضافتها للنموذج
        self.controller.add_Purchases_to_model(name_mat, count, type, com_name , buy_price_for_set, buy_price_for_unit ,sile_price_set ,sel_price , expiry)

        # تحديث الجدول بعد الحفظ
        self.refresh_table()

    def refresh_table(self):
        # استرجاع البيانات من النموذج عبر الكونترولر
        data_tabel = self.controller.get_Purchases_from_model()

        # مسح البيانات القديمة في الجدول
        self.table.setRowCount(0)

        # تعبئة الجدول بالبيانات الجديدة
        if data_tabel and len(data_tabel[0]) > 0:  # التأكد من وجود بيانات
            row_count = len(data_tabel[0])  # افتراض أن جميع الأعمدة لها نفس الطول
            self.table.setRowCount(row_count)
        
            # تعبئة البيانات في الجدول
            for row in range(row_count):
                self.table.setItem(row, 9, QTableWidgetItem(str(data_tabel[0][row])))  
                self.table.setItem(row, 0, QTableWidgetItem(data_tabel[1][row]))  # إدخال الاسم
                self.table.setItem(row, 1, QTableWidgetItem(data_tabel[2][row]))
                self.table.setItem(row, 2, QTableWidgetItem(data_tabel[3][row]))   # إدخال اسم الشركة
                self.table.setItem(row, 3, QTableWidgetItem(str(data_tabel[4][row])))  # إدخال النوع
                self.table.setItem(row, 4, QTableWidgetItem(str(data_tabel[5][row])))
                self.table.setItem(row, 6, QTableWidgetItem(str(data_tabel[6][row])))  # إدخال العدد 
                self.table.setItem(row, 5, QTableWidgetItem(str(data_tabel[7][row]))) #الانتهاء
                self.table.setItem(row, 7, QTableWidgetItem(str(data_tabel[8][row]))) #الانتهاء
                self.table.setItem(row, 8, QTableWidgetItem(str(data_tabel[9][row]))) # العمر المناسب








  

        
class Deferred(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.setWindowTitle("دفع مؤجل")
        self.resize(500, 500)

        self.showMaximized()

         
        # فريم جديد
        new_frame = QFrame(self)
        new_frame.setStyleSheet("""background-color: #1A3654; border-radius: 4px;""")
        new_frame.setGeometry(0, 0, self.width(), self.height())
        self.setCentralWidget(new_frame)

        new_layout = QGridLayout(new_frame)

        # فريم العنوان مع Layout خاص به
        lest_label_frame = QFrame()
        layout1 = QVBoxLayout(lest_label_frame)  # استخدام Layout منفصل
        lest_label_frame.setStyleSheet("""
            background-color: #50F296; 
            color: white;
            background-repeat: no-repeat;
            background-position: center;
        """)
        lest_label_frame.setFixedHeight(50)
        # 1,2 لكي تاخذ صف واحد وعمودين الاول والثاني
        new_layout.addWidget(lest_label_frame, 0, 0, 1, 2)  # الهيدر 

        # فريم يحتوي على باقي العناصر مع Layout منفصل
        frame = QFrame()
        
        new_layout.addWidget(frame, 1, 0, 1, 2)

        # إضافة أيقونة في Layout1 (Layout العنوان)
        icon_label = QLabel(lest_label_frame)
        icon = QIcon('./static/15.png')  
        icon_label.setPixmap(icon.pixmap(100, 100))  # تحديد حجم الأيقونة
        layout1.addWidget(icon_label)


         #انشاء فريم لوضع البيانات الفريم الابيض السفلي
        
         #انشاء فريم لوضع البيانات الفريم الابيض السفلي
        frame = QFrame()
        data_frame_layout = QVBoxLayout(frame)
        
        # استرجاع البيانات من الموديل عبر الكونترولر
        data_tabel = self.controller.get_Deferred_from_model()
        
        # إنشاء جدول البيانات
        self.table = QTableWidget()

        #جعل حجم الجدول يتناسب مع حجم الشاشه 
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.table.setAlternatingRowColors(True)
        
        # تعيين خلفية الجدول إلى اللون الأبيض
        self.table.setStyleSheet("background-color: white;")

        
        # إعداد الجدول: تعيين الأعمدة
        self.table.setColumnCount(5)  # عدد الأعمدة (الاسم، النوع، العدد، تاريخ الانتهاء)
        self.table.setHorizontalHeaderLabels(['اسم العميل', 'رقم الهاتف', 'العنوان', 'السعر', 'الترميز'])  # العناوين
        
        # تعبئة الجدول بالبيانات
        if data_tabel and len(data_tabel[0]) > 0:  # التأكد من وجود بيانات
            row_count = len(data_tabel[0])  # افتراض أن جميع الأعمدة لها نفس الطول
            self.table.setRowCount(row_count)
        
            # تعبئة البيانات في الجدول
            for row in range(row_count): 
                self.table.setItem(row, 0, QTableWidgetItem(data_tabel[1][row]))  # إدخال الاسم
                self.table.setItem(row, 1, QTableWidgetItem(data_tabel[2][row]))  # إدخال رقم الهاتف
                self.table.setItem(row, 2, QTableWidgetItem(str(data_tabel[3][row])))  # إدخال العنوان
                self.table.setItem(row, 3, QTableWidgetItem(str(data_tabel[4][row])))  #السعر
                self.table.setItem(row, 4, QTableWidgetItem(str(data_tabel[0][row])))   #id
        
            # تعديل حجم الأعمدة لتناسب المحتوى بعد تعبئة الجدول
            self.table.resizeColumnsToContents()
        else:
            self.table.setRowCount(0)
        
        # إضافة الجدول إلى التخطيط داخل الفريم
        data_frame_layout.addWidget(self.table)
        
        # تعيين التخطيط للفريم
        frame.setLayout(data_frame_layout)
        
        # إضافة الفريم إلى التخطيط الخارجي
        new_layout.addWidget(frame, 1, 0)
    


        
        #انشاء فريم للحفض الفريم الابيض الجانبي
        save_frame = QFrame()
        save_frame.setStyleSheet("""
            border-radius: 4px;
            background-color: #1A3654;
        """)
        save_frame_layout = QGridLayout(save_frame)
        

       




        label = QLabel("")
        label.setStyleSheet('''
             background-color: #1A3654;
            font-family: Inter;
            font-size:20px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')

        save_frame_layout.addWidget(label,0,2)
        # 1,1 تعني العمود الثاني والصف الثاني

        # 2,1 تعني انهو ياخذ صفين الثاني والثالث وياخذ عمود واحد
        new_layout.addWidget(save_frame,1,1)


        
        
        # البحث في فريم الجانبي لل (save frame layout)

        label_history = QLabel("اسم العميل")
        label_history.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        save_frame_layout.addWidget(label_history, 0, 1)

        self.customer_name = QLineEdit()
        self.customer_name.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget( self.customer_name, 0, 0)


        
        # البحث في فريم الجانبي لل (save frame layout)

        label_history = QLabel("رقم الهاتف ")
        label_history.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        save_frame_layout.addWidget(label_history, 1, 1)

        self.phone_num = QLineEdit()
        self.phone_num.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(self.phone_num , 1, 0)

        ######
        
        
        # البحث في فريم الجانبي لل (save frame layout)

        label_number = QLabel("العنوان")
        label_number.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        save_frame_layout.addWidget(label_number, 2, 1)

        self.address = QLineEdit()
        self.address.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(self.address, 2, 0)



        
        # البحث في فريم الجانبي لل (save frame layout)

        label_End_date = QLabel("السعر ")
        label_End_date.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        save_frame_layout.addWidget(label_End_date, 3, 1)

        self.price = QLineEdit()
        self.price.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(self.price, 3, 0)


         #المجموع 
        button1 = QPushButton()
        button1.clicked.connect(self.send_data_defer_to_controller)
        button1.setStyleSheet("""
                    QPushButton {
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    
                    background-repeat: no-repeat;
                    background-position: center;}
                              
                    QPushButton:hover {
                    background-color: lightblue; /* Hover color */
                      
                              
                               }
                              
                    QPushButton:pressed {
                    background-color: #92F7BD; /* Pressed color */
                    color: white; /* Change text color on press */
                        }
                             
                               """)
        
        icon = QIcon('./static/Group 8 (1).png')  # تحميل الأيقونة
        button1.setIcon(icon)
        button1.setIconSize(QSize(90, 36))
        
        save_frame_layout.addWidget(button1,4,0,1,2)



        button2 = QPushButton()
        button2.clicked.connect(self.controller.update_defer_show)
        button2.setStyleSheet("""
                     QPushButton {
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    
                    background-repeat: no-repeat;
                    background-position: center;}
                              
                    QPushButton:hover {
                    background-color: lightblue; /* Hover color */
                      
                              
                               }
                              
                    QPushButton:pressed {
                    background-color: #92F7BD; /* Pressed color */
                    color: white; /* Change text color on press */
                        }
                             
                               """)
        
        icon = QIcon('./static/20.png')  # تحميل الأيقونة
        button2.setIcon(icon)
        button2.setIconSize(QSize(90, 36))
        
        save_frame_layout.addWidget(button2,5,0,1,2)

        
        button3 = QPushButton()
        button3.clicked.connect(self.controller.del_defer_show)
        button3.setStyleSheet("""
                     QPushButton {
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    
                    background-repeat: no-repeat;
                    background-position: center;}
                              
                    QPushButton:hover {
                    background-color: lightblue; /* Hover color */
                      
                              
                               }
                              
                    QPushButton:pressed {
                    background-color: #92F7BD; /* Pressed color */
                    color: white; /* Change text color on press */
                        }
                             
                               """)
        
        icon = QIcon('./static/14.png')  # تحميل الأيقونة
        button3.setIcon(icon)
        button3.setIconSize(QSize(90, 36))
        
        save_frame_layout.addWidget(button3,6,0,1,2)


        
    def send_data_defer_to_controller(self):
        # الحصول على البيانات من الواجهة
        customer_name = self.customer_name.text()
        phone_num = self.phone_num.text()
        address = self.address.text()
        price = self.price.text()

        # إرسال البيانات إلى الكونترولر لإضافتها للنموذج
        self.controller.add_Deferred_to_model(customer_name, phone_num, address, price)

        # تحديث الجدول بعد الحفظ
        self.refresh_table()

    def refresh_table(self):
        # استرجاع البيانات من النموذج عبر الكونترولر
        data_table = self.controller.get_Deferred_from_model()

        # مسح البيانات القديمة في الجدول
        self.table.setRowCount(0)

        # تعبئة الجدول بالبيانات الجديدة
        if data_table and len(data_table[0]) > 0:
            row_count = len(data_table[0])  # افتراض أن جميع الأعمدة لها نفس الطول
            self.table.setRowCount(row_count)

            
            for row in range(row_count):
                self.table.setItem(row, 4, QTableWidgetItem(str(data_table[0][row])))  # إدخال الاسم
                self.table.setItem(row, 0, QTableWidgetItem(data_table[1][row]))  # إدخال الاسم
                self.table.setItem(row, 1, QTableWidgetItem(data_table[2][row]))  # إدخال النوع
                self.table.setItem(row, 2, QTableWidgetItem(str(data_table[3][row])))  # إدخال العدد
                self.table.setItem(row, 3, QTableWidgetItem(str(data_table[4][row])))

      




           
class Closet(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.setWindowTitle("المخزن")
        self.resize(500, 500)

        
         
        # فريم جديد
        new_frame = QFrame(self)
        new_frame.setStyleSheet("""background-color: #1A3654; border-radius: 4px;""")
        new_frame.setGeometry(0, 0, self.width(), self.height())
        self.setCentralWidget(new_frame)

        new_layout = QGridLayout(new_frame)

        # فريم العنوان مع Layout خاص به
        lest_label_frame = QFrame()
        layout1 = QVBoxLayout(lest_label_frame)  # استخدام Layout منفصل
        lest_label_frame.setStyleSheet("""
            background-color: #50F296; 
            color: white;
            background-repeat: no-repeat;
            background-position: center;
        """)
        lest_label_frame.setFixedHeight(50)
        # 1,2 لكي تاخذ صف واحد وعمودين الاول والثاني
        new_layout.addWidget(lest_label_frame, 0, 0, 1, 2)  # الهيدر 

        # فريم يحتوي على باقي العناصر مع Layout منفصل
        frame = QFrame()
        new_layout.addWidget(frame, 1, 0, 1, 2)

        # إضافة أيقونة في Layout1 (Layout العنوان)
        icon_label = QLabel(lest_label_frame)
        icon = QIcon('./static/16.png')  
        icon_label.setPixmap(icon.pixmap(100, 100))  # تحديد حجم الأيقونة
        layout1.addWidget(icon_label)


         #انشاء فريم لوضع البيانات الفريم الابيض السفلي
        frame = QFrame()
        data_frame_layout = QVBoxLayout(frame)
        
        # استرجاع البيانات من الموديل عبر الكونترولر
        data_tabel = self.controller.get_Purchases_from_model()
        
        # إنشاء جدول البيانات
        self.table = QTableWidget()

        #جعل حجم الجدول يتناسب مع حجم الشاشه 
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.table.setAlternatingRowColors(True)
        
        # تعيين خلفية الجدول إلى اللون الأبيض
        self.table.setStyleSheet("background-color: white;")

        
        # إعداد الجدول: تعيين الأعمدة
        self.table.setColumnCount(8)  # عدد الأعمدة (المادة، العدد، اسم الشركة، سعر الشراء ,سعر البيع ,تاريخ الانتهاء)
        self.table.setHorizontalHeaderLabels(['المادة،', ' العدد،', 'النوع', 'اسم الشركة ', ' سعر الشراء ', "سعر البيع ", "تاريخ الانتهاء",'الترميز'])  # العناوين
        
        # تعبئة الجدول بالبيانات
        if data_tabel and len(data_tabel[0]) > 0:  # التأكد من وجود بيانات
            row_count = len(data_tabel[0])  # افتراض أن جميع الأعمدة لها نفس الطول
            self.table.setRowCount(row_count)
        
            # تعبئة البيانات في الجدول
            for row in range(row_count):
                self.table.setItem(row, 7, QTableWidgetItem(str(data_tabel[0][row])))  
                self.table.setItem(row, 0, QTableWidgetItem(data_tabel[1][row]))  # إدخال الاسم
                self.table.setItem(row, 1, QTableWidgetItem(data_tabel[2][row]))
                self.table.setItem(row, 2, QTableWidgetItem(data_tabel[3][row]))   # إدخال اسم الشركة
                self.table.setItem(row, 3, QTableWidgetItem(str(data_tabel[4][row])))  # إدخال النوع
                self.table.setItem(row, 4, QTableWidgetItem(str(data_tabel[5][row])))  # إدخال العدد 
                self.table.setItem(row, 5, QTableWidgetItem(str(data_tabel[6][row]))) #الانتهاء
                self.table.setItem(row, 65, QTableWidgetItem(str(data_tabel[7][row]))) # العمر المناسب
        
            # تعديل حجم الأعمدة لتناسب المحتوى بعد تعبئة الجدول
            self.table.resizeColumnsToContents()
        else:
            self.table.setRowCount(0)
        
        # إضافة الجدول إلى التخطيط داخل الفريم
        data_frame_layout.addWidget(self.table)
        
        # تعيين التخطيط للفريم
        frame.setLayout(data_frame_layout)
        
        # إضافة الفريم إلى التخطيط الخارجي
        new_layout.addWidget(frame, 1, 0)

        
        #انشاء فريم للحفض الفريم الابيض الجانبي
        save_frame = QFrame()
        save_frame.setStyleSheet("""
            border-radius: 4px;
            background-color: #1A3654;
        """)
        save_frame_layout = QGridLayout(save_frame)
        # save_frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

       




        label = QLabel("")
        label.setStyleSheet('''
             background-color: #1A3654;
            font-family: Inter;
            font-size:20px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')

        save_frame_layout.addWidget(label,0,0)
        # 1,1 تعني العمود الثاني والصف الثاني

        # 2,1 تعني انهو ياخذ صفين الثاني والثالث وياخذ عمود واحد
        new_layout.addWidget(save_frame,1,1)



        
        # البحث في فريم الجانبي لل (save frame layout)

        label_research = QLabel("البحث")
        label_research.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        save_frame_layout.addWidget(label_research, 0, 1)

        research_input = QLineEdit()
        research_input.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(research_input, 0, 0)



        
        # البحث في فريم الجانبي لل (save frame layout)

        label_type = QLabel("النوع")
        label_type.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        save_frame_layout.addWidget(label_type, 1, 1)

        type_input = QLineEdit()
        type_input.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(type_input, 1, 0)


        
        #حذف فقط
        button1 = QPushButton()
        button1.setStyleSheet("""
                    QPushButton {
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    
                    background-repeat: no-repeat;
                    background-position: center;}
                              
                    QPushButton:hover {
                    background-color: lightblue; /* Hover color */
                      
                              
                               }
                              
                    QPushButton:pressed {
                    background-color: #92F7BD; /* Pressed color */
                    color: white; /* Change text color on press */
                        } 
                             
                               """)
        
        icon = QIcon('./static/14.png')  # تحميل الأيقونة
        button1.setIcon(icon)
        button1.setIconSize(QSize(90, 36))
        
        save_frame_layout.addWidget(button1,2,0,1,2)
        

        


        
class Data_analysis(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.setWindowTitle("تحليل")
        self.resize(500, 500)


#####ازرار الالمؤجل

class DelDefer(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.setWindowTitle("تعديل المادة")
        self.resize(300, 250)


        new_frame = QFrame(self)
        new_frame.setStyleSheet("""background-color: #1A3654; border-radius: 4px;""")
        new_frame.setGeometry(0, 0, self.width(), self.height())
        self.setCentralWidget(new_frame)

        new_layout = QGridLayout(new_frame)


        label = QLabel('اكتب ترميز المنتج الذي تريد حذفه')
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        new_layout.addWidget(label,0,1)

        self.id_defe = QLineEdit('')
        self.id_defe.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        new_layout.addWidget(self.id_defe,0,0)

        button1 = QPushButton()
        button1.clicked.connect(self.send_id_defe_to_controller)
        button1.setStyleSheet("""
                     QPushButton {
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    
                    background-repeat: no-repeat;
                    background-position: center;}
                              
                    QPushButton:hover {
                    background-color: lightblue; /* Hover color */
                      
                              
                               }
                              
                    QPushButton:pressed {
                    background-color: #92F7BD; /* Pressed color */
                    color: white; /* Change text color on press */
                        }
                             
                               """)
        
        icon = QIcon('./static/14.png')  # تحميل الأيقونة
        button1.setIcon(icon)
        button1.setIconSize(QSize(90, 36))
        
        new_layout.addWidget(button1,1,0,1,2)

    def send_id_defe_to_controller(self):
        id_defe = self.id_defe.text()
        self.controller.del_Deferred_from_model(id_defe)



class UpdateDefer(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.setWindowTitle("تعديل مادة")
        self.resize(300, 250)

        new_frame = QFrame(self)
        new_frame.setStyleSheet("""background-color: #1A3654; border-radius: 4px;""")
        new_frame.setGeometry(0, 0, self.width(), self.height())
        self.setCentralWidget(new_frame)

        new_layout = QGridLayout(new_frame)


        label = QLabel('اكتب ترميز المنتج الذي تريد تعديله')
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        new_layout.addWidget(label,0,1)

        self.id_defe = QLineEdit('')
        self.id_defe.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        new_layout.addWidget(self.id_defe,0,0)


        label = QLabel('اسم العميل')
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        new_layout.addWidget(label,1,1)

        self.cos_name = QLineEdit('')
        self.cos_name.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        new_layout.addWidget(self.cos_name,1,0)
        

        label = QLabel(' رقم الهاتف')
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        new_layout.addWidget(label,2,1)



        self.cos_phone= QLineEdit('')
        self.cos_phone.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        new_layout.addWidget(self.cos_phone,2,0)


        label = QLabel('العنوان')
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        new_layout.addWidget(label,3,1)



        self.cos_location = QLineEdit('')
        self.cos_location.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        new_layout.addWidget(self.cos_location,3,0)



        
        label = QLabel('السعر')
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        new_layout.addWidget(label,4,1)



        self.price = QLineEdit('')
        self.price.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        new_layout.addWidget(self.price,4,0)





        button = QPushButton()
        button.clicked.connect(self.send_update_data_defer_to_controller)
        button.setStyleSheet("""
                     QPushButton {
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    
                    background-repeat: no-repeat;
                    background-position: center;}
                              
                    QPushButton:hover {
                    background-color: lightblue; /* Hover color */
                      
                              
                               }
                              
                    QPushButton:pressed {
                    background-color: #92F7BD; /* Pressed color */
                    color: white; /* Change text color on press */
                        }
                             
                               """)
        
        icon = QIcon('./static/20.png')  # تحميل الأيقونة
        button.setIcon(icon)
        button.setIconSize(QSize(90, 36))

        new_layout.addWidget(button,5,0,1,2)


    def send_update_data_defer_to_controller(self):
        id_defe = self.id_defe.text()
        cos_name = self.cos_name.text()
        cos_phone = self.cos_phone.text()
        cos_location = self.cos_location.text()
        price = self.price.text()
        self.controller.update_Deferred_to_model(id_defe,cos_name, cos_phone, cos_location , price)


##################المشتريات



class Delpur(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.setWindowTitle("حذف المادة")
        self.resize(300, 250)


         
        # فريم جديد
        new_frame = QFrame(self)
        new_frame.setStyleSheet("""background-color: #1A3654; border-radius: 4px;""")
        new_frame.setGeometry(0, 0, self.width(), self.height())
        self.setCentralWidget(new_frame)

        new_layout = QGridLayout(new_frame)


        label = QLabel('اكتب ترميز المنتج الذي تريد حذفه')
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        new_layout.addWidget(label,0,1)

        self.id_mat = QLineEdit('')
        self.id_mat.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        new_layout.addWidget(self.id_mat,0,0)

        button1 = QPushButton()
        button1.clicked.connect(self.send_id_purch_to_controller)
        button1.setStyleSheet("""
                     QPushButton {
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    
                    background-repeat: no-repeat;
                    background-position: center;}
                              
                    QPushButton:hover {
                    background-color: lightblue; /* Hover color */
                      
                              
                               }
                              
                    QPushButton:pressed {
                    background-color: #92F7BD; /* Pressed color */
                    color: white; /* Change text color on press */
                        }
                             
                               """)
        
        icon = QIcon('./static/14.png')  # تحميل الأيقونة
        button1.setIcon(icon)
        button1.setIconSize(QSize(90, 36))
        
        new_layout.addWidget(button1,1,0,1,2)

    def send_id_purch_to_controller(self):
        id_purch = self.id_mat.text()
        self.controller.del_Purchases_from_model(id_purch)



class Updatepurch(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.setWindowTitle("تعديل مادة")
        self.resize(300, 250)


         
        # فريم جديد
        new_frame = QFrame(self)
        new_frame.setStyleSheet("""background-color: #1A3654; border-radius: 4px;""")
        new_frame.setGeometry(0, 0, self.width(), self.height())
        self.setCentralWidget(new_frame)

        new_layout = QGridLayout(new_frame)


        label = QLabel('اكتب ترميز المنتج الذي تريد تعديله')
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        new_layout.addWidget(label,0,1)

        self.purch_id = QLineEdit()
        self.purch_id.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        new_layout.addWidget(self.purch_id,0,0)


        label = QLabel('اسم المادة')
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        new_layout.addWidget(label,1,1)

        self.name_mat = QLineEdit()
        self.name_mat.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        new_layout.addWidget(self.name_mat,1,0)
        

        label = QLabel('اسم الشركة')
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        new_layout.addWidget(label,2,1)



        self.name_com = QLineEdit()
        self.name_com.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        new_layout.addWidget(self.name_com,2,0)


        label = QLabel('سعر الشراء')
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        new_layout.addWidget(label,3,1)



        self.buy_price = QLineEdit()
        self.buy_price.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        new_layout.addWidget(self.buy_price,3,0)
        


        label = QLabel('العدد ')
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        new_layout.addWidget(label,4,1)



        self.count = QLineEdit()
        self.count.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        new_layout.addWidget(self.count,4,0)




        label = QLabel('النوع')
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        new_layout.addWidget(label,5,1)



        self.type = QLineEdit()
        self.type.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        new_layout.addWidget(self.type,5,0)
        




        label = QLabel("تاريخ الانتهاء")
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        new_layout.addWidget(label,7,1)

        self.expiry = QDateEdit()
        # تعيين التاريخ الافتراضي ليكون تاريخ اليوم
        self.expiry.setDate(QDate.currentDate())

        # تعيين تنسيق العرض ليشمل اليوم والشهر والسنة فقط
        self.expiry.setDisplayFormat("dd/MM/yyyy")


        self.expiry.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        new_layout.addWidget(self.expiry,7,0)




        label = QLabel(' سعر البيع ')
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        new_layout.addWidget(label,6,1)



        self.sel_price = QLineEdit()
        self.sel_price.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        new_layout.addWidget(self.sel_price,6,0)

 

        button = QPushButton()
        button.clicked.connect(self.send_update_purch_to_controller)
        button.setStyleSheet("""
                     QPushButton {
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    
                    background-repeat: no-repeat;
                    background-position: center;}
                              
                    QPushButton:hover {
                    background-color: lightblue; /* Hover color */
                      
                              
                               }
                              
                    QPushButton:pressed {
                    background-color: #92F7BD; /* Pressed color */
                    color: white; /* Change text color on press */
                        }
                             
                               """)
        
        icon = QIcon('./static/20.png')  # تحميل الأيقونة
        button.setIcon(icon)
        button.setIconSize(QSize(90, 36))

        new_layout.addWidget(button,8,0,1,2)

    def send_update_purch_to_controller(self):
        purch_id = self.purch_id.text()
        name_mat = self.name_mat.text()
        name_com = self.name_com.text()
        buy_price = self.buy_price.text()
        count = self.count.text()
        expiry = self.expiry.date().toString('yyyy-MM-dd')
        sel_price = self.sel_price.text()
        type = self.type.text()
        self.controller.update_Purchases_to_model(purch_id, name_mat, count, type, name_com , buy_price ,sel_price , expiry)


class Dellists(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.setWindowTitle("حذف المادة")
        self.resize(300, 250)


         
        # فريم جديد
        new_frame = QFrame(self)
        new_frame.setStyleSheet("""background-color: #1A3654; border-radius: 4px;""")
        new_frame.setGeometry(0, 0, self.width(), self.height())
        self.setCentralWidget(new_frame)

        new_layout = QGridLayout(new_frame)


        label = QLabel('اكتب ترميز المنتج الذي تريد حذفه')
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        new_layout.addWidget(label,0,1)

        self.id_list = QLineEdit('')
        self.id_list.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        new_layout.addWidget(self.id_list,0,0)

        button1 = QPushButton()
        button1.clicked.connect(self.send_id_list_to_controller)
        button1.setStyleSheet("""
                     QPushButton {
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    
                    background-repeat: no-repeat;
                    background-position: center;}
                              
                    QPushButton:hover {
                    background-color: lightblue; /* Hover color */
                      
                              
                               }
                              
                    QPushButton:pressed {
                    background-color: #92F7BD; /* Pressed color */
                    color: white; /* Change text color on press */
                        }
                             
                               """)
        
        icon = QIcon('./static/14.png')  # تحميل الأيقونة
        button1.setIcon(icon)
        button1.setIconSize(QSize(90, 36))
        
        new_layout.addWidget(button1,1,0,1,2)

    def send_id_list_to_controller(self):
        id_list = self.id_list.text()
        self.controller.del_list_from_model(id_list)

        print("sse")





