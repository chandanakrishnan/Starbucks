class Starbucks():
    #Attributes temp,size,type
    #Methods get_order, calculate_prize, print_total 
    temp = "hot"
    size = "Large"
    type = "Latte"
    #Constructor 
    def __init__(self):
        self.type, self.size, self.temp = self.user_request()
    # def __init__(self,New_temp,New_size,New_type):
    #     self.temp = New_temp
    #     self.size = New_size
    #     self.type = New_type
    #gets and sets
    def get_temp(self):
        return self.temp
    def set_temp(self,New_temp):
        self.temp = New_temp
    def get_size(self):
        return self.size
    def set_size(self,New_size):
        self.size = New_size
    def get_type(self):
        return self.type
    def set_type(self,New_type):
        self.type = New_type

    #Methods
    def get_order(self):
        order = ("please enter your order:",self.get_order)
        return order
    def caalculate_prize(self):
        prize = ("prize of the order: ",self.caalculate_prize)
        return prize
    def print_total(self):
        total = ("total :",self.print_total)

    def user_request(self):
        type_coffee = str(input("What is the type of coffee that you want?"))
        size_coffee = str(input("What is the size of coffee that you want?"))
        temperature_coffee = str(input("What is the temperature of coffee that you want?"))
        return type_coffee, size_coffee, temperature_coffee
    def final_price(self):
        #TO DO: calculate the price according to the request, temperature and size
        return 1

    def display(self):
        print("****************")
        print("temp: ", self.temp)
        print("size: ", self.size)
        print("type: ", self.type)
    
    
#Main
if __name__ =='__main__' :
    #starbucks = Starbucks("cold","large","latte")
    starbucks = Starbucks()
    starbucks.display()



 