

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

        # Button 5
        button5 = QPushButton()
        button5.setStyleSheet("""
            QPushButton {
                background-color: #FFF;
                border-radius: 5px;
                padding: 10px;
                font-size: 16px;
                background-image: url('./static/Group 5.png');
                background-repeat: no-repeat;
                background-position: center;
            }
            QPushButton:hover {
                background-color: #E9FDF2;
            }
        """)
        button5.setIcon(icon)
        button5.clicked.connect(controller.show_materials)
        button5.setIconSize(QSize(250, 250))
        frame_layout.addWidget(button5, 1, 1)

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
        frame_layout.addWidget(button6, 1, 2)

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
        frame_layout.addWidget(button7, 2, 0)


        
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
        layout2 = QGridLayout(frame)
        new_layout.addWidget(frame, 1, 0, 1, 2)

        # إضافة أيقونة في Layout1 (Layout العنوان)
        icon_label = QLabel(lest_label_frame)
        icon = QIcon('./static/Group 28.png')  
        icon_label.setPixmap(icon.pixmap(100, 100))  # تحديد حجم الأيقونة
        layout1.addWidget(icon_label)



        
        #انشاء فريم لوضع البيانات الفريم الابيض السفلي
        frame = QFrame()
        frame.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        frame.setFixedHeight(700)
        new_layout.addWidget(frame,1,0)
        frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)


        
        #انشاء فريم للحفض الفريم الابيض الجانبي
        save_frame = QFrame()
        save_frame.setStyleSheet("""
            border-radius: 4px;
            background-color: #1A3654;
        """)
        save_frame_layout = QGridLayout(save_frame)
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
        

        frame_whit = QFrame()
        frame_whit.setStyleSheet("""
         border-radius:4px;
         background-color: #fff;
       """)
        frame_whit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
       
        frame_whit.setFixedHeight(50)  
        save_frame_layout.addWidget(frame_whit, 0, 0)
        



        frame_whit2 = QFrame()
        frame_whit2.setStyleSheet("""
         border-radius: 4px;
         background-color: #fff;
     """)
        frame_whit2.setFixedHeight(50)
        frame_whit2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed) 
        save_frame_layout.addWidget(frame_whit2, 0, 1)

        frame_whit3 = QFrame()
        frame_whit3.setStyleSheet("""
         border-radius: 4px;
         background-color: #fff;
       """)
        frame_whit3.setFixedHeight(50)
        frame_whit3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)  
        save_frame_layout.addWidget(frame_whit3, 0, 2)


        frame_whit4 = QFrame()
        frame_whit4.setStyleSheet("""
        border-radius: 4px;
        background-color: #fff;
       """)
        frame_whit4.setFixedHeight(50)
        frame_whit4.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)  
        save_frame_layout.addWidget(frame_whit4, 0, 3)

        






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
       
        save_frame_layout.addWidget(button1,1,0)



        
        button2 = QPushButton()
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
        
        save_frame_layout.addWidget(button2,2,0)
        
        

        
        button3 = QPushButton()
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
        
        save_frame_layout.addWidget(button3,3,0)
       










        
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
        layout2 = QGridLayout(frame)
        new_layout.addWidget(frame, 1, 0, 1, 2)

        # إضافة أيقونة في Layout1 (Layout العنوان)
        icon_label = QLabel(lest_label_frame)
        icon = QIcon('./static/10.png')  
        icon_label.setPixmap(icon.pixmap(100, 100))  # تحديد حجم الأيقونة
        layout1.addWidget(icon_label)



         #انشاء فريم لوضع البيانات الفريم الابيض السفلي
        frame = QFrame()
        frame.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        frame.setFixedHeight(700)
        new_layout.addWidget(frame,2,0)
        frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        
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
        new_layout.addWidget(save_frame,2,1)



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

        history_input = QLineEdit()
        history_input.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(history_input, 0, 0)


        #المجموع 
        button3 = QPushButton()
        button3.setStyleSheet("""
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    
                    background-repeat: no-repeat;
                    background-position: center;
                             
                               """)
        
        icon = QIcon('./static/Group 9 (1).png')  # تحميل الأيقونة
        button3.setIcon(icon)
        button3.setIconSize(QSize(90, 36))
        
        save_frame_layout.addWidget(button3,1,0)
        


        total_input = QLineEdit()
        total_input.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(total_input, 2, 0)



        
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


        label = QLabel("العدد")
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


        label = QLabel("اسم الشركة")
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        save_frame_layout.addWidget(label, 2, 1)

        

        self.cuont = QLineEdit("")
        self.cuont.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)

        save_frame_layout.addWidget(self.cuont, 2, 0)


        label = QLabel("سعر الشراء")
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        save_frame_layout.addWidget(label, 3, 1)

        

        self.cuont = QLineEdit("")
        self.cuont.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)

        save_frame_layout.addWidget(self.cuont, 3, 0)



        label = QLabel("سعر البيع")
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        save_frame_layout.addWidget(label, 4, 1)

        

        self.cuont = QLineEdit("")
        self.cuont.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)

        save_frame_layout.addWidget(self.cuont, 5, 0)



        label = QLabel("تاريخ الانتهاء")
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        save_frame_layout.addWidget(label, 5, 1)

        

        self.cuont = QLineEdit("")
        self.cuont.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)

        save_frame_layout.addWidget(self.cuont, 4, 0)


         #انشاء فريم لوضع البيانات الفريم الابيض السفلي
        frame = QFrame()
        frame.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        new_layout.addWidget(frame,1,0)
        frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        
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
        button3.setStyleSheet("""
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    
                    background-repeat: no-repeat;
                    background-position: center;
                             
                               """)
        
        icon = QIcon('./static/Group 9 (1).png')  # تحميل الأيقونة
        button3.setIcon(icon)
        button3.setIconSize(QSize(90, 36))
        
        down_save_frame_layout.addWidget(button3,0,1)

        
        total_input = QLineEdit()
        total_input.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        down_save_frame_layout.addWidget(total_input, 0, 0)








  

        
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

      

