from view import *
from model import *


class Controller:
    def __init__(self):
        self.view = MyView(self)
        self.model = Model()

    def show_list(self):
        self.show_list_add = Lists(self)
        self.show_list_add.show() 

    
    def show_sales(self):
        self.show_sales_add = Sales(self)
        self.show_sales_add.show() 

   


    def show_Purchases(self):
        self.show_Purchases_add = Purchases(self)
        self.show_Purchases_add.show() 

    def show_deferred(self):
        self.show_deferred_add = Deferred(self)
        self.show_deferred_add.show() 


      
    def show_materials (self):
        self.show_materials_add =  Materials(self)
        self.show_materials_add.show() 

     
      
    def show_closet(self):
        self.show_closet_add = Closet(self)
        self.show_closet_add.show() 


         
    def show_Data_analysis(self):
        self.show_Data_analysis_add = Data_analysis(self)
        self.show_Data_analysis_add.show()





        #############################  المؤجل




    def del_defer_show(self):
        self.show_del_defer = DelDefer(self)
        self.show_del_defer.show()

    


    def add_Deferred_to_model(self, customer_name, phone_num, address, price):
        self.model.add_Deferred(customer_name, phone_num, address, price)

    def get_Deferred_from_model(self):
        defe_id, customer_name, phone_num, address, price = self.model.get_Deferred()
        return defe_id, customer_name, phone_num, address, price
    
    def del_Deferred_from_model(self,deferred_id):
        self.model.del_Deferred(deferred_id)
        self.show_deferred()

    def update_defer_show(self):
        self.show_update_defer = UpdateDefer(self)
        self.show_update_defer.show()


    def update_Deferred_to_model(self, deferred_id, customer_name, phone_num, address, price):
        self.model.update_Deferred(deferred_id, customer_name, phone_num, address, price)
        self.show_deferred()


        #################pur

        
    def del_purch_show(self):
        self.show_del_purch = Delpur(self)
        self.show_del_purch.show()

    


    def add_Purchases_to_model(self,name_mat, count, type, com_name , buy_price_for_set, buy_price_for_unit ,sile_price_set ,sel_price , expiry):
        self.model.add_Purchases(name_mat, count, type, com_name , buy_price_for_set, buy_price_for_unit ,sile_price_set ,sel_price , expiry)

    def get_Purchases_from_model(self):
        return self.model.get_purchases()
    
    def del_Purchases_from_model(self,purchases_id):
        self.model.del_Purchases(purchases_id)
        self.show_Purchases()

    def update_purch_show(self):
        self.show_update_purch = Updatepurch(self)
        self.show_update_purch.show()


    def update_Purchases_to_model(self, purchases_id, name_mat, count, type, com_name , buy_price ,sel_price , expir):
        self.model.update_Purchases(purchases_id, name_mat, count, type, com_name , buy_price ,sel_price , expir)
        self.show_Purchases()

###################lists
  
    def del_lis_show(self):
        self.show_del_lis = Dellists(self)
        self.show_del_lis.show()


        
    def del_list_from_model(self,list_id):
        self.model.del_list(list_id)
        self.show_list()


################# bills  


    def get_bills_from_model(self):
        return self.model.get_bill()
        