class Materials(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.setWindowTitle("اضافة مواد")
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
        icon = QIcon('./static/17.png')  
        icon_label.setPixmap(icon.pixmap(100, 100))  # تحديد حجم الأيقونة
        layout1.addWidget(icon_label)



         #انشاء فريم لوضع البيانات الفريم الابيض السفلي
        frame = QFrame()
        data_frame_layout = QVBoxLayout(frame)
        
        # استرجاع البيانات من الموديل عبر الكونترولر
        data_tabel = self.controller.get_mat_from_model()
        
        # إنشاء جدول البيانات
        self.table = QTableWidget()

        #جعل حجم الجدول يتناسب مع حجم الشاشه 
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.table.setAlternatingRowColors(True)
        
        # تعيين خلفية الجدول إلى اللون الأبيض
        self.table.setStyleSheet("background-color: white;")

        
        # إعداد الجدول: تعيين الأعمدة
        self.table.setColumnCount(7)  # عدد الأعمدة (الاسم، النوع، العدد، تاريخ الانتهاء)
        self.table.setHorizontalHeaderLabels(['الاسم', 'اسم الشركة', 'نوع ', 'العدد ', 'تاريخ الانتهاء',"العمر المناسب", 'الترميز'])  # العناوين
        
        # تعبئة الجدول بالبيانات
        if data_tabel and len(data_tabel[0]) > 0:  # التأكد من وجود بيانات
            row_count = len(data_tabel[0])  # افتراض أن جميع الأعمدة لها نفس الطول
            self.table.setRowCount(row_count)
        
            # تعبئة البيانات في الجدول
            for row in range(row_count):
                self.table.setItem(row, 6, QTableWidgetItem(str(data_tabel[0][row])))  
                self.table.setItem(row, 0, QTableWidgetItem(data_tabel[1][row]))  # إدخال الاسم
                self.table.setItem(row, 1, QTableWidgetItem(data_tabel[2][row]))  # إدخال اسم الشركة
                self.table.setItem(row, 2, QTableWidgetItem(str(data_tabel[3][row])))  # إدخال النوع
                self.table.setItem(row, 3, QTableWidgetItem(str(data_tabel[4][row])))  # إدخال العدد 
                self.table.setItem(row, 4, QTableWidgetItem(str(data_tabel[5][row]))) #الانتهاء
                self.table.setItem(row, 5, QTableWidgetItem(str(data_tabel[6][row]))) # العمر المناسب
        
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

        label_history = QLabel("اسم المادة")
        label_history.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        save_frame_layout.addWidget(label_history, 0, 1)

        self.name_mat = QLineEdit()
        self.name_mat.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(self.name_mat, 0, 0)



        
        # البحث في فريم الجانبي لل (save frame layout)

        label_history = QLabel("اسم  الشركة")
        label_history.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        save_frame_layout.addWidget(label_history, 1, 1)

        self.name_com = QLineEdit()
        self.name_com.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(self.name_com, 1, 0)

        ######
        
        
        # البحث في فريم الجانبي لل (save frame layout)

        label_number = QLabel("النوع")
        label_number.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        save_frame_layout.addWidget(label_number, 2, 1)

        self.type_mat = QLineEdit()
        self.type_mat.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(self.type_mat, 2, 0)

        label_number = QLabel("العدد")
        label_number.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        save_frame_layout.addWidget(label_number, 3, 1)

        self.count = QLineEdit()
        self.count.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(self.count, 3, 0)



        
        # البحث في فريم الجانبي لل (save frame layout)

        label_End_date = QLabel("تاريخ الانتهاء")
        label_End_date.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        save_frame_layout.addWidget(label_End_date, 4, 1)

        self.expiry = QDateEdit()
        # تعيين التاريخ الافتراضي ليكون تاريخ اليوم
        self.expiry.setDate(QDate.currentDate())

        # تعيين تنسيق العرض ليشمل اليوم والشهر والسنة فقط
        self.expiry.setDisplayFormat("dd/MM/yyyy")


        self.expiry.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(self.expiry, 4, 0)


        label_number = QLabel("العمر المناسب")
        label_number.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        save_frame_layout.addWidget(label_number, 5, 1)

        self.Suitable_age = QLineEdit()
        self.Suitable_age.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        save_frame_layout.addWidget(self.Suitable_age, 5, 0)


         #المجموع 
        button1 = QPushButton()
        button1.clicked.connect(self.send_data_to_controller)
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
        
        save_frame_layout.addWidget(button1,6,0,1,2)
        




        button2 = QPushButton()
        button2.clicked.connect(self.controller.update_mat_show)
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
        
        save_frame_layout.addWidget(button2,7,0,1,2)

        
        button3 = QPushButton()
        button3.clicked.connect(self.controller.del_mat_show)
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
        
        save_frame_layout.addWidget(button3,8,0,1,2)


    def send_data_to_controller(self):
        # الحصول على البيانات من الواجهة
        name_mat = self.name_mat.text()
        name_com = self.name_com.text()
        type_mat = self.type_mat.text()
        count = self.count.text()
        expiry = self.expiry.date().toString('yyyy-MM-dd')
        Suitable_age = self.Suitable_age.text()

        # إرسال البيانات إلى الكونترولر لإضافتها للنموذج
        self.controller.add_mat_to_model(name_mat, name_com, type_mat, count, expiry, Suitable_age)

        # تحديث الجدول بعد الحفظ
        self.refresh_table()

    def refresh_table(self):
        # استرجاع البيانات من النموذج عبر الكونترولر
        data_table = self.controller.get_mat_from_model()

        # مسح البيانات القديمة في الجدول
        self.table.setRowCount(0)

        # تعبئة الجدول بالبيانات الجديدة
        if data_table and len(data_table[0]) > 0:
            row_count = len(data_table[0]) 
            self.table.setRowCount(row_count)

            for row in range(row_count):
                self.table.setItem(row, 6, QTableWidgetItem(str(data_table[0][row])))  
                self.table.setItem(row, 0, QTableWidgetItem(data_table[1][row]))  
                self.table.setItem(row, 1, QTableWidgetItem(data_table[2][row]))  
                self.table.setItem(row, 2, QTableWidgetItem(str(data_table[3][row]))) 
                self.table.setItem(row, 3, QTableWidgetItem(str(data_table[4][row])))  
                self.table.setItem(row, 4, QTableWidgetItem(str(data_table[5][row])))
                self.table.setItem(row, 5, QTableWidgetItem(str(data_table[6][row])))





           
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
        frame.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        frame.setFixedHeight(700)
        new_layout.addWidget(frame,1,0)
        frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        
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


########mat


class DelMat(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.setWindowTitle("تعديل المادة")
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
        button1.clicked.connect(self.send_id_mat_to_controller)
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

    def send_id_mat_to_controller(self):
        id_mat = self.id_mat.text()
        self.controller.del_mat_from_model(id_mat)

 
class UpdateMat(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.setWindowTitle("حذف مادة")
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

        self.mat_id = QLineEdit('')
        self.mat_id.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        new_layout.addWidget(self.mat_id,0,0)


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

        self.name_mat = QLineEdit('')
        self.name_mat.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        new_layout.addWidget(self.name_mat,1,0)
        

        label = QLabel('اسم الشركة  ')
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        new_layout.addWidget(label,2,1)



        self.name_com = QLineEdit('')
        self.name_com.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        new_layout.addWidget(self.name_com,2,0)


        label = QLabel('النوع ')
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        new_layout.addWidget(label,3,1)



        self.type_mat = QLineEdit('')
        self.type_mat.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        new_layout.addWidget(self.type_mat,3,0)
        


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



        self.count = QLineEdit('')
        self.count.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        new_layout.addWidget(self.count,4,0)
        




        label = QLabel("تاريخ الانتهاء")
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        new_layout.addWidget(label,5,1)

        self.expiry = QDateEdit()
        # تعيين التاريخ الافتراضي ليكون تاريخ اليوم
        self.expiry.setDate(QDate.currentDate())

        # تعيين تنسيق العرض ليشمل اليوم والشهر والسنة فقط
        self.expiry.setDisplayFormat("dd/MM/yyyy")


        self.expiry.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        new_layout.addWidget(self.expiry,5,0)




        label = QLabel('العمر المناسب ')
        label.setStyleSheet('''
            color: #FFF;
            font-family: Inter;
            font-size: 14px;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
        ''')
        new_layout.addWidget(label,6,1)



        self.Suitable_age = QLineEdit('')
        self.Suitable_age.setStyleSheet("""
            border-radius: 4px;
            background-color: #fff;
        """)
        new_layout.addWidget(self.Suitable_age,6,0)

 

        button = QPushButton()
        button.clicked.connect(self.send_update_data_to_controller)
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

        new_layout.addWidget(button,7,0,1,2)

    def send_update_data_to_controller(self):
        mat_id = self.mat_id.text()
        name_mat = self.name_mat.text()
        name_com = self.name_com.text()
        type_mat = self.type_mat.text()
        count = self.count.text()
        expiry = self.expiry.date().toString('yyyy-MM-dd')
        Suitable_age = self.Suitable_age.text()
        self.controller.update_mat_to_model(mat_id, name_mat, name_com, type_mat, count, expiry, Suitable_age)












